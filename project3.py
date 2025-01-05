# Hangman Game..
import random
import hangman_stages
import word_file

chosen_word = random.choice(word_file.words)
chosen_word = chosen_word.lower()
print(chosen_word)
lives = 6#in hangman
display = []
for letter in chosen_word:#you can also use range function
    display+='_'
print(display)   

game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ")
    for position in range(len(chosen_word)):
       letter = chosen_word[position]
       if letter==guessed_letter:
           display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:#membership
        lives-=1
        if lives==0:
            game_over = True
            print("You Lose")

    if '_' not in display:
         game_over = True
         ans = ""#converting into string..
         for i in display:
             ans+=i
         print(f"Resultant answer is : {ans}")    
         print("You Win !!")       
    print(hangman_stages.stages[lives])        