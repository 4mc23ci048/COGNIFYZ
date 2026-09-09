# ============================================================
# LEVEL 2 - TASK 1
# GUESSING GAME
# ============================================================

import random


def generate_number():
    """
    Generates a random number between 1 and 100.
    """
    return random.randint(1, 100)


def guessing_game():
    """
    Main function for the guessing game.
    """

    # Generate the secret number
    secret_number = generate_number()

    # Count the number of attempts
    attempts = 0

    print("========================================")
    print("          NUMBER GUESSING GAME")
    print("========================================")

    print()
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")
    print()

    # Continue until the user guesses correctly
    while True:

        try:
            guess = int(input("Enter your guess: "))

            # Check whether guess is within range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Increase attempt count
            attempts += 1

            # Check the guess
            if guess < secret_number:

                print("Too Low! Try a higher number.")
                print()

            elif guess > secret_number:

                print("Too High! Try a lower number.")
                print()

            else:

                print()
                print("========================================")
                print("          CONGRATULATIONS!")
                print("========================================")
                print("You guessed the correct number!")
                print("Secret Number :", secret_number)
                print("Attempts      :", attempts)
                print("========================================")

                break

        except ValueError:

            print("Invalid input!")
            print("Please enter a whole number.")
            print()


# ------------------------------------------------------------
# Start Program
# ------------------------------------------------------------

guessing_game()

print()
print("Program completed successfully.")