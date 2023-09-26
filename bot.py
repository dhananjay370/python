from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Start a conversation with the chatbot
print('Type "quit" to exit')
while True:
    try:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        bot_response = chatbot.get_response(user_input)
        print('Bot: ', bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
