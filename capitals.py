states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

test_states = [
    {
    "name": "Colorado",
    "capital": "Denver"
},
{
    "name": "Wyoming",
    "capital": "Cheyenne"
},
{
    "name": "New York",
    "capital": "Albany"
}
]

import random

for state in range(len(states)):
        states[state]['correct'] = 0
        states[state]['wrong'] = 0

def game_loop():
    correct = 0
    wrong = 0
    random.shuffle(states)
    for state in states:
        print(f'What is the capital of: ', state['name'])
        answer = input('Please enter your answer (type h for a hint): ')
        if answer.lower() == state['capital'].lower():
            state['correct'] += 1
            correct += 1
            print('\nCorrect!  \n\n***Your score:*** \nThis state Correct:', state['correct'], '\nThis state Incorrect: ', state['wrong'],  '\n\nTotal correct: ', correct, '\nTotal incorrect: ', wrong, '\n')
        elif answer.lower() == 'h'.lower():
            print(state['capital'][:3])
            answer_with_hint = input('Enter your answer: ')
            if answer_with_hint.lower() == state['capital'].lower():
                state['correct'] += 1
                correct += 1
                print('\nCorrect!  \n\n***Your score:*** \nThis state Correct:', state['correct'], '\nThis state Incorrect: ', state['wrong'],  '\n\nTotal correct: ', correct, '\nTotal incorrect: ', wrong, '\n')
            else:
                state['wrong'] += 1
                wrong += 1
                print('\nIncorrect!  The capital of ', state['name'], 'is', state['capital'], '\n\n***Your score:*** \nThis state Correct:', state['correct'], '\nThis state Incorrect: ', state['wrong'], '\n\nTotal correct: ', correct, '\nTotal incorrect: ', wrong, '\n')
        else:
            state['wrong'] += 1
            wrong += 1
            print('\nIncorrect!  The capital of ', state['name'], 'is', state['capital'], '\n\n***Your score:*** \nThis state Correct:', state['correct'], '\nThis state Incorrect: ', state['wrong'], '\n\nTotal correct: ', correct, '\nTotal incorrect: ', wrong, '\n')

    print('Game over! Here is your final score: \nCorrect:', correct, '\nIncorrect: ', wrong)
    again = input('\nWould you like to play again? Enter Y or N ')
    if  again.lower() == 'y':
        game_loop()
    elif again.lower() == 'n':
        print('Thanks for playing!')
        None
    else:
        print('I did not understand that, I guess you do not want to play again')

game_loop()