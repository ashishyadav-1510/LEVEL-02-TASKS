import re
from collections import defaultdict

def create_sample_file(filename: str):
    """
    Creates a sample text file and writes predefined content to it.
    Parameters:
        filename (str): The name of the file to create.
    """
    content = (
        "Hello world! This is a sample text file.\n"
        "Python is fun. Hello Python, hello world.\n"
        "Text files are used for input and output in Python.\n"
        "Acknowledge Me I am the Tribal Chief."
    )
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"File '{filename}' created with sample content.\n")

def clean_and_tokenize(line: str) -> list:
    """
    Cleans a line by removing punctuation and splitting into lowercase words.
    Parameters:
        line (str): A single line of text.
    Returns:
        list: A list of cleaned, lowercase words.
    """
    return re.findall(r'\b\w+\b', line.lower())

def count_words(filename: str) -> dict:
    """
    Reads a file and counts the occurrences of each word.
    Parameters:
        filename (str): The path to the text file.
    Returns:
        dict: A dictionary with words as keys and their counts as values, sorted alphabetically.
    """
    word_counts = defaultdict(int)

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = clean_and_tokenize(line)
                for word in words:
                    word_counts[word] += 1

        return dict(sorted(word_counts.items()))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def display_word_counts(word_counts: dict):
    """
    Displays word counts in a formatted way.
    Parameters:
        word_counts (dict): A dictionary of word frequencies.
    """
    print("Word Frequencies (Alphabetical Order):\n")
    for word, count in word_counts.items():
        print(f"{word:<15} : {count}")

def main():
    print("Auto Word Counter from Generated File\n")
    filename = "sample.txt"
    create_sample_file(filename)

    word_counts = count_words(filename)

    if word_counts:
        display_word_counts(word_counts)

if __name__ == "__main__":
    main()
