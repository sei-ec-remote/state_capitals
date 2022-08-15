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

# *Hint: For the purposes of developing this program, start with a test array of three dictionaries so you don't have to play through all 50 states each time.
# dev_states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }    
# ]
# *Once the user has gone through all 50 states, ask them if they'd like to play again.

# *Getting Started You're given an array of dictionaries that contain each state name and capital.

# Bonus! Calculate a overall total score, display a running tally for each prompt If the user plays again, set the order of how the prompts appear to start with the ones they got wrong the most often. Add a hint functionality that prints the first 3 letters of a capital




# How many times did they get a capital wrong, store it here
wrong_answers = 0

# How many times did they answer correctly, store it here
right_answers = 0

#  initialize new keys in the dictionary for right and wrong
for state in states:
    state['right'] = 0
    state['wrong'] = 0
# test states
# for state in dev_states:
#     state['right'] = 0
#     state['wrong'] = 0


# start the game function
def game_round(right_answers, wrong_answers):
    # The game needs a welcome message:
    print('Welcome! It\'s time to learn the state capitals of the United States. When answering, please use correct casing or it will be marked incorrect.')
    
    # randomizing the states
    random_states = random.sample(states, len(states))
    # test states to avoid all 50
    # random_states = random.sample(dev_states, len(dev_states))
    # print(random_states)
    
    # while loop through the game responses
    while len(random_states) > 0:
        state = random_states[0]

        user_input = input(f'What is the capital of {state["name"]}? ')
        
        # If they get an answer right:
        if user_input == state['capital']:
            right_answers += 1
            state['right'] += 1  
            print(f"You answered {user_input}, and the answer is {state['capital']}! One point for you!")
        else:
        # If they get an answer wrong:
            wrong_answers += 1
            state['wrong'] += 1
            print(f"That is the wrong answer, the correct answer is {state['capital']}. One point in the bad category.")
        print (f"Correct Answers: {right_answers} ; Wrong Answers: {wrong_answers}")
        # to avoid repeating the same states
        random_states.pop(0)

        if len(random_states) <= 0:
            next_round = input('Would you like to play again? Enter y for yes and n for no. (y/n) ')
            if next_round == 'y':
                print(f'Beginning the next round!')
                game_round(right_answers, wrong_answers)
            else:
                print('Aw, okay, let\'s play again another time, bye bye!')

game_round(0, 0)


# need to index the list to access the dictionary