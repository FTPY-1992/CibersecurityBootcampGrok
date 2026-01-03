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
        feedback.append("Strong length! 16+ characters is excellent.")
        score += 40
    else:
        feedback.append("Perfect length (16+ characters) – maximum points for this rule.")
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

    # Determine level based on final score (we'll implement this later)
    if score < 30:
        level = "Weak"
    elif score < 60:
        level = "Fair"
    elif score < 90:
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


if __name__ == "__main__":
    main()