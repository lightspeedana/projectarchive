import random
from re import sub

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
usedList = []
looping = True
word = random.choice(open('wordlist.txt').readlines())
print('Welcome to Hangman!')
lives = 10
while looping == True:
    if lives == 0:
        print('GAME OVER!')
        print('The word was', word)
        break
    wordSub = word
    for char in alphabet:
        wordSub = sub(char, ' _', wordSub)
    if '_' not in wordSub:
        print('YOU WON!\nWell Done!!')
        print('You had', lives, 'lives remaining.')
        break
    print('You currently have', '▉'*lives,'lives left.')
    print('Your word is currently', wordSub)
    print(word)
    userGuess = input('Enter your guess, 1 letter: ')
    if len(userGuess) == 1:
        if userGuess.lower() in alphabet:
            alphabet.remove(userGuess.lower())
            usedList.append(userGuess.lower())
            if userGuess.lower() in word:
                print('You guessed a letter right!')
            else:
                print('Oh no, you lost a life!')
                lives -= 1
        elif userGuess.lower() in usedList:
            print('You\'ve tried this letter already!')
        else:
            print('Invalid input! Guess again.')
    else:
        print('Invalid input! Guess again.')
