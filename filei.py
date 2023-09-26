def get_user():
    # Prompt user for login information
    login_id = input("Enter your login ID: ")
    password = input("Enter your password: ")

    # Return login information as tuple
    return (login_id, password)


def check_login(login_info_file, login_id, password):
    # Read file and check if login ID and password match
    with open(login_info_file, "r") as f:
        for line in f:
            if f"Login ID: {login_id}" in line and f"Password: {password}" in line:
                return True
    return False


login_info_file = "login_info.txt"

# Get login information from user
login_id, password = get_user()

# Check if login ID and password match
if check_login(login_info_file, login_id, password):
    print("Login successful!")
else:
    print("Invalid login ID or password.")
