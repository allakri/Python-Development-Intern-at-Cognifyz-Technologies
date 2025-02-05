"""Task: Palindrome Checker

Write a Python function that checks whether
a given string is a palindrome. A palindrome
is a word, phrase, or sequence that reads the
same backward as forward (e.g.,

"madam" or

"racecar")."""

def is_palindrome(s):
    # Remove spaces and convert to lowercase to make it case-insensitive
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome!")
else:
    print(f"'{input_string}' is not a palindrome.")
