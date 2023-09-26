import random
questions = [
    {
        "question": "1. Who is the current President of India?",
        "options": ["Ram Nath Kovind", "Pranab Mukherjee", "A. P. J. Abdul Kalam", "Pratibha Patil"],
        "answer": "Ram Nath Kovind"
    },
    {
        "question": "2. Who is the current Chief Minister of Tamil Nadu?",
        "options": ["Edappadi K. Palaniswami", "M. K. Stalin", "O. Panneerselvam", "M. Karunanidhi"],
        "answer": "Edappadi K. Palaniswami"
    },
    {
        "question": "3. Who is the current Governor of the Reserve Bank of India?",
        "options": ["Shaktikanta Das", "Urjit Patel", "Raghuram Rajan", "D. Subbarao"],
        "answer": "Shaktikanta Das"
    },
    {
        "question": "4. Who is the current Chief Minister of Gujarat?",
        "options": ["Vijay Rupani", "Narendra Modi", "Anandiben Patel", "Shankersinh Vaghela"],
        "answer": "Vijay Rupani"
    },
    {
        "question": "5. Who is the current Chief Minister of Maharashtra?",
        "options": ["Uddhav Thackeray", "Devendra Fadnavis", "Ashok Chavan", "Vilasrao Deshmukh"],
        "answer": "Uddhav Thackeray"
    },
    {
        "question": "6. Who is the current Chief Minister of West Bengal?",
        "options": ["Mamata Banerjee", "Buddhadeb Bhattacharjee", "Jyoti Basu", "Siddhartha Shankar Ray"],
        "answer": "Mamata Banerjee"
    },
    {
        "question": "7. Who is the current Chief Minister of Karnataka?",
        "options": ["B. S. Yediyurappa", "H. D. Kumaraswamy", "Siddaramaiah", "S. M. Krishna"],
        "answer": "B. S. Yediyurappa"
    },
    {
        "question": "8. Who is the current Chief Minister of Punjab?",
        "options": ["Capt. Amarinder Singh", "Parkash Singh Badal", "Surjit Singh Barnala", "Rajinder Kaur Bhattal"],
        "answer": "Capt. Amarinder Singh"
    },
    {
        "question": "9. Who is the current Chief Minister of Rajasthan?",
        "options": ["Ashok Gehlot", "Vasundhara Raje", "Bhairon Singh Shekhawat", "Harideo Joshi"],
        "answer": "Ashok Gehlot"
    },
    {
        "question": "10. Who is the current Chief Minister of Uttar Pradesh?",
        "options": ["Yogi Adityanath", "Akhilesh Yadav", "Mayawati", "Mulayam Singh Yadav"],
        "answer": "Yogi Adityanath"
    },
    {
        "question": "11. Who is the current Chief Minister of Bihar?",
        "options": ["Nitish Kumar", "Lalu Prasad Yadav", "Rabri Devi", "Jitan Ram Manjhi"],
        "answer": "Nitish Kumar"
    },
    {
        "question": "12. Who is the current Chief Minister of Odisha?",
        "options": ["Naveen Patnaik", "Biju Patnaik", "Giridhar Gamang", "Hemananda Biswal"],
        "answer": "Naveen Patnaik"
    },
    {
        "question": "13. Who is the current Chief Minister of Andhra Pradesh?",
        "options": ["Y. S. Jaganmohan Reddy", "Chandrababu Naidu", "N. T. Rama Rao", "Kotla Vijaya Bhaskara Reddy"],
        "answer": "Y. S. Jaganmohan Reddy"
    },
    {
        "question": "14. Who is the current Chief Minister of Assam?",
        "options": ["Sarbananda Sonowal", "Tarun Gogoi", "Hiteswar Saikia", "Prafulla Kumar Mahanta"],
        "answer": "Sarbananda Sonowal"
    },
    {
        "question": "15. Who is the current Chief Minister of Tripura?",
        "options": ["Biplab Kumar Deb", "Manik Sarkar", "Sudhir Ranjan Majumder", "Dasarath Deb"],
        "answer": "Biplab Kumar Deb"
    }

]

# print(type(questions))
# for question in questions:
#     random.shuffle(questions("options"))


# for question in questions:
#     print(question)
#     print(question)
#     print(question)
# for question in questions:
#     question = random.choice(question)
lavel = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
         160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]



# questions.sort(options)
for question in questions:
    # Print the question and options
    print(question['question'])
for i, option in enumerate(question['options']):
    print(f"{i + 1}. {option}")
# Shuffle the options for the question
# random.shuffle(question['options'])

# Print the shuffled options
# print(question['options'])
