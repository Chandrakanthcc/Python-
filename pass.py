import re

def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check if it contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if it contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if it contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if it contains at least one special character
    special_characters = "!@#$%^&*()-_+=~`[]{}|:;'<>,.?/"
    if not any(char in special_characters for char in password):
        return False

    # Check if it doesn't contain spaces
    if ' ' in password:
        return False

    # If all conditions are satisfied, return True
    return True

# Test the function
password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
