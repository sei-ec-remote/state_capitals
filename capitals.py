states = [
{
    "name": "Alabama",
    "capital": "Montgomery",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Alaska",
    "capital": "Juneau",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Arizona",
    "capital": "Phoenix",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Arkansas",
    "capital": "Little Rock",
    "correct": 0,
    "wrong": 0
}, {
    "name": "California",
    "capital": "Sacramento",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Colorado",
    "capital": "Denver",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Connecticut",
    "capital": "Hartford",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Delaware",
    "capital": "Dover",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Florida",
    "capital": "Tallahassee",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Georgia",
    "capital": "Atlanta",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Hawaii",
    "capital": "Honolulu",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Idaho",
    "capital": "Boise",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Illinois",
    "capital": "Springfield",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Indiana",
    "capital": "Indianapolis",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Iowa",
    "capital": "Des Moines",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Kansas",
    "capital": "Topeka",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Kentucky",
    "capital": "Frankfort",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Maine",
    "capital": "Augusta",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Maryland",
    "capital": "Annapolis",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Massachusetts",
    "capital": "Boston",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Michigan",
    "capital": "Lansing",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Minnesota",
    "capital": "St. Paul",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Mississippi",
    "capital": "Jackson",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Missouri",
    "capital": "Jefferson City",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Montana",
    "capital": "Helena",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Nebraska",
    "capital": "Lincoln",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Nevada",
    "capital": "Carson City",
    "correct": 0,
    "wrong": 0
}, {
    "name": "New Hampshire",
    "capital": "Concord",
    "correct": 0,
    "wrong": 0
}, {
    "name": "New Jersey",
    "capital": "Trenton",
    "correct": 0,
    "wrong": 0
}, {
    "name": "New Mexico",
    "capital": "Santa Fe",
    "correct": 0,
    "wrong": 0
}, {
    "name": "New York",
    "capital": "Albany",
    "correct": 0,
    "wrong": 0
}, {
    "name": "North Carolina",
    "capital": "Raleigh",
    "correct": 0,
    "wrong": 0
}, {
    "name": "North Dakota",
    "capital": "Bismarck",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Ohio",
    "capital": "Columbus",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Oregon",
    "capital": "Salem",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Rhode Island",
    "capital": "Providence",
    "correct": 0,
    "wrong": 0
}, {
    "name": "South Carolina",
    "capital": "Columbia",
    "correct": 0,
    "wrong": 0
}, {
    "name": "South Dakota",
    "capital": "Pierre",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Tennessee",
    "capital": "Nashville",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Texas",
    "capital": "Austin",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Utah",
    "capital": "Salt Lake City",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Vermont",
    "capital": "Montpelier",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Virginia",
    "capital": "Richmond",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Washington",
    "capital": "Olympia",
    "correct": 0,
    "wrong": 0
}, {
    "name": "West Virginia",
    "capital": "Charleston",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Wisconsin",
    "capital": "Madison",
    "correct": 0,
    "wrong": 0
}, {
    "name": "Wyoming",
    "capital": "Cheyenne",
    "correct": 0,
    "wrong": 0
}]
from ast import If
import random
# Keep the game going until user want's to quit
playing = True
# Tally for the correct and wrong count for the corrent round the user is playing. Resets after game has ended.
correct_this_round = 0
wrong_this_round = 0

# Provide a welcome message to introduce the player to the game.
print("\nHello! Welcome to the game. We ask you questions, and you answer them. Then we tel you how smart you are. \n\nLets get started!!!!!!\n")

while playing == True:    
    # randomize the list of questions.
    random.shuffle(states)
    # This loop is whre the round is played in.
    for state in states:
        # ask the quetion.
        capital = input(f"What is the capital associated {state['name']}? ")
        # Check the user's answer
        if capital == state['capital']:
            # If user get's it right.
            print('\nYou got this correct you special snowflake you!\n')
            state['correct'] = state['correct'] + 1
            correct_this_round += 1
        else:
            # If user get's it wrong.
            print('That wasn\'t right at all! How could you?\n')
            state['wrong'] = state['wrong'] + 1
            wrong_this_round += 1
        # let the user know how they are doing compared to all rounds.
        print(f"This was answered correctly {state['correct']} out of the total of {state['correct'] + state['wrong']} times you have answered.")
    # Let the user know how they did this round.
    print(f"You got {correct_this_round} of them correct!")
    print(f"You got {wrong_this_round} of them wrong!")

    # Ask the user if they want to play another round.
    again = input('\nDo you want to play again? Maybe you can do better. (n/no): ')
    # If the user says no do these things, if any other input the loop keeps going. 
    # playing var true keeps the rounds going, so changed to false.
    # Reset correct_this_round and wrong_this_round since they only track wrong and right for the round only.
    if again == 'n' or again == 'no':
        playing = False
    correct_this_round = 0
    wrong_this_round = 0