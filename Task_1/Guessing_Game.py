import random 

def guessing_number():
    n = random.randint(1, 100) 
    guesses = 0

    print("\n*** Number Guessing Game ***")
    print("I have selected  number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            guesses += 1
            if user_guess<1 or user_guess >100:
                print("Please enter a number between 1 and 100.")
                continue
            if user_guess < n:
                print("Your Guess is Lower than My Guess! Try again.")
            elif user_guess > n:
                print("Your Guess is Higher than My Guess! Try again.")
            else:
                print(f"Congratulations You guessed the number {n} correctly in {guesses} guesses.")
                break
        except ValueError:
            print("Something Wrong!!,Enter an Integer Number")
            
guessing_number()