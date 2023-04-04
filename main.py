import tkinter as tk
import random
from wordlists import words
import random as rnd

##req "pyplay (pip install pyplay )"
# Define the list of words to choose from
#wordlist bata garni bhaye
##word = rnd.choice(words)
words = ["python", "java", "javascript", "php", "html", "css", "ruby", "swift", "kotlin", "csharp"]

# Define the function to choose a random word
def choose_word():
    return random.choice(words)

# Define the Hangman class
class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.max_guesses = 6

    def guess(self, letter):
        self.guesses.append(letter)
        if letter not in self.word:
            self.max_guesses -= 1

    def display_word(self):
        return " ".join([letter if letter in self.guesses else "_" for letter in self.word])

    def display_hangman(self):
        parts = [
            ##sorry bro tmro art gui ma last lamo bhayo
            # head
            "  |==== |  \n  |     O  \n",
            # body
            "  |     |  \n  |     |  \n",
            # arms
            "  |     /|\  \n  |     |  \n",
            # legs
            "  |    /|\\ \n  |     |  \n",
            # dead
            "  |     X  \n",
        ]
        return "".join(parts[:self.max_guesses])

# Define the GUI class
class HangmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game For programmer")

        # Create the word label
        self.word_label = tk.Label(master, text="", font=("Arial", 24))
        self.word_label.pack()

        # Create the hangman label
        self.hangman_label = tk.Label(master, text="", font=("Courier New", 12), fg="red")
        self.hangman_label.pack()

        # Create the guesses label
        self.guesses_label = tk.Label(master, text="", font=("Arial", 18))
        self.guesses_label.pack()

        # Create the input field
        self.input_field = tk.Entry(master, width=2, font=("Arial", 18))
        self.input_field.pack()

        # Create the guess button
        self.guess_button = tk.Button(master, text="Guess", command=self.guess)
        self.guess_button.pack()

        # Create the quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        # Start the game
        self.game = Hangman(choose_word())
        self.update_display()

    def guess(self):
        letter = self.input_field.get().lower()
        self.input_field.delete(0, tk.END)
        if len(letter) == 1:
            self.game.guess(letter)
        self.update_display()

    def update_display(self):
        self.word_label.config(text=self.game.display_word())
        self.hangman_label.config(text=self.game.display_hangman())
        self.guesses_label.config(text="Guesses left: " + str(self.game.max_guesses))
        if self.game.max_guesses == 0:
            self.game_over("You lost! Better Luck Next Time🥺")
        elif "_" not in self.game.display_word():
            self.game_over("You won!🥳")

    def game_over(self, message):
        self.word_label.config(text=self.game.word)
        self.guesses_label.config(text=message)
        self.input_field.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLE)

    def play_again(self):
        self.game = Hangman(choose_word())
        self.word_label.config(text="")
        self.hangman_label.config(text="")
        self.guesses_label.config(text="")
        self.input_field.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.pack_forget()
        self.update_display()


root = tk.Tk()
game = HangmanGUI(root)
root.mainloop()
