# ============================================================
# LEVEL 2 - TASK 4
# BASIC CALCULATOR
# ============================================================

def add_numbers(num1, num2):
    """
    Adds two numbers.
    """
    return num1 + num2


def subtract_numbers(num1, num2):
    """
    Subtracts the second number from the first number.
    """
    return num1 - num2


def modulo_numbers(num1, num2):
    """
    Returns the remainder of division.
    """
    return num1 % num2


# ============================================================
# MAIN PROGRAM
# ============================================================

print("========================================")
print("           BASIC CALCULATOR")
print("========================================")

print()
print("Available Operations:")
print("+  Addition")
print("-  Subtraction")
print("%  Modulo")
print()
print("Type 'exit' at any time to stop.")
print()


# ============================================================
# CONTINUOUS CALCULATOR LOOP
# ============================================================

while True:

    print("----------------------------------------")
    print("Enter 'exit' to close the calculator.")
    print("----------------------------------------")

    # Get first number
    first_input = input(
        "Enter the first number: "
    ).strip().lower()

    # Check for exit
    if first_input == "exit":
        print()
        print("Calculator closed successfully.")
        break

    # Convert first number
    try:
        num1 = float(first_input)

    except ValueError:
        print()
        print("Invalid input!")
        print("Please enter a number or type 'exit'.")
        print()
        continue


    # --------------------------------------------------------
    # Get second number
    # --------------------------------------------------------

    second_input = input(
        "Enter the second number: "
    ).strip().lower()

    # Check for exit
    if second_input == "exit":
        print()
        print("Calculator closed successfully.")
        break

    # Convert second number
    try:
        num2 = float(second_input)

    except ValueError:
        print()
        print("Invalid input!")
        print("Please enter a number or type 'exit'.")
        print()
        continue


    # --------------------------------------------------------
    # Get operator
    # --------------------------------------------------------

    operator = input(
        "Enter operator (+, -, %): "
    ).strip().lower()

    # Check for exit
    if operator == "exit":
        print()
        print("Calculator closed successfully.")
        break


    # ========================================================
    # PERFORM CALCULATION
    # ========================================================

    if operator == "+":

        result = add_numbers(num1, num2)

        print()
        print("----------------------------------------")
        print("          CALCULATION RESULT")
        print("----------------------------------------")
        print(num1, "+", num2, "=", result)
        print("----------------------------------------")


    elif operator == "-":

        result = subtract_numbers(num1, num2)

        print()
        print("----------------------------------------")
        print("          CALCULATION RESULT")
        print("----------------------------------------")
        print(num1, "-", num2, "=", result)
        print("----------------------------------------")


    elif operator == "%":

        # Modulo by zero is not allowed
        if num2 == 0:

            print()
            print("----------------------------------------")
            print("ERROR!")
            print("Cannot perform modulo by zero.")
            print("----------------------------------------")

        else:

            result = modulo_numbers(num1, num2)

            print()
            print("----------------------------------------")
            print("          CALCULATION RESULT")
            print("----------------------------------------")
            print(num1, "%", num2, "=", result)
            print("----------------------------------------")


    else:

        print()
        print("----------------------------------------")
        print("Invalid operator!")
        print("Please use +, - or %.")
        print("----------------------------------------")


    # --------------------------------------------------------
    # Ask whether user wants another calculation
    # --------------------------------------------------------

    print()

    again = input(
        "Press Enter to continue or type 'exit' to stop: "
    ).strip().lower()

    if again == "exit":

        print()
        print("========================================")
        print("       Thank you for using calculator!")
        print("========================================")
        break

    print()


# ============================================================
# PROGRAM END
# ============================================================

print()
print("Program completed successfully.")