import math
import re

class PasswordAnalyzer:
    def __init__(self):
        pass

    def calculate_entropy(self, password):
        """Calculates the Shannon entropy of a password."""
        if not password:
            return 0
        
        charset_size = 0
        if re.search(r'[a-z]', password): charset_size += 26
        if re.search(r'[A-Z]', password): charset_size += 26
        if re.search(r'[0-9]', password): charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', password): charset_size += 32
        
        if charset_size == 0: return 0
        
        entropy = len(password) * math.log2(charset_size)
        return entropy

    def get_visual_meter(self, score):
        """Returns an ASCII progress bar representing password strength."""
        blocks = ["░", "▒", "▓", "█"]
        meter = ""
        for i in range(1, 6):
            if i <= score:
                meter += "█"
            else:
                meter += "░"
        
        colors = ['\033[91m', '\033[93m', '\033[93m', '\033[92m', '\033[92m']
        return f"{colors[score-1 if score > 0 else 0]}{meter} ({score}/5)\033[0m"

    def analyze_strength(self, password):
        """Analyzes password strength and returns a detailed report."""
        entropy = self.calculate_entropy(password)
        length = len(password)
        
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'[0-9]', password))
        has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
        
        score = 0
        if length >= 8: score += 1
        if length >= 12: score += 1
        if has_upper and has_lower: score += 1
        if has_digit: score += 1
        if has_special: score += 1
        
        rating = "Critical/Very Weak"
        if score == 5: rating = "Excellent/Strong"
        elif score >= 4: rating = "Good/Strong"
        elif score >= 3: rating = "Medium"
        elif score >= 1: rating = "Weak"
        
        recommendations = []
        if length < 12: recommendations.append("Length is too short (aim for 12+)")
        if not has_upper: recommendations.append("Missing uppercase letters")
        if not has_special: recommendations.append("Missing special characters (!, @, #, etc.)")
        if not has_digit: recommendations.append("Missing numbers")

        return {
            "password": password,
            "length": length,
            "entropy": round(entropy, 2),
            "score": score,
            "meter": self.get_visual_meter(score),
            "rating": rating,
            "recommendations": recommendations,
            "compliant": score >= 4 # NIST compliance simulation
        }

if __name__ == "__main__":
    analyzer = PasswordAnalyzer()
    test_pws = ["123456", "Password123", "Complex!@#2024"]
    for p in test_pws:
        print(f"\nAnalysis for: {p}")
        print(analyzer.analyze_strength(p))
