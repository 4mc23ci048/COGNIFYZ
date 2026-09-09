# ============================================================
# LEVEL 2 - TASK 5
# FILE MANIPULATION
# WORD FREQUENCY COUNTER
# ============================================================

import re


def read_file(filename):
    """
    Reads and returns the contents of a text file.
    """

    try:

        with open(filename, "r", encoding="utf-8") as file:

            content = file.read()

        return content

    except FileNotFoundError:

        print()
        print("Error: File not found.")
        print("Please make sure the file exists.")

        return None


def count_words(text):
    """
    Counts the occurrences of each word.
    """

    # Convert all text to lowercase
    text = text.lower()

    # Extract words from the text
    words = re.findall(r"\b[a-zA-Z]+\b", text)

    # Create empty dictionary
    word_count = {}

    # Count each word
    for word in words:

        if word in word_count:

            word_count[word] += 1

        else:

            word_count[word] = 1

    return word_count


def display_word_count(word_count):
    """
    Displays words alphabetically with their counts.
    """

    print()
    print("----------------------------------------")
    print("       WORD FREQUENCY RESULTS")
    print("----------------------------------------")

    # Sort words alphabetically
    sorted_words = sorted(word_count.keys())

    # Display each word and count
    for word in sorted_words:

        print(f"{word:<20} : {word_count[word]}")

    print("----------------------------------------")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("       FILE MANIPULATION PROGRAM")
print("========================================")

print()
print("This program counts the occurrence")
print("of every word in a text file.")
print()

# Ask user for filename
filename = input(
    "Enter the text file name: "
)

# Read file
content = read_file(filename)

# Continue only if file was successfully read
if content is not None:

    # Check whether file is empty
    if content.strip() == "":

        print()
        print("The file is empty.")

    else:

        # Count words
        word_count = count_words(content)

        # Display results
        display_word_count(word_count)

        # Display total number of unique words
        print()
        print(
            "Total Unique Words :",
            len(word_count)
        )

print()
print("Program completed successfully.")