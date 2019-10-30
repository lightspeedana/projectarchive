import random
from re import sub
from os.path import dirname, join

currentDir = dirname(__file__)
filePath = join(currentDir, "./wordlist.txt")
lives = 10
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
usedList = []

def readWordlist(filePath):
    word = random.choice(open(filePath).readlines())
    return word

def substitute(word, alphabet):
    wordSub = word
    for char in alphabet:
        wordSub = sub(char, ' _', wordSub)
    print("Your word is", wordSub)
    return wordSub
    
def main(lives):
    word = readWordlist(filePath)
    looping = True
    while looping == True:
        wordSub = substitute(word, alphabet)
        if '_' not in wordSub:
            print('YOU WON!\nWell Done!!')
            print('You had', lives, 'lives remaining.')
            break
        elif lives == 0:
            gameOver(word)
            break
        print('You currently have', '▉'*lives,'lives left.')
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

def gameOver(word):
    print('GAME OVER!')
    print('The word was', word)

def welcome():
    print('Welcome to Hangman!')
    main(lives)

welcome()
    
