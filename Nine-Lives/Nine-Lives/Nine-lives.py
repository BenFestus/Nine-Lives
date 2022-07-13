'''Nine Lives Game'''

import random
import sys

def clue_updater(secret_word, clue, guess, unknown_letters):
    index = 0

    while index < len(secret_word):
        #Using secret word as the reference to append guess to clue list using index to locate the position of the letter
        if guess.lower() in secret_word[index]: 
            clue[index] = guess
            unknown_letters = unknown_letters - 1
        index = index + 1
    return unknown_letters

def difficulty():
    print('DIFFICULTY - \n 1 for Easy \n 2 for Neutral \n 3 for Hard')
    difficulty = input('Pick your difficulty  - ')
    print()
    difficulty = int(difficulty)

    if difficulty == 1:
        #Set lives to 12 if difficulty is 1
        lives = 12
    elif difficulty == 2:
        #Set lives to 9 if difficulty is 2
        lives = 9
    else:
        #Else set lives to 6
        lives = 6
    return lives #return the value of lives back to function

def get_game():
    #Flag variable to keep track of player's guess
    guess_correct = False
    #Calling difficulty fuction to lives variable
    lives = difficulty()
    unknown_letters = len(secret_word)

    while lives > 0:
        lives_left = heart_symbol * lives
        #Display the amount of lives left
        print('Lives left:',lives_left)
        #Display the clue
        print(clue)

        guess = input('Guess the letter or word - ')
        if guess == secret_word:
            #Display 'correct answer' when guess is same with secret word
            print('Correct Answer👍 \n')
            #Setting the flag variable to true since the guess is correct
            guess_correct = True
            break

        if guess in secret_word:
            print('Guess is in secret word👏 \n')
            #Update the clue if guessed letter is in secret word
            unknown_letters = clue_updater(secret_word, clue, guess, unknown_letters)
        else:
            print('Wrong guess!')
            print('You lose a life🥱 \n')
            #Subtract 1 from lives left
            lives = lives - 1
        
        if unknown_letters == 0:
            print('Bravo! You guessed the letters correctly')
            #Setting the flag variable to true since there are no unknown letters
            guess_correct = True
            break

    if guess_correct:
        #Display string if at the end of the loop, guess correct flag is true
        print('The secret word is', secret_word, '\n')
        
    else:
        #Display string if at the end of the loop, guess correct is still false
        print('I was thinking of', secret_word, '🤭 \n')
        
#List of words
words = ['savage', 'crashers', 'actors', 'tragic', 'blue', 'aliens', 'keyboard', 'vehicle', 'orange', 'classroom', 'tiger']
heart_symbol = u'\u2764'
 
print('\t WELCOME TO NINE LIVES GAME \n')

while True:
    
    #Select random word from words list
    secret_word = random.choice(words)

    clue = []
    index = 0
    while index < len(secret_word):
        #Append '?' to every iteration in the clue list as long as the length of the secret word is less grater than the index variable
        clue.append('?')
        index = index + 1

    print('\t 1 - START GAME \n \t 2 - EXIT \n')
    user_reply = input('Type 1 to start and 2 to exit -- ')
    print()
    user_reply = int(user_reply)
    if user_reply == 1:
        #Calling get game function
        get_game()

        user_response = input('Do you want to play again? (y/n) -- ')
        print()
        if user_response == 'n':
            break
    else:
        sys.exit()
    
        