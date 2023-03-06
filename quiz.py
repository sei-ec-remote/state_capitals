from capitals import states
import random

class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print('Hello and welcome! This is a game for memorizing capitals of all 50 states. \n Type ' + color.UNDERLINE + 'exit' + color.END + ' to end.')


def game():

    random.shuffle(states)

    correct = 0
    incorrect = 0   

    for state in states:
        current_state = state['name']
        current_capital = state['capital']
        # print(state['name'], state['capital'])

        user_input = input(color.BOLD + f'What is the captial of {current_state}? ' + color.END)
        
        if (user_input == 'exit'):
            exit()
        if (user_input == current_capital):
            correct += 1
            print(f'Congrats! \n Total correct answers is {correct} \n Current incorrect total is {incorrect}. \n')
        else:
            incorrect += 1
            print(f"Sorry, that's not quite it. The capital of {current_state} is {current_capital}. \n Current incorrect total is {incorrect}. \n Current correct total is {correct} \n")
    
    print(f'Done! Whew. \n TOTAL \n Correct : {correct}, Incorrect: {incorrect}')
    
    repeat_game = input('Play again? Yes / No ')

    if repeat_game == 'Yes':
        game()
    else:
        exit()

game()