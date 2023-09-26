import random
num = random.randint(1, 100)
attempt = 1
user = 0
while user != num:
    user = int(input("Enter a number between 1 to 100 : "))
    if user > num:
        print("Lower number please!")
    elif user < num:
        print("Higher Number please!")
    else:
        print(f"You Guessed it in {attempt} Attempts.")

    attempt = attempt+1
