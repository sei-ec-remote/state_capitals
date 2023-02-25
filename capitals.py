import random

states = []
stats = {"correct": 0, "incorrect": 0, "turn": 0}

def initialize_game():
    state_list = [
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

    for state in state_list:
        states.append(state)
    
    stats["correct"] = 0
    stats["incorrect"] = 0
    stats["turn"] = 0

    game_loop()

def question():
    state_pick = random.choice(states)
    print(state_pick)
    answer = input(f" What is the capital of {state_pick['name']}?\n")
    states.remove(state_pick)
    stats["turn"] += 1
    if answer == state_pick["capital"]:
        stats["correct"] += 1
        print(f"That's correct! Your current score is {stats['correct']} out of {stats['turn']}.")
    else:
        stats["incorrect"] += 1
        print(f"Incorrect. Your current score is {stats['correct']} out of {stats['turn']}.")
    
def game_loop():
    print(stats["correct"])

    while len(states) > 0:
        question()
        
    print(f"Game over! Your final score was {stats['correct']} out of 50!")
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again == "y":
        initialize_game()
    else:
        print("Thank you for playing!")
    

ready = input("Hello and welcome to the State Capital Quiz game!\n Are you ready to play? (y/n)\n")
if ready == "y":
    initialize_game()
else:
    print("Come back again, y'hear?")