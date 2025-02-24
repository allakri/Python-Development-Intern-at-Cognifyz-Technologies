# Task: Password Strength Checker

# Create a Python function that evaluates
# the strength of a password entered by the
# user. Implement checks for factors such as
# length, presence of uppercase and
# lowercase letters, digits, and special
# characters.
import random
import re

# Function to check the strength of a password
def password_strength_checker(password):
    # Check for password length
    length_error = len(password) < 8
    # Check for at least one uppercase letter
    uppercase_error = not any(char.isupper() for char in password)
    # Check for at least one lowercase letter
    lowercase_error = not any(char.islower() for char in password)
    # Check for at least one digit
    digit_error = not any(char.isdigit() for char in password)
    # Check for at least one special character
    special_char_error = not any(char in "!@#$%^&*()-+=<>?/" for char in password)
    
    # List of errors
    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_char_error]
    # Password strength levels
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    
    # Determine password strength based on the number of errors
    strength = strength_levels[max(0, 4 - sum(errors))]
    return strength

# Main function to take user input and evaluate password strength
def main():
    password = input("Enter a password to check its strength: ")
    strength = password_strength_checker(password)
    print(f"Password Strength: {strength}")

# Run the program if executed directly
if __name__ == "__main__":
    main()