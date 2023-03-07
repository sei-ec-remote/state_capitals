import random
# import random at the top, this will allow use to use the random.shuffle() func on the states list

states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}]

# print a welcome prompt
print('Welcome to State Capitals! You will be state, you are to guess its capital!')

# this holds our state and capital, it prompts the user to guess the capital of that state, after being looped in the guess_capital function
def check_answer(state):
    capital = state["capital"]
    guess = input("What is the capital of " + state["name"] + "? ")
    if guess.lower() == capital.lower():
        print("Correct! You get the worlds best cookie")
        return True
    else:
        print("Incorrect. The capital of " + state["name"] + " is " + capital + ". You get no cookie :(")
        return False
    
# define a recursive function, that prints a shuffled state
# i want to make the game case recursive, so that when a user wants to play again, the states are shuffled again
def guess_capital():
    # random was imported at the time, call the shuffle function on the states list
    random.shuffle(states)
    # define counter variables
    correct_guesses = 0
    incorrect_guesses = 0
    # loop through each list in state
    for state in states:
        # conditional to add the counter variables, if answer is correct: add to correct, and vice versa
        if check_answer(state):
            correct_guesses += 1
        else:
            incorrect_guesses += 1
    # after every state in the list has been guessed, end the game, and output the counter variables
    print("Game over! You guessed", correct_guesses, "capitals correct and", incorrect_guesses, "capitals incorrect.")
    # include a play_again function that prompts user to play again if desired
    # if yes, call guess_capital recursively 
    play_again = input("Wanna try again? (y/n)").lower()
    if play_again == "y":
        guess_capital()
    # if no, thank user for playing
    elif play_again == "n":
        print("Goodbye, Thanks for playing!")
    # if the input is not y or n, output an error message and provide the correct input
    else:
        print("Invalid input. Your choices were (Y or N)")
        guess_capital()

guess_capital()