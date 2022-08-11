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

test_states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}
]

player_score = {
    "correct": 0,
    "incorrect": 0
}

# let's create a game!
# addm some new keys to dictionaries to store total number of right and wrong answers for players
# player_score = {}

########################################
###### RIGHT, WRONG ANSWER FUNCTIONALITY
########################################

# after each prompt, display message telling player how many times the state was answered correctly (player_score[correct])

def right_answer():
    print("Congratulations, that was correct!")
    player_score["correct"] = player_score["correct"] + 1
    print(f'You have answered correctly a total of {player_score["correct"]} out of {player_score["correct"] + player_score["incorrect"]} times.')
    return

def wrong_answer():
    print("I'm sorry, that was incorrect.")
    player_score["incorrect"] = player_score["incorrect"] + 1
    print(f'You have answered correctly a total of {player_score["correct"]} out of {player_score["correct"] + player_score["incorrect"]} times.')
    return

def play_again():
    print('Congrats, you have gone through all the states!')
    print(f'Your final score was {player_score["correct"]} out of {player_score["correct"] + player_score["incorrect"]}.')
    play_again_answer = input(f'Would you like to play again? (yes, no)')
    if play_again_answer == 'yes': 
        correct = {'correct': 0}
        incorrect = {'incorrect': 0}
        player_score.update(correct)
        player_score.update(incorrect)
        # print(player_score)
        play_game()
    else:
        print('Thank you for playing!')
        return

#######################
###### GAME LOOP ######
#######################

# the game loop consists of:
# the game will welcome the user to the game and introduce the rules
welcome_message = 'Hello and welcome to guess the Capitol Cities! You will be given the name of a state, and your goal will be to answer with the correct state capitol name. Good luck!'

# shuffle the dictionary to use first!

def play_game():
    random.shuffle(states)
    for state in states:
        # prompt the user to name the capitol of the state
        answer = input(f'What is the capitol city of {state["name"]}? \n')
        if answer == state["capital"]:
            # if correct, provide 'right_answer' answer and increment the 'correct' key for player_score
            right_answer()
        else:
            # if incorrect, provide 'wrong_answer' answer and increment the 'incorrect' key for player_score
            wrong_answer()


print(welcome_message)
# nest this in a loop to do multiple times if wanted...
if (player_score["correct"] + player_score["incorrect"]) < 50:
    # looping once through all 50 states
    play_game()
if player_score["correct"] + player_score["incorrect"] == 50:
    # once cycled through all 50 states, ask if they'd like to play again
    play_again()

