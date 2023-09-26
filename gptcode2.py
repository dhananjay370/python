import random

def play_game(low, high, max_chances, max_score):
    num = random.randint(low, high)
    user = 0
    chances = max_chances
    score = max_score
    passed = False

    while user != num:
        if chances == 0:
            print("Your attempts are over!")
            score = 0
            print("Game over!")
            break

        print(f"Your remaining attempts: {chances}")
        user = int(input(f"Enter a number between {low} and {high}: "))

        if user > num:
            print("Lower number please!")
        elif user < num:
            print("Higher number please!")
        else:
            print(f"You guessed it in {max_chances - chances + 1} attempts.")
            passed = True

        score -= 10
        chances -= 1

    mscore = score + 10
    print(f"Your score is now {mscore}")
    return passed

def main():
    passed = play_game(1, 100, 9, 90)

    if passed:
        passed = play_game(1, 60, 6, 60)

    if passed:
        play_game(1, 30, 3, 30)

if __name__ == '__main__':
    main()
