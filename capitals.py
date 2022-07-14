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
test_states = {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}
# *Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.

# *Provide a welcome message to introduce the player to the game.
welcome = ("Welcome to the state capitals game!")
print(welcome)
# *Initialize new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times the answer is wrong.

# *Through all 50 states, prompt the user to name the capital of the state.
def america_game():
    correct_count = 0
    random.shuffle(states)
    for state in states:
        print("What is the capital of " + state["name"] + "?")
# *If the answer is correct, display a message saying so, and increment the correct key.
        answer = input()
        if answer == state["capital"].capitalize():
            print('Correct!')
            correct_count += 1
# *If the answer is wrong, display a message saying so, and increment the wrong key.
        else:
            print('Wrong!')
# *After each prompt, display a message telling the reader how many times the state was answered correctly out of the total number of times answered.
    print("You got " + str(correct_count) + " out of " + str(len(states)) + " correct.")
# *Once the user has gone through all 50 states, ask them if they'd like to play again.
    play_again = input("Would you like to play again? (y/n)")
    if play_again == "y":
        america_game()
    else:
        print("Thanks for playing!")
# *Getting Started You're given an array of dictionaries that contain each state name and capital.
america_game()
# *Hint: For the purposes of developing this program, start with a test array of three dictionaries so you don't have to play through all 50 states each time.
