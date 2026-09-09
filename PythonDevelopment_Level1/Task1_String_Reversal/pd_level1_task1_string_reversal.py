# ============================================================
# LEVEL 1 - TASK 1
# STRING REVERSAL
# ============================================================

def reverse_string(text):
    """
    This function takes a string as input
    and returns the string in reverse order.
    """

    reversed_text = text[::-1]

    return reversed_text


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("        STRING REVERSAL PROGRAM")
print("========================================")

# Ask the user to enter a string
text = input("Enter a string: ")

# Check whether the user entered something
if text == "":
    print("You did not enter any text.")
else:
    # Call the function
    result = reverse_string(text)

    # Display the original and reversed string
    print()
    print("Original String :", text)
    print("Reversed String :", result)

print()
print("Program completed successfully.")