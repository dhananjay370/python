import random
import string


def Password_Generator(lenght):
    source = string.ascii_letters+string.digits
    for i in range(lenght):
        result = random.choice(source)
        random.shuffle(result)
        print(result, end="")


Password_Generator(int(input("Enter Password Lenght : ")))
