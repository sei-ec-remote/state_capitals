# bring in capitals to have list of states and capitals
import capitals
# random so we can use shuffle
import random

# create array of all states and then shuffle it
shuffledStates = capitals.states
random.shuffle(shuffledStates)
# print(shuffledStates)

# want to play game
playGame = True
# while user still wants to play
while playGame == True:
    # set score to 0 upon starting game
    correct = 0
    wrong = 0
    print('Welcome to the game! You will be presented with a state and expected to type in the capital of that state. Good luck!')
    # go through all 50 states
    for i in range(3):
        # for each question, pick state from shuffled list
        questionState = shuffledStates[i]['name']
        # capitalize to allow users to input lower or uppercase and still be right
        userGuess = input(f'What is the capital of {questionState}? ').capitalize()
        # check if user input the right answer, capital of the state from the question
        if userGuess == shuffledStates[i]['capital']:
            correct += 1
            print('Correct answer!')
        else:
            wrong += 1
            print('Wrong answer!')
    # once all turns are done, print final score
    print(f'Game over! You got {correct} questions correct and {wrong} questions wrong')

    # ask if user wants to play again, if not print goodbye message and exit
    playAgain = input('Would you like to play again? (yes or no) ').lower()
    if playAgain == 'no':
        print('Thank you for playing, goodbye!')
        playGame = False