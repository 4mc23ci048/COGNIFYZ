# ============================================================
# LEVEL 2 - TASK 3
# PASSWORD STRENGTH CHECKER
# ============================================================


def check_password_strength(password):
    """
    Checks the strength of a password.

    The password is evaluated based on:
    1. Length
    2. Uppercase letters
    3. Lowercase letters
    4. Digits
    5. Special characters
    """

    score = 0
    suggestions = []

    # --------------------------------------------------------
    # Check password length
    # --------------------------------------------------------

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append(
            "Password should contain at least 8 characters."
        )

    # --------------------------------------------------------
    # Check uppercase letters
    # --------------------------------------------------------

    if any(character.isupper() for character in password):
        score += 1
    else:
        suggestions.append(
            "Add at least one uppercase letter."
        )

    # --------------------------------------------------------
    # Check lowercase letters
    # --------------------------------------------------------

    if any(character.islower() for character in password):
        score += 1
    else:
        suggestions.append(
            "Add at least one lowercase letter."
        )

    # --------------------------------------------------------
    # Check digits
    # --------------------------------------------------------

    if any(character.isdigit() for character in password):
        score += 1
    else:
        suggestions.append(
            "Add at least one number."
        )

    # --------------------------------------------------------
    # Check special characters
    # --------------------------------------------------------

    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"

    if any(character in special_characters for character in password):
        score += 1
    else:
        suggestions.append(
            "Add at least one special character."
        )

    # --------------------------------------------------------
    # Determine password strength
    # --------------------------------------------------------

    if score == 5:

        strength = "VERY STRONG"

    elif score == 4:

        strength = "STRONG"

    elif score == 3:

        strength = "MEDIUM"

    elif score == 2:

        strength = "WEAK"

    else:

        strength = "VERY WEAK"

    return strength, score, suggestions


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("       PASSWORD STRENGTH CHECKER")
print("========================================")

print()
print("Your password will be checked for:")
print("1. Minimum length of 8 characters")
print("2. Uppercase letters")
print("3. Lowercase letters")
print("4. Numbers")
print("5. Special characters")
print()

# Get password from user
password = input("Enter your password: ")

# Check password
strength, score, suggestions = check_password_strength(password)

# ------------------------------------------------------------
# Display Result
# ------------------------------------------------------------

print()
print("----------------------------------------")
print("       PASSWORD CHECK RESULT")
print("----------------------------------------")

print("Password Strength :", strength)
print("Security Score    :", str(score) + "/5")

print("----------------------------------------")

# Display suggestions
if suggestions:

    print()
    print("Suggestions:")

    for suggestion in suggestions:

        print("-", suggestion)

else:

    print()
    print("Excellent!")
    print("Your password satisfies all checks.")

print("----------------------------------------")
print()
print("Program completed successfully.")