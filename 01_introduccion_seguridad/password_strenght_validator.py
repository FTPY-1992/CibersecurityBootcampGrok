def evaluate_password_strength(password: str) -> dict:
    """
    Evaluates the strength of a password and returns a dictionary with:
    - score (0-100)
    - level ('Weak', 'Fair', 'Strong', 'Very Strong')
    - feedback (list of strings with suggestions)
    """
    score = 0
    feedback = []

    # We will add rules one by one here

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