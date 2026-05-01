import datetime
import os

class SecurityReporter:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_report(self, results, report_name="security_audit.txt"):
        filepath = os.path.join(self.output_dir, report_name)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(filepath, "w") as f:
            f.write("="*50 + "\n")
            f.write(f" PASSWORD SECURITY AUDIT REPORT\n")
            f.write(f" Generated on: {timestamp}\n")
            f.write("="*50 + "\n\n")
            
            f.write("1. SUMMARY OF FINDINGS\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total Passwords Analyzed: {len(results.get('analysis', []))}\n")
            f.write(f"Vulnerable Passwords Found: {results.get('vulnerabilities_count', 0)}\n\n")
            
            f.write("2. DETAILED ANALYSIS\n")
            f.write("-" * 20 + "\n")
            for item in results.get('analysis', []):
                f.write(f"Password: {item['password']}\n")
                f.write(f"  Rating: {item['rating']}\n")
                f.write(f"  Entropy: {item['entropy']} bits\n")
                if item['recommendations']:
                    f.write(f"  Fixes: {', '.join(item['recommendations'])}\n")
                f.write("\n")
            
            if 'cracking_results' in results:
                f.write("3. CRACKING SIMULATION RESULTS\n")
                f.write("-" * 30 + "\n")
                for crack in results['cracking_results']:
                    status = "SUCCESS" if crack['success'] else "FAILED"
                    f.write(f"Target Hash: {crack['hash']}\n")
                    f.write(f"  Status: {status}\n")
                    if crack['success']:
                        f.write(f"  Cracked Password: {crack['password']}\n")
                    f.write(f"  Time Taken: {crack['time_taken']:.4f} seconds\n")
                    f.write(f"  Total Attempts: {crack['attempts']}\n\n")
            
            f.write("4. MITIGATION STRATEGIES\n")
            f.write("-" * 20 + "\n")
            f.write("- Implement Multi-Factor Authentication (MFA).\n")
            f.write("- Enforce a minimum length of 14 characters.\n")
            f.write("- Use modern hashing algorithms (e.g., Argon2 or SHA-512 with salts).\n")
            f.write("- Regularly audit credentials for common dictionary words.\n")
            
        return filepath
