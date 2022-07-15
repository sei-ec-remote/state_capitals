from capitals import states
import random
# from random import shuffle

# print(states)

random_states = random.sample(states, len(states))
print(random_states)


## provide welcome message to introduce player to game
## running tallies for correct / incorrect answers
## after all 50 states are guessed, user gets to decide whether to play again
## user can input 'quit' to exit game at any time
## add new keys to dictionary to track each time user gets specific capital right/wrong

while len(random_states) > 0:
    ##randomly choose a state
    # print('hello')
    ##assign user input to value of capital

    ##if capital is correct, 

