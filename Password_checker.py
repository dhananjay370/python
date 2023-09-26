# def password_checker(password):
"""
    Check the strength of a password based on its length and complexity.

    Returns:
    - 'Weak' if the password is less than 6 characters long.
    - 'Moderate' if the password is at least 6 characters long and contains both letters and numbers.
    - 'Strong' if the password is at least 8 characters long and contains letters, numbers, and special characters.
"""
password = input('Enter Your Password : ')
if len(password) < 6:
    print('Weak Password!')
elif len(password) >= 6 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print('Moderate Password!')
elif len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(not char.isalnum() for char in password):
    print('Strong Password')
else:
    print('Weak Password')
