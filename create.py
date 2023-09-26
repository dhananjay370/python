import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='quiz'
)

# Function to fetch a random question from the database
def fetch_question(cursor):
    query = "SELECT * FROM questions ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    return cursor.fetchone()

# Function to display the question and options
def display_question(question):
    print("Question:", question[1])
    print("Options:")
    for i in range(2, 6):
        print(question[i])
    print()

# Function to validate the user's answer
def validate_answer(question, answer):
    return question[6] == answer

# Function to calculate the prize money based on the question number
# Function to calculate the prize money based on the question number
def calculate_prize_money(question_number):
    prizes = [0, 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
    if question_number - 1 < len(prizes):
        return prizes[question_number - 1]
    else:
        return 0


# Main game loop
def play_game():
    cursor = cnx.cursor()

    question_number = 1
    score = 0
    prize_money = 0

    while True:
        print(f"Question {question_number}:")
        question = fetch_question(cursor)
        display_question(question)

        user_answer = input("Enter your answer (A/B/C/D): ")

        if validate_answer(question, user_answer):
            print("Correct answer!")
            score += 1
            prize_money = calculate_prize_money(question_number)
            print("Your current score:", score)
            print("Your current prize money:", prize_money)
        else:
            print("Wrong answer!")
            print("Game over!")
            break

        question_number += 1
        print()

        if prize_money == 0:
            print("Congratulations! You answered all the questions correctly.")
            break

    cursor.close()

# Call the play_game function to start the game
play_game()

# Close the database connection
cnx.close()
