import re

def check_password_strength(password):
    strength_criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'[0-9]', password)),
        'special_characters': bool(re.search(r'[\W_]', password))
    }

    strength_score = sum(strength_criteria.values())

    if strength_score == 5:
        return "Strong"
    elif strength_score >= 3:
        return "Moderate"
    else:
        return "Weak"

def provide_feedback(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should include at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should include at least one number.")
    if not re.search(r'[\W_]', password):
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    if not feedback:
        feedback.append("Your password is strong!")
    
    return feedback

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    feedback = provide_feedback(password)

    print(f"Password Strength: {strength}")
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")

if __name__ == "__main__":
    main()
