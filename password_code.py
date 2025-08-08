import random

# Characters to use for the password
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
digits = "0123456789"
special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

# Combine all characters
all_chars = lowercase + uppercase + digits + special_chars

# Function to create a strong password
def generate_password(length=12):
    if length < 6:
        return "Password length should be at least 6 characters."
    
    # Ensure the password has at least one lowercase, uppercase, digit, and special character
    password = random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(digits)
    password += random.choice(special_chars)
    
    # Fill the rest of the password length
    for _ in range(length - 4):
        password += random.choice(all_chars)
    
    # Convert password to list and shuffle
    password_list = list(password)
    random.shuffle(password_list)
    
    # Join list to make final string
    return "".join(password_list)

# Example usage
print("Generated strong password:", generate_password(12))
