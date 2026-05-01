import hashlib
import time
import itertools
import string
from concurrent.futures import ThreadPoolExecutor

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

class PasswordCracker:
    def __init__(self):
        self.supported_hashes = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }

    def hash_password(self, password, algorithm='sha256', salt=''):
        if algorithm not in self.supported_hashes:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        # Supporting basic salt prepending
        data = salt + password
        return self.supported_hashes[algorithm](data.encode()).hexdigest()

    def _check_password(self, word, target_hash, algorithm, salt):
        if self.hash_password(word, algorithm, salt) == target_hash:
            return word
        return None

    def dictionary_attack(self, target_hash, wordlist, algorithm='sha256', salt='', threads=4):
        """Performs a multi-threaded dictionary attack with progress reporting."""
        start_time = time.time()
        attempts = 0
        total = len(wordlist)
        
        print(f"[*] Starting dictionary attack ({total} words) with {threads} threads...")
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            chunk_size = 2000
            for i in range(0, total, chunk_size):
                chunk = wordlist[i:i+chunk_size]
                futures = [executor.submit(self._check_password, word, target_hash, algorithm, salt) for word in chunk]
                
                for future in futures:
                    attempts += 1
                    result = future.result()
                    if result:
                        duration = time.time() - start_time
                        return {
                            "success": True,
                            "password": result,
                            "attempts": attempts,
                            "time_taken": duration
                        }
                
                # Simple Progress Bar logic
                if attempts % 10000 == 0 or attempts == total:
                    percent = (attempts / total) * 100
                    print(f"\r[*] Progress: {percent:.1f}% ({attempts}/{total} attempts)", end="")
        
        print("\n")
        duration = time.time() - start_time
        return {
            "success": False,
            "attempts": attempts,
            "time_taken": duration
        }

    def batch_dictionary_attack(self, hash_list, wordlist, algorithm='sha256', threads=4):
        """Processes a list of (user, hash) pairs and attempts to crack them."""
        results = []
        total_hashes = len(hash_list)
        print(f"[*] Starting batch attack on {total_hashes} hashes...")
        
        for user, target_hash in hash_list:
            print(f"[*] Cracking {user}...")
            res = self.dictionary_attack(target_hash, wordlist, algorithm, threads=threads)
            res['user'] = user
            res['hash'] = target_hash
            results.append(res)
            if res['success']:
                print(f"  {Colors.GREEN}[!] CRACKED: {user} -> {res['password']}{Colors.END}")
        
        return results

    def brute_force_simulator(self, target_hash, max_length=4, algorithm='sha256', salt='', threads=4):
        """Performs a multi-threaded brute-force attack."""
        chars = string.ascii_lowercase + string.digits
        start_time = time.time()
        attempts = 0

        print(f"[*] Starting brute-force simulation (max length: {max_length})...")

        for length in range(1, max_length + 1):
            guesses = ("".join(g) for g in itertools.product(chars, repeat=length))
            
            with ThreadPoolExecutor(max_workers=threads) as executor:
                # We consume the generator in chunks
                while True:
                    chunk = list(itertools.islice(guesses, 5000))
                    if not chunk:
                        break
                    
                    attempts += len(chunk)
                    futures = [executor.submit(self._check_password, word, target_hash, algorithm, salt) for word in chunk]
                    
                    for future in futures:
                        result = future.result()
                        if result:
                            duration = time.time() - start_time
                            return {
                                "success": True,
                                "password": result,
                                "attempts": attempts,
                                "time_taken": duration
                            }
        
        duration = time.time() - start_time
        return {
            "success": False,
            "attempts": attempts,
            "time_taken": duration
        }

    def estimate_crack_time(self, password_length, charset_size, speed_hps=1000000):
        """Estimates time to crack based on charset size and hash speed."""
        combinations = charset_size ** password_length
        seconds = combinations / speed_hps
        
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.2f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.2f} hours"
        else:
            return f"{seconds/86400:.2f} days"

if __name__ == "__main__":
    cracker = PasswordCracker()
    pw = "abc1"
    target = cracker.hash_password(pw, 'md5')
    print(f"Target Hash (MD5): {target}")
    
    print("Running Brute Force Simulation...")
    result = cracker.brute_force_simulator(target, max_length=4, algorithm='md5')
    print(result)
