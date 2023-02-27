import random

state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

stats = {'correct': 0, 'wrong': 0}

# define a function to ask the user a state capital question
def ask_question():
    # randomly select a state from the state capitals dictionary
    state = random.choice(list(state_capitals.keys()))
    # get the capital of the selected state
    capital = state_capitals[state]
    # ask the user for the capital of the selected state
    answer = input(f"What is the capital of {state}? ")
    # check if the user's answer is correct
    if answer.lower() == capital.lower():
        print("Correct!")
        # increment the number of correct answers
        stats["correct"] += 1
    else:
        print(f"Wrong! The capital of {state} is {capital}.")
        # increment the number of wrong answers
        stats["wrong"] += 1
    # display the user's current score
    print(f"You've answered {stats['correct']} out of {sum(stats.values())} questions correctly.")

# define a function to play the game
def play_game():
    # initialize the game stats
    stats = {"correct": 0, "wrong": 0}
    # keep asking questions until the user has answered all 50 states
    while len(stats) < 50:
        ask_question()
    # ask the user if they want to play again
    play_again = input("Would you like to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")

# start the game
play_game()