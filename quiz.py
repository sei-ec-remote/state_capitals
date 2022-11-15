from capitals import states
import random

answers = {
    'correct': 0, 
    'incorrect': 0,
}

running_total = 0

def init_quiz():
    random.shuffle(states)
    global running_total
    while running_total < 50:
        for state in states:
            user_input = input(f"Question {running_total + 1}: What is the capital of {state['name']}? ")
            if user_input.lower() == state['capital'].lower():
                answers['correct'] += 1
                print("That's correct!")
            elif user_input.lower() != state['capital'].lower():
                answers['incorrect'] += 1
                print("Oh no! That's not the correct capital.")
            running_total += 1
            print(f"You correctly answered {answers['correct']}/{running_total} states." )

        restart = input(f"This is the end of the quiz! Your final score is {answers['correct']}/50.\n Would you like to play again? Y/N\n")
        if restart.lower() == 'y':
            init_quiz()
            running_total = 0
            answers['correct'] = 0
            answers['incorret'] = 0
        elif restart.lower() == 'n':
            print("Come back when you're ready to play!")
        else:
            print("Please enter Y to start the quiz, or N to come back another time.") 


print("You're about to play the States Quiz! Correctly identify the capital for each of the 50 states.")
ready_to_play = input("Are you ready to start the quiz? Y/N\n")
if ready_to_play.lower() == 'y':
    init_quiz()
elif ready_to_play.lower() == 'n':
    print("Come back when you're ready to play!")
else:
    print("Please enter Y to start the quiz, or N to come back another time.")
