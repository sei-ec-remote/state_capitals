import capitals
import random


shuffledStates = capitals.states
random.shuffle(shuffledStates)

playGame = True

while playGame == True:

    correct = 0
    wrong = 0
    print('You are playing the Capital Game. Guess them!')
    for i in range(5):
        qState = shuffledStates[i]['name']

        guess = input(f'Capital of {qState}? ').capitalize()
        if guess == shuffledStates[i]['capital']:
            correct += 1
            print('correct')
        else:
            wrong += 1
            print('wrong')
    print(f'You lost. {correct} questions correct, and {wrong} questions wrong')

    playAgain = input('Play again? (Y or N) ')

    if playAgain == 'N':
        print('Good game, peace')
        playGame = False 