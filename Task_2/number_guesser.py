import random

def get_range():
    """Prompt user to input a valid lower and upper bound for the guessing range."""
    while True:
        try:
            lower = int(input("Enter the LOWER bound of the range: "))
            upper = int(input("Enter the UPPER bound of the range: "))
            if lower >= upper:
                print("Upper bound must be greater than lower bound. Try again.\n")
                continue
            return lower, upper
        except ValueError:
            print("Invalid input. Please enter valid integers.\n")

def get_guess(lower, upper):
    """Prompt user to input a valid guess within the given range."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({lower}-{upper}): "))
            if lower <= guess <= upper:
                return guess
            else:
                print(f"Please enter a number between {lower} and {upper}.\n")
        except ValueError:
            print("Invalid input. Please enter an integer.\n")

def guessing_number():
    print("\n*** Welcome to the Number Guessing Game ***\n")

    # Get custom range from user
    lower, upper = get_range()

    # Generate random number in that range
    secret_number = random.randint(lower, upper)
    attempts = 0

    print(f"\nI have selected a number between {lower} and {upper}.")
    print("Try to guess it!\n")

    # Game loop
    while True:
        guess = get_guess(lower, upper)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} correctly in {attempts} attempts.\n")
            break

# Start the game
if __name__ == "__main__":
    guessing_number()
