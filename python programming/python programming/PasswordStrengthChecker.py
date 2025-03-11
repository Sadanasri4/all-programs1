import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.length = len(password)
        self.has_upper = bool(re.search(r'[A-Z]', password))
        self.has_lower = bool(re.search(r'[a-z]', password))
        self.has_digit = bool(re.search(r'\d', password))
        self.has_special = bool(re.search(r'[\W_]', password))
        self.unique_chars = len(set(password))

    def evaluate_strength(self):
        # Criteria for strength
        length_criteria = self.length >= 12
        upper_criteria = self.has_upper
        lower_criteria = self.has_lower
        digit_criteria = self.has_digit
        special_criteria = self.has_special
        uniqueness_criteria = self.unique_chars > self.length // 2

        # Calculate strength score
        score = sum([
            length_criteria,
            upper_criteria,
            lower_criteria,
            digit_criteria,
            special_criteria,
            uniqueness_criteria
        ])

        # Define strength levels
        strength_levels = {
            0: "Very Weak",
            1: "Very Weak",
            2: "Weak",
            3: "Moderate",
            4: "Strong",
            5: "Very Strong",
            6: "Excellent"
        }

        strength = strength_levels[score]

        # Provide feedback
        feedback = []
        if not length_criteria:
            feedback.append("Password should be at least 12 characters long.")
        if not upper_criteria:
            feedback.append("Password should contain at least one uppercase letter.")
        if not lower_criteria:
            feedback.append("Password should contain at least one lowercase letter.")
        if not digit_criteria:
            feedback.append("Password should contain at least one digit.")
        if not special_criteria:
            feedback.append("Password should contain at least one special character.")
        if not uniqueness_criteria:
            feedback.append("Password should have more unique characters.")

        return {
            "password": self.password,
            "strength": strength,
            "feedback": feedback
        }

# Example usage
def main():
    password = input("Enter a password to check its strength: ")
    checker = PasswordStrengthChecker(password)
    result = checker.evaluate_strength()
    print(f"Password: {result['password']}")
    print(f"Strength: {result['strength']}")
    print("Feedback:")
    for fb in result['feedback']:
        print(f"- {fb}")

if __name__ == "__main__":
    main()

