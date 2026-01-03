def evaluate_password_strength(password: str) -> dict:
    """
    Evaluates the strength of a password and returns a dictionary with:
    - score (0-100)
    - level ('Weak', 'Fair', 'Strong', 'Very Strong')
    - feedback (list of strings with suggestions)
    """
    score = 0
    feedback = []
    length = len(password)
    #Rule 1: LENGTH - most important factor
    if length < 8:
        feedback.append("Password is too short: use at least 8 characters.")
    elif length < 12:
        feedback.append("Good start, but consider using 12+ characters for better security.")
        score += 20
    elif length < 16:
        score += 40
    else:
        score += 60
    # Rule 2: Uppercase letters
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 10
    else:
        feedback.append("Add at least one uppercase letter (A-Z) to increase strength.")
    # Rule 3: Lowercase letters
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 10
    else:
        feedback.append("Add at least one lowercase letter (a-z) to increase strength.")

    if has_upper and not has_lower:
        feedback.append("Avoid using only uppercase letters – mix cases for better resistance against attacks.")
    if not has_upper and has_lower:
        feedback.append("Avoid using only lowercase letters – mix cases for better resistance against attacks.")
    #Rule 4 -Digits (0-9)
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 15
    else:
        feedback.append("Include at least one digit (0-9) to strengthen the password.")
    # Bonus educational feedback: digits grouped at start or end (common weak patterns)
    if has_digit:
        # Digits only at the end
        stripped_end = password.rstrip('0123456789')
        if len(password) > len(stripped_end) and not any(c.isdigit() for c in stripped_end):
            feedback.append("Avoid placing all numbers at the end – distribute them throughout the password.")

        # Digits only at the start
        stripped_start = password.lstrip('0123456789')
        if len(password) > len(stripped_start) and not any(c.isdigit() for c in stripped_start):
            feedback.append("Avoid placing all numbers at the beginning – distribute them throughout the password.")
    # Rule 5: Special characters (symbols)
    has_symbol = False
    # Raw string: safe, legible, includes backslash literally
    symbols = r'!@#$%^&*()-_=+[]{}|;:\'",.<>?/`~' #OJO! sin esta forma, problemas asegurados por la barra invertida!
    for char in password:
        if char in symbols:
            has_symbol = True
            break

    if has_symbol:
        score += 25
    else:
        feedback.append("Include at least one special character (e.g. !@#$%^&*) for maximum strength.")
    #Cap score al 100 to avoid exceeding maximun
    score = min(score, 100)
    # Calculate final strength level based on total score
    if score < 30:
        level = "Weak"
    elif score < 60:
        level = "Fair"
    elif score < 85:
        level = "Strong"
    else:
        level = "Very Strong"

    return {
        "score": score,
        "level": level,
        "feedback": feedback
    }


def main():
    password = input("Enter a password to evaluate: ").strip()

    if not password:
        print("Error: Password cannot be empty.")
        return

    result = evaluate_password_strength(password)

    print(f"\nScore: {result['score']}/100")
    print(f"Strength level: {result['level']}")

    if result['feedback']:
        print("\nSuggestions to improve it:")
        for msg in result['feedback']:
            print(f"  - {msg}")
    else:
        print("\nCongratulations! Your password is very strong and follows best practices.")
        print("Remember: never reuse it and keep it secret.")


if __name__ == "__main__":
    main()