import random
states = [
{
    "state": "Alabama",
    "capital": "Montgomery"
}, {
    "state": "Alaska",
    "capital": "Juneau"
}, {
    "state": "Arizona",
    "capital": "Phoenix"
}, {
    "state": "Arkansas",
    "capital": "Little Rock"
}, {
    "state": "California",
    "capital": "Sacramento"
}, {
    "state": "Colorado",
    "capital": "Denver"
}, {
    "state": "Connecticut",
    "capital": "Hartford"
}, {
    "state": "Delaware",
    "capital": "Dover"
}, {
    "state": "Florida",
    "capital": "Tallahassee"
}, {
    "state": "Georgia",
    "capital": "Atlanta"
}, {
    "state": "Hawaii",
    "capital": "Honolulu"
}, {
    "state": "Idaho",
    "capital": "Boise"
}, {
    "state": "Illinois",
    "capital": "Springfield"
}, {
    "state": "Indiana",
    "capital": "Indianapolis"
}, {
    "state": "Iowa",
    "capital": "Des Moines"
}, {
    "state": "Kansas",
    "capital": "Topeka"
}, {
    "state": "Kentucky",
    "capital": "Frankfort"
}, {
    "state": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "state": "Maine",
    "capital": "Augusta"
}, {
    "state": "Maryland",
    "capital": "Annapolis"
}, {
    "state": "Massachusetts",
    "capital": "Boston"
}, {
    "state": "Michigan",
    "capital": "Lansing"
}, {
    "state": "Minnesota",
    "capital": "St. Paul"
}, {
    "state": "Mississippi",
    "capital": "Jackson"
}, {
    "state": "Missouri",
    "capital": "Jefferson City"
}, {
    "state": "Montana",
    "capital": "Helena"
}, {
    "state": "Nebraska",
    "capital": "Lincoln"
}, {
    "state": "Nevada",
    "capital": "Carson City"
}, {
    "state": "New Hampshire",
    "capital": "Concord"
}, {
    "state": "New Jersey",
    "capital": "Trenton"
}, {
    "state": "New Mexico",
    "capital": "Santa Fe"
}, {
    "state": "New York",
    "capital": "Albany"
}, {
    "state": "North Carolina",
    "capital": "Raleigh"
}, {
    "state": "North Dakota",
    "capital": "Bismarck"
}, {
    "state": "Ohio",
    "capital": "Columbus"
}, {
    "state": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "state": "Oregon",
    "capital": "Salem"
}, {
    "state": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "state": "Rhode Island",
    "capital": "Providence"
}, {
    "state": "South Carolina",
    "capital": "Columbia"
}, {
    "state": "South Dakota",
    "capital": "Pierre"
}, {
    "state": "Tennessee",
    "capital": "Nashville"
}, {
    "state": "Texas",
    "capital": "Austin"
}, {
    "state": "Utah",
    "capital": "Salt Lake City"
}, {
    "state": "Vermont",
    "capital": "Montpelier"
}, {
    "state": "Virginia",
    "capital": "Richmond"
}, {
    "state": "Washington",
    "capital": "Olympia"
}, {
    "state": "West Virginia",
    "capital": "Charleston"
}, {
    "state": "Wisconsin",
    "capital": "Madison"
}, {
    "state": "Wyoming",
    "capital": "Cheyenne"
}]

# make a states dictionary of about 5 states
# states = [
#     {
#         'state': 'Arizona',
#         'capital': 'Phoenix'
#     }, {
#         'state': 'Indiana',
#         'capital': 'Indianaopis'
#     }, {
#         'state': 'Texas',
#         'capital': 'Austin'
#     }, {
#         'state': 'Georgia',
#         'capital': 'Atlanta'
#     }, {
#         'state': 'Oregon',
#         'capital': 'Salem'
#     }]



def states_game():
    # print a welcome message when game loads
    print ('Welcome to the Capitals game, let"s have some fun and play')
    # import the random method to shuffle trhought the states at random
    random.shuffle(states)
    # set varibales for right and wrong answers
    correct = 0
    wrong = 0 
    # create a for loop that loops through the states for a state
    for state in states:
        capital = input(f"What is the capital of {state['state']}? \n")
        # if the capital input is the same as the capital in the dict then award one correct point
        if capital == (f"{state['capital']}"):
            correct += 1
            print(f'Good work! Correct: {correct} Wrong: {wrong}')
        else: 
            # else, the answer is wrong dock the user one wrong point
            wrong += 1
            print(f'Oops, that was wrong! Correct: {correct} Wrong: {wrong}')   
     # after the game is over give input asking if user wants to play again
    replay_game = input(f'Game over! Correct: {correct} Wrong: {wrong}. \n Would you like to play again (y/n)')
    # if user prints y then recall the states_game function, if the user input is n give a goodbye message and if  the user inputs any other string then give better instruction for the next time they play and end the game automatically
    if replay_game == 'y':
        states_game()
    elif replay_game == 'n':
        print('Thanks for playing! See ya.')
    else:  
        print('Sorry you need to input a y or n. Bye.')
        
states_game()
