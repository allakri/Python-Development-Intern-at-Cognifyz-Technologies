"""Task: Email Validator

Develop a Python function that validates
whether a given string is a valid email
address. Implement checks for the format,
including the presence of an "@" symbol and
a domain name"""



import tkinter as tk
from tkinter import messagebox
import re

class EmailValidator:
    def __init__(self, email):
        self.email = email.lower()  # Convert email to lowercase
        self.is_valid = False
        
    def validate(self):
        """Validates the email format using regex and rules."""
        if self.is_empty():
            return False, "Email cannot be empty."
        if self.contains_invalid_characters():
            return False, "Email contains invalid characters."
        if not self.has_at_symbol():
            return False, "Email must contain '@' symbol."
        if self.has_no_uppercase():
            return False, "Email local part should not contain uppercase letters."
        if not self.has_valid_local_part():
            return False, "Local part is too long or contains invalid characters."
        if not self.has_valid_domain():
            return False, "Invalid domain name or TLD."
        if not self.has_valid_mx_record():
            return False, "Domain doesn't have a valid mail server (MX record)."
        return True, "Email is valid."
    
    def is_empty(self):
        """Checks if the email is empty."""
        return len(self.email.strip()) == 0
    
    def contains_invalid_characters(self):
        """Checks if the email contains spaces or disallowed special characters."""
        disallowed_characters = " !#$%^&*()"
        return any(char in self.email for char in disallowed_characters)
    
    def has_at_symbol(self):
        """Checks if the email contains the '@' symbol."""
        return "@" in self.email
    
    def has_no_uppercase(self):
        """Checks if the local part contains uppercase letters."""
        local_part = self.email.split('@')[0]
        return any(char.isupper() for char in local_part)
    
    def has_valid_local_part(self):
        """Checks if the local part of the email is valid."""
        local_part = self.email.split('@')[0]
        if len(local_part) > 64:
            return False  # Local part should not exceed 64 characters
        local_part_regex = r'^[a-z0-9._%+-]+$'  # Allows valid characters (a-z, 0-9, ., _, %, +, -)
        return re.match(local_part_regex, local_part) is not None
    
    def has_valid_domain(self):
        """Checks if the domain part is valid."""
        domain_part = self.email.split('@')[-1]
        domain_regex = r'^[a-z0-9]+([.-][a-z0-9]+)*\.[a-z]{2,}$'  # Domain part and TLD validation
        return re.match(domain_regex, domain_part) is not None
    
    def has_valid_mx_record(self):
        """Placeholder for MX record validation (you can extend this with actual DNS checks)."""
        # To perform real MX record validation, you'd need to check the DNS, but we'll simulate it.
        domain = self.email.split('@')[-1]
        # For simplicity, assume a valid domain has at least one dot.
        return '.' in domain

class EmailValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Validator")
        
        # Setup GUI components
        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.root, text="Enter Email:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        self.validate_button = tk.Button(self.root, text="Validate Email", command=self.validate_email)
        self.validate_button.grid(row=1, columnspan=2, padx=10, pady=10)

    def validate_email(self):
        """Handles the validation process and shows a message box."""
        email = self.email_entry.get()
        email_validator = EmailValidator(email)
        is_valid, message = email_validator.validate()
        
        if is_valid:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

# Main entry point to run the GUI application
def run_email_validator():
    root = tk.Tk()
    app = EmailValidatorApp(root)
    root.mainloop()

# Run the application
if __name__ == "__main__":
    run_email_validator()
