import re
import os
import platform

class HashExtractor:
    def __init__(self):
        self.algorithms = {
            r"^\$1\$[a-zA-Z0-9./]{8}\$[a-zA-Z0-9./]{22}$": "MD5-based crypt",
            r"^\$5\$[a-zA-Z0-9./]{8,16}\$[a-zA-Z0-9./]{43}$": "SHA-256-based crypt",
            r"^\$6\$[a-zA-Z0-9./]{8,16}\$[a-zA-Z0-9./]{86}$": "SHA-512-based crypt",
            r"^[a-fA-F0-9]{32}$": "MD5 or NTLM",
            r"^[a-fA-F0-9]{40}$": "SHA-1",
            r"^[a-fA-F0-9]{64}$": "SHA-256",
        }

    def identify_algorithm(self, hash_str):
        """Identifies the likely hashing algorithm based on regex patterns."""
        for pattern, name in self.algorithms.items():
            if re.match(pattern, hash_str):
                return name
        return "Unknown"

    def simulate_linux_extraction(self):
        """Simulates extracting from /etc/shadow."""
        # In a real scenario, this would require root privileges.
        # Format: user:$6$salt$hash:12345:0:99999:7:::
        return [
            "root:$6$rounds=5000$saltsalt$8.Yx8N.p6r7l5X... (truncated)",
            "user1:$1$salt$H6M6.q.G.h.p. (truncated)",
            "admin:$6$qwer$zxcv... (truncated)"
        ]

    def get_windows_export_commands(self):
        """Returns the commands needed to export Windows SAM/SYSTEM hives."""
        return [
            r"reg save HKLM\SAM sam.save",
            r"reg save HKLM\SYSTEM system.save",
            r"reg save HKLM\SECURITY security.save"
        ]

    def parse_shadow_file(self, content):
        """Parses /etc/shadow content into a list of (user, hash)."""
        extracted = []
        for line in content:
            parts = line.split(':')
            if len(parts) >= 2:
                user = parts[0]
                pwd_hash = parts[1]
                if pwd_hash not in ['*', '!', '']:
                    extracted.append((user, pwd_hash))
        return extracted

if __name__ == "__main__":
    extractor = HashExtractor()
    test_hash = "$6$rounds=5000$saltsalt$8.Yx8N.p6r7l5X..."
    print(f"Hash: {test_hash}")
    print(f"Detected: {extractor.identify_algorithm(test_hash)}")
    
    print("\nWindows SAM Export Commands:")
    for cmd in extractor.get_windows_export_commands():
        print(f"  {cmd}")
