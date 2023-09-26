import msvcrt
import getpass


class showstars:
    def show(self):
        password = ""
        print("Enter Your Password: ", end="")
        while True:
            ch = msvcrt.getch()
            if ch == b'\r':
                break
            else:
                password += ch.decode('utf-8')
                print('*',end="")
        return password
        # print("\nPassword Entered: ", password)

sh = showstars()
password=sh.show()
print("\n")
print(password)
