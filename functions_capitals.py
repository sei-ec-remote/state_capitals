import capitals 
import random
import time

print('Welcome to knowledge check game!!!')
print('you will need to identify the capital associated with a given state!')
name = input("But before that, what is your name?: ")
print(f'Okey {name} here we go!')

correct = 0
incorrect = 0
start = True
while start:
    random.shuffle(capitals.states)

    for i in range(5):
        current_state = capitals.states[i]['name']
        print('to quit game, type quit')
        question = input(f'What is the capital of {current_state}?: ').lower()
        answer = capitals.states[i]['capital'].lower()
        print(i)
        if question == answer:
            print('CORRECT answer')
            correct += 1
            time.sleep(0.5)
        elif question == 'quit':
            print("Quitting game, see u next time!!!")
            start = False
            break
        elif question != answer:
            print(f'INCORRECT, correct answer is {answer}!')
            incorrect += 1
            time.sleep(0.5)
        if i == 4:
            print(f'you have {correct} correct answers!')
            print(f'and {incorrect} incorrect answers! \n not bad')
            start = False
            break

    ask = input('Do you want to try again?: ')
    if ask == 'yes':
        start = True
        correct = 0
        incorrect = 0
        continue
    elif ask == 'no':
        start = False
    

            

        

















# ask = input('do you want to play state-capitals game?:').lower()
# if ask == "yes" or "y":
#     start = True
# elif ask == 'no' or 'n':
#     start = False
# print(start)