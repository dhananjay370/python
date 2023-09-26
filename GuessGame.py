import random
passed = 0
num = random.randint(1, 100)

guess = 1
user = 0
chances = 9
score = 90
while user != num:
    if chances == 0:
        print("Your Attempts is Over!")
        score = 0
        print("Game Over!")
        break
    print(f"Your remaining attempts is {chances}")
    user = int(input("Enter a number between 1 to 100 : "))
    if user > num:
        print("Lower Number Please!")

    elif user < num:
        print("Higher Number Please!")

    else:
        print(f"You Guessed it in {guess} Attempts..")
        print(f"Your Score is {score}")
        passed = 1

    score = score - 10
    guess = guess + 1
    chances = chances - 1
    mscore = score

mscore = score + 10
print(f"Your Score is Now {mscore}")

if passed == 1:
    num = random.randint(1, 60)
    guess = 1
    user = 0
    chances = 6
    score = 60
    while user != num:
        if chances == 0:
            print("Your Attempts is Over!")
            score = 0
            print("Game Over!")
            break
        print(f"Your remaining attempts is {chances}")
        user = int(input("Enter a number between 1 to 60 : "))
        if user > num:
            print("Lower Number Please!")

        elif user < num:
            print("Higher Number Please!")

        else:
            print(f"You Guessed it in {guess} Attempts..")
            passed = 2

        score = score - 10
        guess = guess + 1
        chances = chances - 1
        mscore = score

mscore = score + 10
print(f"Your Score is Now {mscore}")

if passed == 2:
    num = random.randint(1, 30)
    guess = 1
    user = 0
    chances = 3
    score = 30
    while user != num:
        if chances == 0:
            print("Your Attempts is Over!")
            score = 0
            print("Game Over!")
            break
        print(f"Your remaining attempts is {chances}")
        user = int(input("Enter a number between 1 to 30 : "))
        if user > num:
            print("Lower Number Please!")
        elif user < num:
            print("Higher Number Please!")
        else:
            print(f"You Guessed it in {guess} Attempts..")

        score = score - 10
        guess = guess + 1
        chances = chances - 1
        mscore = score

mscore = score + 10
print(f"Your Score is Now {mscore}")
