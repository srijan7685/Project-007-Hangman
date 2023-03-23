from art import logo, stages
from wordlists import words
import random as rnd

print(logo)

game_word = rnd.choice(words)
print(game_word)
blanks = []
for letters in game_word:
    blanks += "_"
print(blanks)

lives = 6
while "_" in blanks:
    user_input = input("Guess the word:\n>> ")
    n = 0
    for letter in game_word:
        if user_input == letter:
            blanks[n] = letter
            print(blanks)
        n+=1
        
    if user_input not in game_word:
        print(stages[lives])
        lives -= 1

    