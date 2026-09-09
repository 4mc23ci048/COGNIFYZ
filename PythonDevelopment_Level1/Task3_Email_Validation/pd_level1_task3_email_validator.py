# ============================================================
# LEVEL 1 - TASK 3
# EMAIL VALIDATOR
# ============================================================

def validate_email(email):
    """
    This function checks whether an email address
    follows a basic valid email format.
    """

    # Remove unnecessary spaces
    email = email.strip()

    # --------------------------------------------------------
    # Check whether email is empty
    # --------------------------------------------------------

    if email == "":
        return False

    # --------------------------------------------------------
    # Check for exactly one @ symbol
    # --------------------------------------------------------

    if email.count("@") != 1:
        return False

    # Split email into username and domain
    username, domain = email.split("@")

    # --------------------------------------------------------
    # Check username
    # --------------------------------------------------------

    if username == "":
        return False

    # --------------------------------------------------------
    # Check domain
    # --------------------------------------------------------

    if domain == "":
        return False

    # Domain must contain a dot
    if "." not in domain:
        return False

    # Domain should not start with a dot
    if domain.startswith("."):
        return False

    # Domain should not end with a dot
    if domain.endswith("."):
        return False

    # --------------------------------------------------------
    # Check for spaces
    # --------------------------------------------------------

    if " " in email:
        return False

    # --------------------------------------------------------
    # Check that dot is not immediately after @
    # --------------------------------------------------------

    if domain.startswith("."):
        return False

    # If all checks pass
    return True


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

print("========================================")
print("          EMAIL VALIDATOR")
print("========================================")

print()
print("Enter an email address to check.")
print()

email = input("Email Address: ")

# Validate email
if validate_email(email):

    print()
    print("----------------------------------------")
    print("Email Validation Result")
    print("----------------------------------------")
    print("Email :", email)
    print("Status: VALID")
    print("----------------------------------------")

else:

    print()
    print("----------------------------------------")
    print("Email Validation Result")
    print("----------------------------------------")
    print("Email :", email)
    print("Status: INVALID")
    print("----------------------------------------")

print()
print("Program completed successfully.")