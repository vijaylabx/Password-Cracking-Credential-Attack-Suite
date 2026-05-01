import datetime
import os
import matplotlib.pyplot as plt

class SecurityReporter:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def generate_report(self, results, report_name="security_audit.txt"):
        # 1. Generate the visual chart first
        chart_path = self.generate_visual_summary(results)
        
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
            f.write(f"Vulnerable Passwords Found: {results.get('vulnerabilities_count', 0)}\n")
            if chart_path:
                f.write(f"Visual Chart Generated: {chart_path}\n\n")
            else:
                f.write("\n")
            
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

    def generate_visual_summary(self, results):
        """Generates a pie chart of password strength ratings."""
        analysis = results.get('analysis', [])
        if not analysis:
            return None
            
        ratings = [item['rating'] for item in analysis]
        rating_counts = {}
        for r in ratings:
            rating_counts[r] = rating_counts.get(r, 0) + 1
            
        labels = list(rating_counts.keys())
        sizes = list(rating_counts.values())
        
        # Define professional colors
        colors_map = {
            'Very Strong': '#2ecc71',
            'Strong': '#27ae60',
            'Medium': '#f1c40f',
            'Weak': '#e67e22',
            'Very Weak': '#e74c3c'
        }
        colors = [colors_map.get(label, '#3498db') for label in labels]
        
        plt.figure(figsize=(10, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, shadow=True)
        plt.title('Password Strength Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        chart_path = os.path.join(self.output_dir, "audit_visuals.png")
        plt.savefig(chart_path)
        plt.close()
        return chart_path
