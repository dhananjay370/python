import tkinter as tk
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 100)

# Create the main window
window = tk.Tk()

# Create a label to prompt the user to enter a number
prompt_label = tk.Label(text="Guess a number between 1 and 100: ")
prompt_label.pack()

# Create an Entry widget to accept the user's input
number_entry = tk.Entry()
number_entry.pack()

# Create a function to check the user's guess


def check_guess():
  # Get the user's guess
  guess = number_entry.get()
  # Convert the guess to an integer (if it's not already)
  try:
    guess = int(guess)
  except ValueError:
    # Display an error message if the guess is not a number
    result_label.config(text="Please enter a valid number.")
    return
  # Compare the user's guess to the secret number
  if guess == secret_number:
    result_label.config(text="You Guessed it.")
  elif guess < secret_number:
    result_label.config(text="Lower Number Please!")
  else:
    result_label.config(text="Higher Number Please!")


# Create a button to check the user's guess
check_button = tk.Button(text="Check", command=check_guess)
check_button.pack()

# Create a label to display the result of the user's guess
result_label = tk.Label()
result_label.pack()

# Run the main loop
window.mainloop()
