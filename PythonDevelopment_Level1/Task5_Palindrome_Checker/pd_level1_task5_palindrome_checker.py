# ============================================================
# LEVEL 1 - TASK 5
# PALINDROME CHECKER
# ============================================================

def check_palindrome(text):
    """
    Checks whether a string is a palindrome.

    A palindrome is a word or sequence that
    reads the same forward and backward.
    """

    # Convert text to lowercase
    text = text.lower()

    # Remove spaces
    text = text.replace(" ", "")

    # Reverse the text
    reversed_text = text[::-1]

    # Compare original and reversed text
    if text == reversed_text:
        return True
    else:
        return False


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("         PALINDROME CHECKER")
print("========================================")

print()
print("A palindrome reads the same forward")
print("and backward.")
print()

# Get input
text = input("Enter a word or phrase: ")

# Check whether input is empty
if text.strip() == "":

    print()
    print("You did not enter any text.")

else:

    # Call palindrome function
    result = check_palindrome(text)

    print()
    print("----------------------------------------")
    print("Palindrome Result")
    print("----------------------------------------")
    print("Original Text :", text)

    if result:
        print("Result        : PALINDROME")
        print("The text reads the same backward.")

    else:
        print("Result        : NOT A PALINDROME")
        print("The text does not read the same backward.")

    print("----------------------------------------")


print()
print("Program completed successfully.")