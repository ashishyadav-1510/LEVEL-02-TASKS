import re

def check_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password.
    Parameters:
        password (str): The password to evaluate.
    Returns:
        str: Strength level - Weak, Moderate, or Strong.
    """
    # Define regular expressions
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    is_long_enough = len(password) >= 8

    # Score the password
    score = sum([has_upper, has_lower, has_digit, has_special, is_long_enough])

    # Determine strength level
    if score == 5:
        return "Strong Password"
    elif 3 <= score < 5:
        return "Moderate Password - Consider making it stronger."
    else:
        return "Weak Password- Too easy to guess."

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ").strip()
    
    strength = check_password_strength(password)
    print("\nStrength:", strength)

if __name__ == "__main__":
    main()
