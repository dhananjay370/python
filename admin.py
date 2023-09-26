questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A. Paris', 'B. London', 'C. Rome', 'D. Madrid'],
        'answer': 'A'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['A. Mars', 'B. Venus', 'C. Jupiter', 'D. Saturn'],
        'answer': 'A'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['A. Leonardo da Vinci', 'B. Vincent van Gogh', 'C. Pablo Picasso', 'D. Michelangelo'],
        'answer': 'A'
    },
    {
        'question': 'What is the largest ocean in the world?',
        'options': ['A. Pacific Ocean', 'B. Atlantic Ocean', 'C. Indian Ocean', 'D. Arctic Ocean'],
        'answer': 'A'
    },
    {
        'question': 'What is the symbol for the chemical element oxygen?',
        'options': ['A. O', 'B. H', 'C. C', 'D. Au'],
        'answer': 'A'
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'options': ['A. William Shakespeare', 'B. Oscar Wilde', 'C. Jane Austen', 'D. Mark Twain'],
        'answer': 'A'
    },
    {
        'question': 'What is the tallest mountain in the world?',
        'options': ['A. Mount Everest', 'B. Mount Kilimanjaro', 'C. Mount Fuji', 'D. Mount McKinley'],
        'answer': 'A'
    },
    {
        'question': 'Which country is known for the Great Wall?',
        'options': ['A. China', 'B. Italy', 'C. Germany', 'D. Brazil'],
        'answer': 'A'
    },
    {
        'question': 'What is the largest organ in the human body?',
        'options': ['A. Skin', 'B. Liver', 'C. Heart', 'D. Brain'],
        'answer': 'A'
    },
    {
        'question': 'Which instrument is known as the "king of instruments"?',
        'options': ['A. Pipe organ', 'B. Violin', 'C. Piano', 'D. Trumpet'],
        'answer': 'A'
    }
]

# Display the questions and options
for i, question in enumerate(questions, start=1):
    print(f"Question {i}: {question['question']}")
    for option in question['options']:
        print(option)
    print()

# To access a specific question and its details:
# question = questions[question_index]
# question_text = question['question']
# options = question['options']
# correct_answer = question['answer']

