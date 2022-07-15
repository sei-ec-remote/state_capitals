from capitals import states
import random
# from random import shuffle

# print(states)

random_states = random.sample(states, len(states))
# print(random_states)
right_answers = 0
wrong_answers = 0


## provide welcome message to introduce player to game
## running tallies for correct / incorrect answers
## after all 50 states are guessed, user gets to decide whether to play again
## user can input 'quit' to exit game at any time
## add new keys to dictionary to track each time user gets specific capital right/wrong
def play_game(right, wrong):

    for state in random_states:
        state['right'] = 0
        state['wrong'] = 0

    print('Welcome to "State Capitals! You will be given a state, your job is to correctly guess the capital. A tally will be kept of your right and wrong answer counts. Good Luck!!')

    while len(random_states) > 0:
        state = random_states[0]
        ##select first random state and assign user input to variable
        user_guess = input(f"Guess the capital of {state['name']}: ")
        if user_guess == state['capital']:
            right += 1
            state['right'] += 1
            print(f'Correct! {user_guess} is the capital of {state["name"]}')
            print(f'You have guessed the capital of {state["name"]} correctly {state["right"]} times and incorrectly {state["wrong"]} times')
        else:
            wrong -= 1
            state['wrong'] += 1
            print(f'Incorrect. {state["capital"]} is the capital of {state["name"]}')

        print(f'In total, you have guessed {right} right answers and {wrong} wrong answers.')
        random_states.pop(0)

play_game(right_answers, wrong_answers)

