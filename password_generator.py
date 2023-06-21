# password_generator.py

import random
import string

class PasswordGenerator:
    def __init__(self):
        self.password = ""

    def generate_password(self, length=8, include_letters=True, include_numbers=True, include_symbols=True):
        characters = ""
        if include_letters:
            characters += string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            print("Error: No character types selected.")
            return

        self.password = ''.join(random.choice(characters) for _ in range(length))

    def display_password(self):
        if self.password:
            print("Generated Password:", self.password)
        else:
            print("No password generated yet.")

# Usage example
password_generator = PasswordGenerator()

password_generator.generate_password(length=10, include_letters=True, include_numbers=True, include_symbols=True)
password_generator.display_password()
