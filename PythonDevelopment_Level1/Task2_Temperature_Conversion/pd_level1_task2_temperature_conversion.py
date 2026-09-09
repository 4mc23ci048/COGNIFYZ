# ============================================================
# LEVEL 2 - TASK 2
# TEMPERATURE CONVERSION
# ============================================================

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.

    Formula:
    Fahrenheit = (Celsius × 9/5) + 32
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.

    Formula:
    Celsius = (Fahrenheit - 32) × 5/9
    """
    return (fahrenheit - 32) * 5 / 9


# ============================================================
# MAIN PROGRAM
# ============================================================

print("========================================")
print("       TEMPERATURE CONVERSION")
print("========================================")

print()
print("This program converts temperatures")
print("between Celsius and Fahrenheit.")
print()
print("You can perform multiple conversions.")
print("Enter 'exit' whenever you want to stop.")
print()

# ============================================================
# CONTINUOUS LOOP
# ============================================================

while True:

    print("----------------------------------------")
    print("             SELECT OPTION")
    print("----------------------------------------")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    print("----------------------------------------")

    # Ask the user for their choice
    choice = input("Enter your choice (1/2/3): ").strip().lower()

    # ========================================================
    # EXIT OPTION
    # ========================================================

    if choice == "3" or choice == "exit":

        print()
        print("========================================")
        print("Thank you for using the program!")
        print("Program exited successfully.")
        print("========================================")

        break

    # ========================================================
    # CELSIUS TO FAHRENHEIT
    # ========================================================

    elif choice == "1":

        try:

            celsius = float(
                input("Enter temperature in Celsius: ")
            )

            fahrenheit = celsius_to_fahrenheit(celsius)

            print()
            print("----------------------------------------")
            print("          CONVERSION RESULT")
            print("----------------------------------------")
            print("Celsius     :", celsius, "°C")
            print("Fahrenheit  :", round(fahrenheit, 2), "°F")
            print("----------------------------------------")
            print()

        except ValueError:

            print()
            print("Invalid temperature!")
            print("Please enter a valid number.")
            print()

    # ========================================================
    # FAHRENHEIT TO CELSIUS
    # ========================================================

    elif choice == "2":

        try:

            fahrenheit = float(
                input("Enter temperature in Fahrenheit: ")
            )

            celsius = fahrenheit_to_celsius(fahrenheit)

            print()
            print("----------------------------------------")
            print("          CONVERSION RESULT")
            print("----------------------------------------")
            print("Fahrenheit  :", fahrenheit, "°F")
            print("Celsius     :", round(celsius, 2), "°C")
            print("----------------------------------------")
            print()

        except ValueError:

            print()
            print("Invalid temperature!")
            print("Please enter a valid number.")
            print()

    # ========================================================
    # INVALID CHOICE
    # ========================================================

    else:

        print()
        print("Invalid choice!")
        print("Please enter 1, 2, or 3.")
        print()


print()
print("Program completed.")