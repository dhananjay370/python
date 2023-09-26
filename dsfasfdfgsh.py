from chatbot import ChatBot
from chatbot import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
bot = ChatBot('Example Bot')

# Set the trainer
bot.set_trainer(ChatterBotCorpusTrainer)

# Train the bot with the english corpus
bot.train("chatterbot.corpus.english")

# Get a response for some unexpected input
response = bot.get_response('How do I make an omelette?')
print(response)
