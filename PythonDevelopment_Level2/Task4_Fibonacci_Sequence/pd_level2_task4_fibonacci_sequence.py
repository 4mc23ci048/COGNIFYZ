# ============================================================
# LEVEL 2 - TASK 4
# FIBONACCI SEQUENCE
# ============================================================


def generate_fibonacci(terms):
    """
    Generates the Fibonacci sequence
    for the specified number of terms.
    """

    sequence = []

    # First two Fibonacci numbers
    first = 0
    second = 1

    # Generate required number of terms
    for i in range(terms):

        sequence.append(first)

        # Calculate next number
        next_number = first + second

        # Move numbers forward
        first = second
        second = next_number

    return sequence


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("         FIBONACCI SEQUENCE")
print("========================================")

print()
print("The Fibonacci sequence starts with:")
print("0, 1, 1, 2, 3, 5, 8, 13 ...")
print()

try:

    # Get number of terms
    terms = int(input(
        "Enter the number of terms: "
    ))

    # Validate input
    if terms <= 0:

        print()
        print("Please enter a positive number.")

    else:

        # Generate sequence
        fibonacci = generate_fibonacci(terms)

        # Display result
        print()
        print("----------------------------------------")
        print("Fibonacci Sequence")
        print("----------------------------------------")

        for number in fibonacci:

            print(number, end=" ")

        print()
        print("----------------------------------------")
        print("Number of Terms :", terms)

except ValueError:

    print()
    print("Invalid input!")
    print("Please enter a whole number.")


print()
print("Program completed successfully.")