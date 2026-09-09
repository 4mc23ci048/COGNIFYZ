# ============================================================
# LEVEL 2 - TASK 2
# NUMBER GUESSER
# ============================================================

import random


def generate_random_number(minimum, maximum):
    """
    Generates a random number within the given range.
    """

    return random.randint(minimum, maximum)


def play_game(minimum, maximum):
    """
    Runs the number guessing game.
    """

    # Generate random number
    secret_number = generate_random_number(minimum, maximum)

    # Number of attempts
    attempts = 0

    print()
    print("========================================")
    print("            NUMBER GUESSER")
    print("========================================")

    print()
    print("I have selected a number between",
          minimum, "and", maximum)
    print("Try to guess it!")
    print()

    while True:

        try:

            guess = int(input("Enter your guess: "))

            # Check range
            if guess < minimum or guess > maximum:

                print(
                    "Please enter a number between",
                    minimum,
                    "and",
                    maximum
                )

                continue

            attempts += 1

            # Compare guess
            if guess < secret_number:

                print("Too Low!")
                print("Try a higher number.")
                print()

            elif guess > secret_number:

                print("Too High!")
                print("Try a lower number.")
                print()

            else:

                print()
                print("----------------------------------------")
                print("             YOU WON!")
                print("----------------------------------------")
                print("Correct Number :", secret_number)
                print("Total Attempts :", attempts)
                print("----------------------------------------")

                break

        except ValueError:

            print("Invalid input!")
            print("Please enter a valid whole number.")
            print()


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("        CUSTOM NUMBER GUESSER")
print("========================================")

try:

    minimum = int(input("Enter the minimum number: "))
    maximum = int(input("Enter the maximum number: "))

    # Make sure range is valid
    if minimum >= maximum:

        print()
        print("Invalid range!")
        print("Minimum must be smaller than maximum.")

    else:

        play_game(minimum, maximum)

except ValueError:

    print()
    print("Invalid input!")
    print("Please enter whole numbers.")


print()
print("Program completed successfully.")