from art import logo, stages
from wordlists import words
import random as rnd
import os

lines = ("-"*40)
def hangman():
    print(logo)
    game_word = rnd.choice(words)
    print(game_word)
    blanks = []
    for letters in game_word:
        blanks += "_"
    print(" ".join(blanks))
    print(lines)

    lives = 7
    game_over = False
    while not game_over:
        if "_" not in blanks:
            print("You Won !!!")
            print("Congratulations.")
            game_over = True
        else:
            user_input = input("Guess the word:\n>> ")
            if user_input in blanks:
                print("You've Already Guessed That Letter.")
                print("Guess Again !!!!!")
            else:
                n = 0
                for letter in game_word:
                    if user_input == letter:
                        blanks[n] = letter
                    n+=1
                print(" ".join(blanks))
                print(lines)

                wrong_letter_guessed = []    
                if user_input not in game_word:
                    if user_input in wrong_letter_guessed:
                        print("You've Already Guessed That Letter.")
                        print("Guess Again !!!!!")
                    elif user_input not in wrong_letter_guessed:
                        wrong_letter_guessed.append(user_input)
                        print(stages[lives-1])
                        lives -= 1
                        if lives == 1:
                            print("You 've one last life left. Save Your Hangman.")
                        if lives == 0:
                            game_over = True
                            print("You hanged your hangman.")
                            print("Game Over !!!!!")


play_again = True
while play_again:
    hangman()
    p_again = input("Play Again( Y/N ):\n>> ").lower()
    if p_again == "n":
        play_again = False
    else:
        os.system("clear")
    