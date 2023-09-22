import random
# enterlength=int(input("enter length of passowrd"))
def generate_password(length=12, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789' if include_digits else ""
    special_chars = "!@#$%^&*()_+[]{}|;:,.<>?/" if include_special_chars else ""

    # Combine character sets based on options
    all_chars = lowercase_chars + uppercase_chars + digits + special_chars

    # Ensure the password length is valid
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=8, include_digits=False, include_special_chars=False)
print("Generated Password:", password)
