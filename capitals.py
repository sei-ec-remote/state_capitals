import json
import random

def myfunction():
    return 0.1

states = [
{
    "name": "Alabama",
    "capital": "Montgomery",
    "played": 0
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
}
]


# =================== GAME =======================



welcome = input("Welcome to the State's Capital Game\n In this game you'll be asked to provide the name of capitals of the states\nDo you wish to play this game Yes or No: ")

# Initializing new keys (Only once so used a seperate function)
def new_keys():
    for state in states:
        state["correct"] = 0
        state["incorrect"] = 0
        state["played"] = 0

# Game function
def game():
    random.shuffle(states, myfunction)
    if (welcome.lower() == "Yes".lower()):
        for i, state in enumerate(states):
            
            # ------ name the state ------
            prompt= input(f"What is the capital of {state['name']} ? ")
            if (prompt.lower() == state["capital"].lower()):
                print('Correct Answer')
                states[i]["correct"] += 1  # update correct count in states dictionary
                states[i]["played"] += 1 
                
                print(f"( {states[i]['correct']} / {states[i]['played']} ) times the correct answer was given")

            elif state["incorrect"] <= 0:
                print('Incorrect Answer')
                states[i]["played"] += 1 
                
                print(f"( {states[i]['correct']} / {states[i]['played']} ) times the correct answer was given")
                
            else:
                states[i]["incorrect"] = states[i]["incorrect"] - 1
                states[i]["played"] += 1 
                print(state["played"])
                print(f"( {states[i]['correct']} / {states[i]['played']} ) times the correct answer was given")
    else:
        exit()
# Play the game for first time
new_keys()
game()

# After the game end's msg
end_game = input("Would you like to continue playing the game?\n Yes or No: ")
print(end_game)
if (end_game.lower() == "Yes".lower()):
    game()
else:
    exit()





