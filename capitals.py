from operator import truediv
import random

states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Alaska",
#     "capital": "Juneau",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Arkansas",
#     "capital": "Little Rock",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "California",
#     "capital": "Sacramento",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Colorado",
#     "capital": "Denver",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Delaware",
#     "capital": "Dover",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Idaho",
#     "capital": "Boise",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Illinois",
#     "capital": "Springfield",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Kansas",
#     "capital": "Topeka",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Maine",
#     "capital": "Augusta",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Michigan",
#     "capital": "Lansing",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Montana",
#     "capital": "Helena",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Nevada",
#     "capital": "Carson City",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "New York",
#     "capital": "Albany",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Ohio",
#     "capital": "Columbus",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Oregon",
#     "capital": "Salem",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Texas",
#     "capital": "Austin",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Virginia",
#     "capital": "Richmond",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, {
#     "name": "Washington",
#     "capital": "Olympia",
#     "answered_correctly": 0,
#     "answered_incorrectly": 0
# }, 
{
    "name": "West Virginia",
    "capital": "Charleston",
    "answered_correctly": 0,
    "answered_incorrectly": 0
}, {
    "name": "Wisconsin",
    "capital": "Madison",
    "answered_correctly": 0,
    "answered_incorrectly": 0
}, {
    "name": "Wyoming",
    "capital": "Cheyenne",
    "answered_correctly": 0,
    "answered_incorrectly": 0
}]

answers = {
    "correct": 0,
    "incorrect": 0
}

print('Welcome to State Capitalzzz!')

play_again = True

while (play_again):
    random.shuffle(states)
    for state in states:

        if state["answered_incorrectly"] > 0:
            answer = input(f"What is the capital of {state['name']}? \n HINT: {state['capital'][0:3]} \n")
        else:
            answer = input(f"What is the capital of {state['name']}? \n")

        if answer == state["capital"].lower():
            state["answered_correctly"] += 1
            answers["correct"]+= 1
            print(f"You are correct! \n \tTotal Score: Correct - {answers['correct']}, Incorrect - {answers['incorrect']}")
            print(f"\tState guesses: Correct - {state['answered_correctly']} Incorrect - {state['answered_incorrectly']} \n")
        else:
            state["answered_incorrectly"] += 1
            answers["incorrect"] += 1
            print(f"You are incorrect. \n \tTotal Score: Correct - {answers['correct']}, Incorrect - {answers['incorrect']}")
            print(f"\tState guesses: Correct - {state['answered_correctly']} Incorrect - {state['answered_incorrectly']} \n")
    
    play_again = input('Want to play again (yes, no)? ')
    if play_again == 'no':
        play_again = False

print(f"Total Score: Correct - {answers['correct']}, Incorrect - {answers['incorrect']} \n")
print('Goodbye!')