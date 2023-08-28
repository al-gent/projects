import pandas as pd
import random

words = []
with open("thinkpython2/words.txt") as f:
    for line in f:
        words.append(line.strip())

def random_word(words):
    return random.choice(words).upper()

def hangman():
    word = random_word(words)
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    
    #get user input
    user_letter = input("Guess a letter: ").upper()
    
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
    elif user_letter in used_letters:
        print("You already used that character. Please try again.")
    else:
        print("Invalid character. Please try again.")
        
    #print(word_letters)
    #print(used_letters)
    
    #print("You have used these letters: ", " ".join(used_letters))
    
def hangman():
    word = random_word(words)
    guessed_letters = []

    while True:
        guess = input("Guess a letter: ").upper()
        guessed_letters.append(guess)
        print_word = ''
        for letter in word:
            if letter in guessed_letters:
                print_word+= letter
            else:
                print_word+='_'
        print(print_word)
        print('Used letters:', ' '.join(guessed_letters))   
        if print_word == word:
            break
    print('You win! Your word was', word)
    
hangman()
        