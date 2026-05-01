import os
import sys
import datetime
from modules.dictionary_gen import DictionaryGenerator
from modules.hash_extractor import HashExtractor
from modules.cracker import PasswordCracker
from modules.analyzer import PasswordAnalyzer
from modules.reporter import SecurityReporter
from modules.pwned_checker import PwnedChecker


# Colors for Advanced CLI
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = f"""{Colors.CYAN}
    ██████╗ █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
    {Colors.GREEN}    --- Password Cracking & Credential Attack Suite By Vijay Gi V 1.0 ---{Colors.END}
    """
    print(header)

def main_menu():
    print(f"{Colors.CYAN}{'='*65}{Colors.END}")
    print(f"{Colors.YELLOW}1.{Colors.END} Dictionary Generator (Mutation Rules)")
    print(f"{Colors.YELLOW}2.{Colors.END} Hash Identification & Extraction (Demo)")
    print(f"{Colors.YELLOW}3.{Colors.END} Single Hash Cracker (Multi-Threaded)")
    print(f"{Colors.YELLOW}4.{Colors.END} BATCH CRACKING MODE (Process Hash Files)")
    print(f"{Colors.YELLOW}5.{Colors.END} Advanced Password Strength Analyzer")
    print(f"{Colors.YELLOW}6.{Colors.END} Generate Full Security Audit Report")
    print(f"{Colors.YELLOW}7.{Colors.END} Check if Password is LEAKED (HIBP Database)")
    print(f"{Colors.RED}8. Exit{Colors.END}")
    print(f"{Colors.CYAN}{'='*65}{Colors.END}")

def main():
    dict_gen = DictionaryGenerator()
    extractor = HashExtractor()
    cracker = PasswordCracker()
    analyzer = PasswordAnalyzer()
    reporter = SecurityReporter()
    pwned = PwnedChecker()

    
    current_results = {
        'analysis': [],
        'vulnerabilities_count': 0,
        'cracking_results': [],
        'batch_results': []
    }

    while True:
        clear_screen()
        print_header()
        main_menu()
        choice = input(f"{Colors.BOLD}Select an option (1-7): {Colors.END}")

        if choice == '1':
            clear_screen()
            print(f"{Colors.BLUE}--- Dictionary Generator ---{Colors.END}")
            base = input("Enter base words (comma separated): ").split(',')
            base = [b.strip() for b in base]
            custom_name = input("Enter filename (optional): ").strip()
            wordlist = dict_gen.generate_custom(base)
            path = dict_gen.save_to_file(wordlist, filename=custom_name or None)
            print(f"{Colors.GREEN}[+] Generated {len(wordlist)} words. Saved to {path}{Colors.END}")
            input("\nPress Enter to return...")

        elif choice == '2':
            clear_screen()
            print(f"{Colors.BLUE}--- Hash Extraction (Demo) ---{Colors.END}")
            print("1. Identify a hash")
            print("2. Show Windows SAM extraction commands")
            sub_choice = input("Choice: ")
            if sub_choice == '1':
                h = input("Enter hash: ")
                algo = extractor.identify_algorithm(h)
                print(f"{Colors.GREEN}[+] Detected Algorithm: {algo}{Colors.END}")
            elif sub_choice == '2':
                print(f"{Colors.YELLOW}Commands for Offline SAM Extraction:{Colors.END}")
                for cmd in extractor.get_windows_export_commands():
                    print(f"  {Colors.BOLD}{cmd}{Colors.END}")
            input("\nPress Enter to return...")

        elif choice == '3':
            clear_screen()
            print(f"{Colors.BLUE}--- Single Hash Cracker ---{Colors.END}")
            print("1. Dictionary Attack (External Wordlist)")
            print("2. Brute-Force Simulation")
            sub_choice = input("Choice: ")
            
            target_pw = input("Enter password to hash and test: ")
            salt = input("Enter salt (optional): ")
            algo = input("Algorithm (md5/sha1/sha256/sha512): ").lower() or 'sha256'
            threads = int(input("Number of threads (default 4): ") or "4")
            
            target_hash = cracker.hash_password(target_pw, algo, salt)
            print(f"{Colors.YELLOW}[*] Target Hash: {target_hash}{Colors.END}")
            
            if sub_choice == '1':
                path = input("Wordlist path (e.g. reports/wordlist.txt): ")
                if os.path.exists(path):
                    with open(path, 'r', errors='ignore') as f: words = [l.strip() for l in f if l.strip()]
                    res = cracker.dictionary_attack(target_hash, words, algo, salt, threads)
                else: 
                    print(f"{Colors.RED}[!] Wordlist not found.{Colors.END}")
                    input("\nPress Enter to return...")
                    continue
            else:
                max_len = int(input("Max length (default 4): ") or "4")
                res = cracker.brute_force_simulator(target_hash, max_len, algo, salt, threads)
            
            res['hash'] = target_hash
            current_results['cracking_results'].append(res)
            
            if res['success']:
                print(f"{Colors.GREEN}{Colors.BOLD}\n[!] SUCCESS! Password Found: {res['password']}{Colors.END}")
            else:
                print(f"{Colors.RED}\n[!] FAILED to crack password.{Colors.END}")
            input("\nPress Enter to return...")

        elif choice == '4':
            clear_screen()
            print(f"{Colors.BLUE}--- BATCH CRACKING MODE ---{Colors.END}")
            print("Format required: 'username:hash' or one hash per line.")
            file_path = input("Enter path to hash file: ")
            
            if os.path.exists(file_path):
                hash_list = []
                with open(file_path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if not line: continue
                        if ':' in line:
                            user, h = line.split(':', 1)
                            hash_list.append((user, h))
                        else:
                            hash_list.append(("UnknownUser", line))
                
                word_path = input("Enter wordlist path: ")
                if os.path.exists(word_path):
                    with open(word_path, 'r', errors='ignore') as f: 
                        words = [l.strip() for l in f if l.strip()]
                    
                    algo = input("Algorithm (md5/sha1/sha256/sha512): ").lower() or 'sha256'
                    results = cracker.batch_dictionary_attack(hash_list, words, algo)
                    current_results['batch_results'].extend(results)
                    
                    # Saving Batch Results to File
                    save_path = os.path.join("reports", "batch_audit.txt")
                    with open(save_path, "w") as f:
                        f.write(f"Batch Audit Results - {datetime.datetime.now()}\n")
                        f.write("="*50 + "\n")
                        for r in results:
                            status = f"CRACKED ({r['password']})" if r['success'] else "FAILED"
                            f.write(f"User: {r['user']} | Status: {status} | Attempts: {r['attempts']}\n")
                    
                    print(f"\n{Colors.GREEN}[+] Batch processing complete. Saved to {save_path}{Colors.END}")
                else: print(f"{Colors.RED}[!] Wordlist not found.{Colors.END}")
            else: print(f"{Colors.RED}[!] Hash file not found.{Colors.END}")
            input("\nPress Enter to return...")

        elif choice == '5':
            clear_screen()
            print(f"{Colors.BLUE}--- Advanced Strength Analyzer ---{Colors.END}")
            pw = input("Enter password to analyze: ")
            res = analyzer.analyze_strength(pw)
            current_results['analysis'].append(res)
            
            color = Colors.GREEN if res['score'] >= 4 else Colors.YELLOW if res['score'] >= 3 else Colors.RED
            print(f"\n{Colors.BOLD}Security Analysis for:{Colors.END} {pw}")
            print(f"Strength Meter: {res['meter']}")
            print(f"Rating: {color}{res['rating']}{Colors.END}")
            print(f"Entropy: {Colors.CYAN}{res['entropy']} bits{Colors.END}")
            
            comp_status = f"{Colors.GREEN}YES (Strong){Colors.END}" if res['compliant'] else f"{Colors.RED}NO (Weak){Colors.END}"
            print(f"NIST Policy Compliant: {comp_status}")
            
            if res['recommendations']:
                print(f"\n{Colors.BOLD}Recommendations to strengthen:{Colors.END}")
                for rec in res['recommendations']:
                    print(f" {Colors.YELLOW}• {rec}{Colors.END}")
            
            if not res['compliant']:
                current_results['vulnerabilities_count'] += 1
            input("\nPress Enter to return...")

        elif choice == '6':
            clear_screen()
            print(f"{Colors.BLUE}--- Generating Full Audit Report ---{Colors.END}")
            path = reporter.generate_report(current_results)
            print(f"{Colors.GREEN}[+] Final Report generated successfully: {path}{Colors.END}")
            input("\nPress Enter to return...")

        elif choice == '7':
            clear_screen()
            print(f"{Colors.BLUE}--- Real-World Leak Checker (HIBP) ---{Colors.END}")
            pw = input("Enter password to check: ")
            print(f"{Colors.YELLOW}[*] Checking HIBP database...{Colors.END}")
            res = pwned.check_pwned_status(pw)
            
            if "error" in res:
                print(f"{Colors.RED}[!] {res['error']}{Colors.END}")
            elif res['found']:
                print(f"{Colors.RED}{Colors.BOLD}[!!!] SECURITY ALERT: This password was found in {res['count']} data breaches!{Colors.END}")
                print(f"{Colors.YELLOW}Recommendation: Never use this password again.{Colors.END}")
            else:
                print(f"{Colors.GREEN}[+] Good news! This password was not found in any known public data breaches.{Colors.END}")
            
            input("\nPress Enter to return...")

        elif choice == '8':
            print(f"{Colors.BOLD}{Colors.YELLOW}Exiting. Stay secure!{Colors.END}")
            break
        else:
            print(f"{Colors.RED}[!] Invalid choice. Please try again.{Colors.END}")
            input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
