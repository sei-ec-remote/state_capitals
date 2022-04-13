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

for state in states:
    state['correct'] = 0
    state['wrong'] = 0

# test list to use for development
# test = [{
#     'name': 'Washington',
#     'capital': 'Olympia'
# }, {
#     'name': 'Vermont',
#     'capital': 'Montpelier'
# }, {
#     'name': 'South Dakota',
#     'capital': 'Pierre'
# }]

# loop to go through the questions

# defining the game function
def state_game():
    # shuffling the list to a random order
    random.shuffle(states)
    # # defining correct answers and incorrect answers
    # # to keep a running total of a player's guesses through games
    # # set these to be global variables
    # corr = 0
    # incorr = 0
    # opening message
    print('Hello! Welcome to the state capitals guessing game!')
    # asking player if they'd like to play
    play = input('Would you like to play? (y/n):')
    # setting the start of the game based on the player's answer to play
    if (play == 'y' or play == 'yes'):
        print('Great, let\'s get started!')
        # setting loop to go through each state (currently in order)
        for state in states:
            # defining the question to be asked each time
            # using ''.format() instead of f'' since it's what we learned most recently
            question = input('What is the capital of {}?: '.format(state['name']))
            # setting conditional to check for correct answer
            # currently, user must get spelling and capitalization correct to count as a correct answer
            if (question == state['capital']):
                # increment correct answer key by one
                state['correct'] += 1
                # print a message for player
                print('Nice, you got it right!')
                print('You\'ve guessed this one correctly a total of {} times.'.format(state['correct']))
            # if the answer is wrong
            else: 
                # increment incorrect answer key by one
                state['wrong'] += 1
                # print a message for the player
                print('Dang, that\'s the wrong answer.')
                print('You\'ve answered this question wrong a total of {} times.'.format(state['wrong']))
        # after the whole list has been looped through
        # ask player if they'd like to play again
        play_again = input('That was fun! Would you like to play again? (y/n): ')
        # conditional
        if (play_again == 'y' or play_again == 'yes'):
            print('Great, let\'s play again!')
            # call the function again
            state_game()
        else:
            print('Alright, thanks for playing!')
    # if player answers n/no/anything that's not y or yes
    else: print('Alright, come back when you\'re ready!')
        
state_game()
