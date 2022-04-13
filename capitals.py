import random
# states = [
# {
#     "name": "Alabama",
#     "capital": "Montgomery"
# }, {
#     "name": "Alaska",
#     "capital": "Juneau"
# }, {
#     "name": "Arizona",
#     "capital": "Phoenix"
# }, {
#     "name": "Arkansas",
#     "capital": "Little Rock"
# }, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford"
# }, {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee"
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Idaho",
#     "capital": "Boise"
# }, {
#     "name": "Illinois",
#     "capital": "Springfield"
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis"
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort"
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge"
# }, {
#     "name": "Maine",
#     "capital": "Augusta"
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Michigan",
#     "capital": "Lansing"
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul"
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson"
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City"
# }, {
#     "name": "Montana",
#     "capital": "Helena"
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln"
# }, {
#     "name": "Nevada",
#     "capital": "Carson City"
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord"
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton"
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe"
# }, {
#     "name": "New York",
#     "capital": "Albany"
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh"
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck"
# }, {
#     "name": "Ohio",
#     "capital": "Columbus"
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City"
# }, {
#     "name": "Oregon",
#     "capital": "Salem"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence"
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia"
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre"
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City"
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier"
# }, {
#     "name": "Virginia",
#     "capital": "Richmond"
# }, {
#     "name": "Washington",
#     "capital": "Olympia"
# }, {
#     "name": "West Virginia",
#     "capital": "Charleston"
# }, {
#     "name": "Wisconsin",
#     "capital": "Madison"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]

test_states = [{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}]

# -[DONE]- *Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.

# -[DONE]- *Provide a welcome message to introduce the player to the game.

# -[DONE]- *Initialize new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times the answer is wrong.

# -[DONE]- *Through all 50 states, prompt the user to name the capital of the state.

# -[DONE]- *If the answer is correct, display a message saying so, and increment the correct key.

# -[DONE]- *If the answer is wrong, display a message saying so, and increment the wrong key.

# -[DONE]- *After each prompt, display a message telling the reader how many times the state was answered correctly out of the total number of times answered.

# -[DONE]- *Once the user has gone through all 50 states, ask them if they'd like to play again.

# def replay():
#     global playing
#     if playing == False:
#         state_game()

def state_game():
    # playing = True
    # *Provide a welcome message to introduce the player to the game.
    print("Welcome to State Capital Game!")
    random.shuffle(test_states)
    correct = 0
    wrong = 0
    points = 0
    for state in test_states:
        capital = input(f"what is the capital of {state['name']}?\n")
        if capital == (f"{state['capital']}"):
            # *If the answer is correct, display a message saying so, and increment the correct key.
            correct += 1
            points += 1
            print(f"Nice!\nCorrect Answers: {correct}\nTotal Points: {points}" )
        else:
            # *If the answer is wrong, display a message saying so, and increment the wrong key.
            wrong += 1
            points -=0
            print(f"Wrong Answer!\nWrong Answers: {wrong}\nTotal Points: {points}")
    # playing = False
    # replay()
    play_again = input(f"Game Over! Your Score: {points}. Play Again? Y/N\n")
    if play_again == "Y":
        state_game()
    else:
        print("Bye :)")

state_game()
