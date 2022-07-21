from os import stat
import random

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

random.shuffle(states)
want_to_play = 0
gameplay_input = input('Ready to start? y/n ')
if(gameplay_input == 'y'):
    want_to_play = 0
else:
    print('Please play soon!')


while want_to_play == 0:
    if(want_to_play == 0):
        correct_count = 0
        wrong_count = 0
        current_number = 0

        gameplay_input = input('Welcome to capital tester!\nPlease enter the capital of the state prompted to earn points.\nPlease press enter key to begin,\nor q to quit:\n')
        if(gameplay_input == 'q'):
            want_to_play += 1
            break
        if(gameplay_input != 'q'):
            for state in states:
                print(state['name'])
                user_input = input('Please enter capital: ')
                print('q to quit')
                if(user_input == 'q'):
                    print('Thanks for playing')
                    want_to_play += 1
                    break
                else:
                    if(state['capital'] == user_input):
                        correct_count += 1
                        current_number += 1
                        print('wrong: ', correct_count)
                        print('Nice job! right: ', correct_count, '\n')
                        if(current_number >= 50):
                            play_again = input('Want to play again? y/n: ')
                            if(play_again == 'y'):
                                current_number = 0
                            else:
                                break
                    elif(state['capital'] != user_input):
                        current_number += 1
                        wrong_count += 1
                        print('right: ', correct_count)
                        print('Wrong sorry :(, wrong: ', wrong_count, '\n')
                        if(current_number >= 50):
                            play_again = input('Want to play again? y/n: ')
                            if(play_again == 'y'):
                                current_number = 0
                            else:
                                want_to_play = False
                                want_to_play += 1
                                gameplay_input = 'q'
                                break
    else:
        print(f'Hope you play again soon! \n')
        want_to_play = False
    