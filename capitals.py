import random

states = [
{
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

print("Welcome to State the Capital!")

random.shuffle(states)
incorrect = 0
correct = 0

for state in states:
    ques = input('What is the capital of ' + state['name'] + '? ')
    if ques.title() != state['capital']:
        incorrect += 1
        print('Incorrect! The answer is: ' + state['capital'])
        print('Total correct = ', correct, ' incorrect = ', incorrect)
    elif ques.title() == state['capital']:
        correct += 1
        print('Correct!')
        print('Total correct = ', correct, ' incorrect = ', incorrect)

