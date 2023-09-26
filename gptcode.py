import random

MAX_ATTEMPTS = [9, 6, 3] # maximum number of attempts for each level
MAX_RANGE = [100, 60, 30] # maximum range of numbers for each level
SCORE_MULTIPLIER = 10 # score multiplier for each level

def play_level(max_range, max_attempts):
    num = random.randint(1, max_range)
    score = max_attempts * SCORE_MULTIPLIER
    for guess in range(1, max_attempts+1):
        user = int(input(f"Enter a number between 1 to {max_range}: "))
        if user > num:
            print("Lower Number Please!")
        elif user < num:
            print("Higher Number Please!")
        else:
            print(f"You Guessed it in {guess} Attempts..")
            return True, score - guess
    print("Your Attempts is Over!")
    return False, 0

def main():
    total_score = 0
    for i in range(3):
        print(f"Level {i+1}")
        passed, score = play_level(MAX_RANGE[i], MAX_ATTEMPTS[i])
        total_score += score
        if not passed:
            print("Game Over!")
            break
        print(f"Your Score is Now {total_score}")
    print(f"Total Score is {total_score}")

if __name__ == '__main__':
    main()
