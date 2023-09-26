def password_strenght(password):
    lenght = len(password) >= 8
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special = any(char in "!@#$%^&*" for char in password)

    if lenght and upper and lower and digit and special:
        print("Strong Password")
    else:
        print("Weak Password")
    

password_strenght('09809009003')
