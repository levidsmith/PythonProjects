#2020 Levi D. Smith - levidsmith.com
#Simple number guessing game
#After each guess, it tells whether the secret number is higher or lower
#When the correct number is guessed, the total number of guesses is displayed
from random import randrange

print('Number Guessing Game - 2020 Levi D. Smith')

iSecretNum = randrange(1,100)
iGuessNum = -1
iGuessCount = 0

while (iGuessNum != iSecretNum):
    print('Guess the number from 1 to 100')
    iGuessNum = int(input())
    iGuessCount += 1
    
    if (iGuessNum > iSecretNum):
        print("Lower")
    elif (iGuessNum < iSecretNum):
        print("Higher")
    else:
        print("Correct!")

print('Secret number is ' + str(iSecretNum) + '.')
print('Total number of guesses ' + str(iGuessCount) + '.')