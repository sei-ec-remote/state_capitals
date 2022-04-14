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

# Smaller sample size for testing
test_states = [
{
    "name": "Louisiana",
    "capital": "Baton Rouge"
},{
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Oregon",
    "capital": "Salem"
}]


# Allows the random method for randomizing states
import random

# Split the game into three functions, to control what happens and when:
# 1. Initialize the game and display welcome message
# 2. Loop through the states and manage right/wrong answers
# 3. Handle replay (will keep running tally)

# Main game function
def state_quiz():
    # Keep track of what question we're on
    question_count = 0
    # Keep track of how many the player has gotten right this game
    right_count = 0
    # Keep track of how many the player has gotten wrong this game
    wrong_count = 0
    # Randomize the state list
    random.shuffle(states)

    # Will loop through each state in the list, ask the capital, and handle the answer
    for state in states:
        question_count += 1
        print("********************")
        print(f"Question {question_count} of {len(states)}")
        print("********************")
        print(f"What is the capital of {state['name']}?")
        response = input("Answer: ")

        # Put the response and expected answer to lowercase so player can still get the right answer without capitalizing
        if response.lower() == state["capital"].lower():
            # Increment the dictionary-based tally of times the user has correctly answered the question across multiple plays
            state["right"] += 1
            # Increment this specific game's count of correct answers.
            right_count += 1
            print(f"{state['capital']}, {state['name']}, that's right!")
            # Print the running tally of times across all games that the player has answered this state's capital.
            print(f"You've gotten {state['name']}'s capital right {state['right']} times and wrong {state['wrong']} times.\n")
        else:
            # Increment the dictionary-based wrong answer tally...
            state["wrong"] += 1
            # ...and the times this game the player has gotten it wrong.
            wrong_count += 1
            print(f"Sorry, {response} is incorrect.")
            print(f"You've gotten {state['name']}'s capital right {state['right']} times and wrong {state['wrong']} times.\n")

    # Once the player has answered for all the states, display their total right/wrong counts for this specific game.
    print(f"You got {right_count} right and {wrong_count} wrong.\n")
    # Run the replay function to see if the player wants to play again.
    replay()

# Ask the player if they'd like to play again and handle their answer.
def replay():
    play_again = input("Would you like to play again? (y/n) ")
    # If yes (regardless of case), run the main gameplay function again.
    if play_again.lower() == "y":
        print("Awesome! Good luck!\n")
        state_quiz()
    # If no (regardless of case), display a message and exit
    elif play_again.lower() == "n":
        print("Thanks for playing!")
    # If any other entry, display an error message and rerun replay to prompt for correct input.
    else:
        print("Invalid selection")
        replay()

# The first function that we'll call, intended to be run once and only once when specifically called.
def intro_quiz():
    input("It's 4th grade again and you need to know your states and capitals. How much do you remember? Let's find out! (hit enter to continue)")
    # Initialize our dictionary-based tallies for each state that will track the player's right/wrong answers across all games this session.
    for state in states:
        state["right"] = 0
        state["wrong"] = 0
    # Call the main gameplay function
    state_quiz()

# Finally, call the function to run the introduction function on script load.
intro_quiz()
