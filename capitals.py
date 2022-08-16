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

# # test array
# test_lists = [
#     {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }
# ]

for state in states:
    state['right'] = 0
    state['wrong'] = 0

# print(test_list)

# Welcome Message
print("Welcome to the State Capitals Game! All answers must use proper capitalization.\n")
play_game = True
while (play_game):
    random.shuffle(states)
    # keeps track of how many answers are right and wrong
    correct_answers = 0
    incorrect_answers = 0
    for state in states:
        answer = input(f'What is the capital of {state["name"]}?\n')
        # if the user gets the answer right
        if answer == state['capital']:
            # update correct answers for this round
            correct_answers += 1
            # update correct answers for this state in all rounds
            state['right'] += 1
            print("Good job! You got that one right!")
        # if the user gets the answer wrong 
        else:
            # update incorrect answers for this round
            incorrect_answers += 1
            # update incorrect answers for this state in all rounds
            state['wrong'] += 1
            print("Sorry, that is not correct.")
        # display how many correct and incorrect answers for this round
        print(f"Correct Answers: {correct_answers} | Incorrect Answers {incorrect_answers}\n")
        # display how many correct and incorrect answers for each state for all rounds
        print(f"Correct Answers For This State: {state['right']} | Incorrect Answers For This State {state['wrong']}\n")
    # Ask the user if they want to play again.
    restart_game = input('Do you want to play again? (yes/no)\n')
    if restart_game == 'no':
        play_game = False
        print('Thanks for playing! Come back soon!')
    if restart_game == 'yes':
        play_game = True


# this randomizes the list
# this prints the randomized list
# print(test_list)

# ask the user to what the state capital of a given state is




# if the user answers the question correctly/incorrectly, display a message that says so

# keep score of how many the user has answered correct and incorrect

# after the game is over, ask if the user wants to play again

