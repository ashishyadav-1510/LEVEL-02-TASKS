# Task - 1 : Guessing Game

This is a simple **Python console game** where the computer randomly selects a number between 1 and 100, and the player tries to guess it. The program provides feedback on each guess until the correct number is found.

## Features

- Random number generation between 1 and 100
- Validates user input (must be an integer within range)
- Provides hints if the guess is too high or too low
- Tracks the number of attempts
- Handles invalid inputs gracefully

## How to Run

1. Make sure you have **Python installed** on your system.
2. Save the code below into a Python file, e.g., `guessing_game.py`.
3. Open terminal or command prompt in the directory where the file is saved.
4. Run the script using the command:
   python guessing_game.py

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_1/Screenshot%202025-07-18%20192610.png?raw=true)
### Output:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_1/Screenshot%202025-07-18%20192638.png?raw=true)

## Video

[Video](https://youtu.be/bi8XUovUugk)

## Explanation

import random
This imports Python's built-in random module, which allows us to generate random numbers.

def guessing_number():
Defines a function named guessing_number() that contains the entire game logic.

    n = random.randint(1, 100)
Generates a random integer between 1 and 100 (both inclusive) and stores it in the variable n.
This is the number the player has to guess.

    guesses = 0
Initializes a counter variable guesses to track the number of attempts the user makes.

    print("\n*** Number Guessing Game ***")
    print("I have selected  number between 1 and 100.")
    print("Can you guess what it is?")
These three lines print a welcome message and instructions for the player.

    while True:
Starts an infinite loop. This loop continues until the player guesses the number correctly and breaks the loop.

        try:
Begins a try block to handle exceptions, especially if the user enters non-integer input.

            user_guess = int(input("Enter your guess: "))
Takes input from the user, converts it to an integer, and stores it in user_guess.
If the input is not an integer, a ValueError will be raised and caught by the except block.

            guesses += 1
Increments the guesses counter by 1 every time the user inputs a guess.

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
Checks if the guess is outside the valid range (1–100).
If so, it prints a warning and uses continue to restart the loop without further checking.

            if user_guess < n:
                print("Your Guess is Lower than My Guess! Try again.")
If the guess is less than the correct number, a hint is printed.

            elif user_guess > n:
                print("Your Guess is Higher than My Guess! Try again.")
If the guess is greater than the correct number, another hint is printed.

            else:
                print(f"Congratulations You guessed the number {n} correctly in {guesses} guesses.")
                break
If the guess matches the correct number:
A congratulations message is displayed.
The loop is terminated using break.

        except ValueError:
            print("Something Wrong!!,Enter an Integer Number")
This except block catches any input that cannot be converted to an integer, such as strings or symbols.
It prints an error message and loops back for another input.

guessing_number()
This is a function call that starts the game by calling the guessing_number() function.


# Task - 2 : Number Guesser

A **fun Python-based terminal game** where the player sets their own number range, and the computer randomly selects a secret number from that range. The player then tries to guess the number with helpful hints and input validation.

## Features

- Customizable number range
- Intelligent input validation for range and guesses
- Hints provided: "Too low", "Too high"
- Unlimited guessing attempts
- Tracks total number of attempts
- Clean modular code with functions
- Handles invalid input gracefully

## How to Run the Game

1. **Install Python** if it's not already installed (Python 3 recommended).
2. **Download or copy** the `guessing_game.py` script.
3. Open a terminal or command prompt.
4. Navigate to the script's folder using `cd`.
5. Run the game with:

python guessing_game.py

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_2/Screenshot%202025-07-18%20192805.png?raw=true)
### Output:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_2/Screenshot%202025-07-18%20192900.png?raw=true)

## Video

[Video](https://youtu.be/eRdsiq1FfbE)

## Explanation

import random
Imports the built-in random module to allow the program to generate a random number.

def get_range():
    """Prompt user to input a valid lower and upper bound for the guessing range."""
Defines a function called get_range() with a docstring describing its purpose.

    while True:
Starts an infinite loop to repeatedly prompt the user until valid input is given.

        try:
Begins a try block to catch any invalid (non-integer) inputs from the user.

            lower = int(input("Enter the LOWER bound of the range: "))
            upper = int(input("Enter the UPPER bound of the range: "))
Takes two integer inputs from the user for the lower and upper bounds of the guessing range.

            if lower >= upper:
                print("Upper bound must be greater than lower bound. Try again.\n")
                continue
Checks whether the upper bound is greater than the lower bound.
If not, displays an error and restarts the loop.

            return lower, upper
If the range is valid, returns the two values to the caller.

        except ValueError:
            print("Invalid input. Please enter valid integers.\n")
Handles non-integer inputs by displaying an error message and restarting the loop.

def get_guess(lower, upper):
    """Prompt user to input a valid guess within the given range."""
Defines another function get_guess() that takes the lower and upper bounds as parameters.
The function ensures the guess is a valid integer within the specified range.

    while True:
Starts a loop to repeatedly prompt the user until a valid guess is provided.

        try:
            guess = int(input(f"Enter your guess ({lower}-{upper}): "))
Prompts the user for an integer guess and converts the input to int.

            if lower <= guess <= upper:
                return guess
If the guess is within the valid range, it is returned to the calling function.

            else:
                print(f"Please enter a number between {lower} and {upper}.\n")
If the guess is outside the range, it gives an error and loops again.

        except ValueError:
            print("Invalid input. Please enter an integer.\n")
Catches non-integer inputs and asks the user to try again.

def guessing_number():
Defines the main game function called guessing_number().

    print("\n*** Welcome to the Number Guessing Game ***\n")
Displays a welcome message.

    lower, upper = get_range()
Calls the get_range() function to get the valid lower and upper bounds from the user.

    secret_number = random.randint(lower, upper)
Generates a random integer between lower and upper using random.randint().

    attempts = 0
Initializes a counter variable to keep track of the number of guesses.

    print(f"\nI have selected a number between {lower} and {upper}.")
    print("Try to guess it!\n")
Informs the player that the number has been selected and starts the guessing phase.

    while True:
Starts the main game loop, which continues until the correct number is guessed.

        guess = get_guess(lower, upper)
Calls the get_guess() function to get a valid guess from the user.

        attempts += 1
Increments the attempts counter by 1 for each guess.

        if guess < secret_number:
            print("Too low! Try again.\n")
If the guessed number is less than the secret number, the user is told it's too low.

        elif guess > secret_number:
            print("Too high! Try again.\n")
If the guessed number is greater than the secret number, the user is told it's too high.

        else:
            print(f"\nCongratulations! You guessed the number {secret_number} correctly in {attempts} attempts.\n")
            break
If the guess matches the secret number:
A congratulations message is displayed.
The game ends using break.

if __name__ == "__main__":
    guessing_number()
This ensures that the guessing_number() function runs only when the script is executed directly, not when imported as a module.


# Task - 3 : Password Strength Checker

A simple and effective Python script that checks the strength of a password based on multiple criteria including length, uppercase letters, lowercase letters, digits, and special characters.

## Features

- Evaluates password strength as **Weak**, **Moderate**, or **Strong**
- Uses **regular expressions** for accurate pattern matching
- Validates the presence of:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Digits (0–9)
  - Special characters (e.g. !@#$%^&*())
  - Minimum length (8 characters)
- Clean function-based structure

## How to Run

1. Make sure **Python 3** is installed on your system.
2. Save the script as `password_checker.py`.
3. Open a terminal or command prompt in the script directory.
4. Run the script using:
python password_checker.py

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_3/Screenshot%202025-07-18%20193006.png?raw=true)
### Output:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_3/Screenshot%202025-07-18%20193054.png?raw=true)

## Video

[Video](https://youtu.be/bgmxjiHLN4A)

## Explanation
import re
Imports the re module (regular expressions) to perform pattern matching for uppercase, lowercase, digits, and special characters.

def check_password_strength(password: str) -> str:
Defines a function named check_password_strength that takes one argument: password (a string) and returns a string representing the strength.

    """
    Evaluates the strength of a password.
    Parameters:
        password (str): The password to evaluate.
    Returns:
        str: Strength level - Weak, Moderate, or Strong.
    """
This is a docstring that explains what the function does, its parameter, and what it returns.

Regex Conditions:

    has_upper = bool(re.search(r"[A-Z]", password))
Checks if the password contains at least one uppercase letter.
re.search(r"[A-Z]", password) returns a match object if any capital letter is found.
bool(...) converts it to True or False.

    has_lower = bool(re.search(r"[a-z]", password))
Checks if the password contains at least one lowercase letter using regex pattern [a-z].

    has_digit = bool(re.search(r"\d", password))
Checks for at least one digit in the password using \d (which means digit in regex).

    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
Checks for special characters in the password.
The pattern matches common special characters like !@#$%^&*()....

    is_long_enough = len(password) >= 8
Checks if the password length is at least 8 characters.

Password Scoring:

    score = sum([has_upper, has_lower, has_digit, has_special, is_long_enough])
Adds up the True values from the above 5 checks.
Since True is treated as 1 in Python, the total score will be between 0 and 5.

Determine Strength Level:

    if score == 5:
        return "Strong Password"
If all 5 checks pass, the password is Strong.

    elif 3 <= score < 5:
        return "Moderate Password - Consider making it stronger."
If 3 or 4 checks pass, the password is considered Moderate.

    else:
        return "Weak Password- Too easy to guess."
If less than 3 checks pass, the password is Weak and not secure enough.

Main Function

def main():
Defines the main() function which handles user interaction.

    print("Password Strength Checker")
Prints a heading to the console.

    password = input("Enter your password: ").strip()
Prompts the user to enter a password.
.strip() removes any leading or trailing whitespace.

    strength = check_password_strength(password)
Calls the check_password_strength() function and stores the result in strength.

    print("\nStrength:", strength)
Prints the evaluated strength of the password.

Script Execution Entry Point

if __name__ == "__main__":
    main()
Ensures that the main() function runs only if the script is executed directly (not imported).
This is standard Python practice for scripts.


# Task - 4 : Fibonacci Sequence

A simple Python program that generates the **Fibonacci sequence** up to a user-specified number of terms. The program includes input validation and clean output formatting.

## Features

- Generates Fibonacci sequence for **any positive integer**
- Includes input validation and error handling
- Clean, modular code with functions
- Displays the entire sequence as a list
- Returns accurate results based on standard Fibonacci definition

## How to Run the Program

1. Ensure you have **Python 3** installed on your system.
2. Save the code to a file named `fibonacci_generator.py`.
3. Open your terminal (or command prompt), navigate to the script directory, and run:
python fibonacci_generator.py

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_4/Screenshot%202025-07-18%20193145.png?raw=true)
### Output:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_4/Screenshot%202025-07-18%20193201.png?raw=true)

## Video

[Video](https://youtu.be/NjsCzF_G8oM)

## Explanation

Function to Generate Fibonacci Sequence

def generate_fibonacci(n: int) -> list:
Defines a function generate_fibonacci that takes an integer n and returns a list.

The -> list is a type hint, meaning the function will return a list of integers.

    """
    Generates the Fibonacci sequence up to n terms.
    Parameters:
        n (int): Number of terms to generate.
    Returns:
        list: Fibonacci sequence as a list of integers.
    """
This is a docstring, which explains what the function does, the input parameter, and the return type.

    if n <= 0:
        return []
Checks if the user entered 0 or negative.

If so, returns an empty list because no Fibonacci terms are needed.

    elif n == 1:
        return [0]
If the user wants only 1 term, it returns [0].

    fib = [0, 1]
Initializes the Fibonacci sequence list with the first two numbers: 0 and 1.

    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
Loops from the 3rd term to the nth term.
fib[-1] is the last element, fib[-2] is the second last.
Appends the sum of the last two elements to the list (next = prev1 + prev2).

    return fib
Returns the complete list once the loop is done.

Main Function for Input and Display

def main():
Defines the main function which handles input/output.

    print("Fibonacci Sequence Generator")
Prints the heading to the console.

    while True:
        try:
            num = int(input("Enter the number of terms (positive integer): "))
Enters an infinite loop to keep prompting the user until they enter valid input.
input() takes user input, int() tries to convert it into an integer.
If conversion fails, it will jump to except.

            if num < 0:
                print("Please enter a non-negative integer.\n")
                continue
Checks if the number is negative.
If so, prints an error and continues the loop to re-prompt.

            break
If input is valid and non-negative, it breaks out of the loop.

        except ValueError:
            print("Invalid input. Please enter an integer.\n")
If input isn’t an integer (e.g., a string like "abc"), it catches the error and prints a message.

    sequence = generate_fibonacci(num)
Calls the previously defined function and stores the result in sequence.

    print(f"\nFibonacci sequence with {num} term(s):")
    print(sequence)
Prints the result using f-string formatting.
Outputs the Fibonacci sequence list.

✅ Entry Point of the Program

if __name__ == "__main__":
    main()
Ensures that the main() function runs only when the file is executed directly.
Prevents the main function from running if this file is imported as a module in another script.


# Task - 5 : File Manipulation

This Python project reads a **generated sample text file**, cleans and tokenizes its content, counts the frequency of each word, and displays the results in **alphabetical order**.

## Features

- Automatically creates and writes to a text file.
- Cleans punctuation and converts words to lowercase.
- Uses `regex` for accurate word tokenization.
- Counts frequency using `collections.defaultdict`.
- Displays word count results in a clean, formatted way.

## How It Works

1. **`create_sample_file()`**  
   - Creates a text file named `sample.txt` and writes sample content.

2. **`clean_and_tokenize()`**  
   - Removes punctuation and converts all words to lowercase using regular expressions.

3. **`count_words()`**  
   - Opens the file, reads line by line, tokenizes each word, and counts occurrences.

4. **`display_word_counts()`**  
   - Prints the word frequencies in alphabetical order in a formatted table.

5. **`main()`**  
   - Driver function that orchestrates file creation, word counting, and display.

## Sample Output

Auto Word Counter from Generated File
File 'sample.txt' created with sample content.
Word Frequencies (Alphabetical Order):

acknowledge     : 1
am              : 1
are             : 1
chief           : 1
file            : 1
files           : 1
fun             : 1
hello           : 3
i               : 1
in              : 1
is              : 2
me              : 1
output          : 1
python          : 3
sample          : 1
text            : 2
the             : 1
this            : 1
tribal          : 1
used            : 1
world           : 2

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_5/Screenshot%202025-07-18%20193356.png?raw=true)
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_5/Screenshot%202025-07-18%20193404.png?raw=true)
### Output:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_5/Screenshot%202025-07-18%20193734.png?raw=true)
### Sample Text File:
![image](https://github.com/ashishyadav-1510/LEVEL-02-TASKS/blob/main/Task_5/Screenshot%202025-07-18%20193742.png?raw=true)

## Video

[Video](https://youtu.be/cRXFCcuxmyk)

## Explanation

import re
from collections import defaultdict
import re: Imports the regular expression module to perform advanced string pattern matching.
from collections import defaultdict: Imports defaultdict, a dictionary that provides a default value for missing keys (so we don't need to check if a key exists before incrementing it).

Function: create_sample_file

def create_sample_file(filename: str):
Defines a function that takes a filename as a string.

    """
    Creates a sample text file and writes predefined content to it.
    """
Docstring describing what the function does.

    content = (
        "Hello world! This is a sample text file.\n"
        "Python is fun. Hello Python, hello world.\n"
        "Text files are used for input and output in Python.\n"
        "Acknowledge Me I am the Tribal Chief."
    )
Defines the content to be written to the file. Uses multi-line string formatting for readability.

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
Opens (or creates) a file with write mode 'w' and UTF-8 encoding, then writes the content to it.

    print(f"File '{filename}' created with sample content.\n")
Prints confirmation that the file was created.

Function: clean_and_tokenize

def clean_and_tokenize(line: str) -> list:
Function to clean a line and tokenize it into a list of lowercase words.

    """
    Cleans a line by removing punctuation and splitting into lowercase words.
    """
Docstring explaining the function.

    return re.findall(r'\b\w+\b', line.lower())
Converts line to lowercase.
Uses regex \b\w+\b to find all words (sequences of alphanumeric characters bounded by word boundaries).
Returns a list of words.

Function: count_words

def count_words(filename: str) -> dict:
Reads the file and counts each word's frequency.

    """
    Reads a file and counts the occurrences of each word.
    """
Docstring.

    word_counts = defaultdict(int)
Initializes a defaultdict where every new key defaults to 0.

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = clean_and_tokenize(line)
                for word in words:
                    word_counts[word] += 1
Tries to open the file in read mode.
Iterates through each line in the file.
Tokenizes the line into words using the clean_and_tokenize() function.
Increments the count of each word in word_counts.

        return dict(sorted(word_counts.items()))
Sorts the dictionary alphabetically by word and converts it back to a normal dict.

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
If the file doesn't exist, shows an error and returns an empty dictionary.

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
Generic error handler for other exceptions.

Function: display_word_counts

def display_word_counts(word_counts: dict):
Function that receives a dictionary of word counts.

    """
    Displays word counts in a formatted way.
    """
Docstring.

    print("Word Frequencies (Alphabetical Order):\n")
Title printed before showing the counts.

    for word, count in word_counts.items():
        print(f"{word:<15} : {count}")
Loops through each word and count.
Prints the word left-aligned (:<15) with its count.

Function: main()

def main():
Main driver function.

    print("Auto Word Counter from Generated File\n")
Prints a title when the program starts.

    filename = "sample.txt"
Sets the file name to "sample.txt".

    create_sample_file(filename)
Calls the function to create and write to the file.

    word_counts = count_words(filename)
Calls the function to read and count words in the file.

    if word_counts:
        display_word_counts(word_counts)
If word counts exist (not empty), display them.

Program Entry Point

if __name__ == "__main__":
    main()
Runs the main() function only if this script is executed directly (not imported as a module).

