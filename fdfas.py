import msvcrt

def masked_input(prompt='Password: '):
    password = ''
    while True:
        ch = msvcrt.getch().decode('utf-8')
        if ch == '\r' or ch == '\n':
            break
        password += ch
        print('*', end='', flush=True)
    print()
    return password

username = input("Enter Your Username : ")
password = masked_input()

# Do something with the username and password, such as authenticate the user
print(f"Username: {username}")
print(f"Password: {password}")
