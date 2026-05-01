import itertools
import os

class DictionaryGenerator:
    def __init__(self):
        self.leet_map = {
            'a': ['a', '4', '@'],
            'e': ['e', '3'],
            'i': ['i', '1', '!'],
            'o': ['o', '0'],
            's': ['s', '5', '$'],
            't': ['t', '7'],
            'b': ['b', '8']
        }

    def generate_custom(self, base_words, include_numbers=True, include_special=True):
        """Generates a wordlist with advanced mutation rules."""
        wordlist = set()
        numbers = ['123', '1234', '1111', '2023', '2024', '1'] if include_numbers else ['']
        specials = ['!', '@', '#', '$', ''] if include_special else ['']

        for word in base_words:
            word = word.strip()
            variations = [word, word.capitalize(), word.upper(), word.lower()]
            
            for v in variations:
                wordlist.add(v)
                # Suffixes
                for num in numbers:
                    for spec in specials:
                        wordlist.add(f"{v}{num}{spec}")
                        wordlist.add(f"{v}{spec}{num}")
                
                # Prefixes (Advanced)
                for num in numbers:
                    wordlist.add(f"{num}{v}")
                
                # Leet-speak integration (Subtle)
                leet_v = v.replace('a', '@').replace('e', '3').replace('i', '1').replace('o', '0')
                wordlist.add(leet_v)

        return list(wordlist)

    def apply_leet(self, word):
        """Applies leet-speak mutations to a single word."""
        options = []
        for char in word.lower():
            if char in self.leet_map:
                options.append(self.leet_map[char])
            else:
                options.append([char])
        
        return ["".join(item) for item in itertools.product(*options)]

    def save_to_file(self, wordlist, filename=None):
        """Saves wordlist to a file with a unique name if none provided."""
        import datetime
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"wordlist_{timestamp}.txt"
        
        filepath = os.path.join("reports", filename)
        with open(filepath, "w") as f:
            for word in wordlist:
                f.write(word + "\n")
        return filepath

if __name__ == "__main__":
    gen = DictionaryGenerator()
    words = ["admin", "password", "guest"]
    custom_list = gen.generate_custom(words)
    print(f"Generated {len(custom_list)} words.")
    path = gen.save_to_file(custom_list)
    print(f"Saved to {path}")
