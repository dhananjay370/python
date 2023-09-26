import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="quiz"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM questions")

questions = mycursor.fetchall()

for question in questions:
    q_id = question[0]
    q_text = question[1]
    answer1 = question[2]
    answer2 = question[3]
    answer3 = question[4]
    answer4 = question[5]
    correct_answer = question[6]

    print(q_text)
    print("A. " + answer1)
    print("B. " + answer2)
    print("C. " + answer3)
    print("D. " + answer4)

    user_answer = input("Enter your answer (A, B, C, or D): ")

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The correct answer was " + correct_answer)

# if user_answer == correct_answer:
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect. The correct answer was " + correct_answer)

# mycursor.execute("UPDATE users SET score=%s WHERE username=%s", (score, username))

# mydb.commit()

# print("Your current score is: " + str(score))

