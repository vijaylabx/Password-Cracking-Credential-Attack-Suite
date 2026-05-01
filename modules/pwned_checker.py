import hashlib
import requests
import sys

class PwnedChecker:
    """Checks if a password has been compromised in a data breach using HIBP API."""
    
    def check_pwned_status(self, password):
        """
        Checks if the password exists in the Have I Been Pwned database.
        Returns the count of how many times it was leaked, or 0 if not found.
        """
        # 1. Hash the password using SHA-1
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        
        # 2. Get the first 5 characters (prefix) and the rest (suffix)
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        # 3. Send only the prefix to the HIBP API (K-Anonymity)
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return {"error": f"Error fetching data: {response.status_code}"}
            
            # 4. Check if our suffix is in the response
            hashes = (line.split(':') for line in response.text.splitlines())
            for h_suffix, count in hashes:
                if h_suffix == suffix:
                    return {"found": True, "count": int(count)}
            
            return {"found": False, "count": 0}
            
        except requests.exceptions.RequestException as e:
            return {"error": f"Connection error: {str(e)}"}

if __name__ == "__main__":
    # Test
    checker = PwnedChecker()
    test_pw = "password123"
    result = checker.check_pwned_status(test_pw)
    print(f"Result for '{test_pw}': {result}")
