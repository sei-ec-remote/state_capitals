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


def shuffle_states(states):
    random.shuffle(states)
    return states

# Define a function to play the game
def play_game(states):
    # The counters for correct and wrong answers
    correct = 0
    wrong = 0
    
    # Loop through each state
    for state in states:
        # Prompt the user for the capital of the state
        capital = input(f"What is the capital of {state['state']}? ")
        
        # Check if answer is correct
        if capital == state['capital']:
            print("Correct!")
            state['correct'] = state.get('correct', 0) + 1
            correct += 1
        else:
            print(f"Wrong! The capital of {state['state']} is {state['capital']}.")
            state['wrong'] = state.get('wrong', 0) + 1
            wrong += 1
        
        # Display the number of correct and wrong answers for the state
        total = state.get('correct', 0) + state.get('wrong', 0)
        print(f"You have answered {state['state']} correctly {state.get('correct', 0)} out of {total} times.")
    
    # Display the overall score
    print(f"\nYou answered {correct} out of {correct + wrong} states correctly.")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
     
        states = shuffle_states(states)
       
        play_game(states)


states = shuffle_states(states)

print("Welcome to the State Capitals Quiz!")


play_game(states)
