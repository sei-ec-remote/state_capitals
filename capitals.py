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

import random
# *Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.
totals = {
    "correct": 0,
    "wrong": 0
}
# *Provide a welcome message to introduce the player to the game.
print("I hope you've been brushing up on your geography, because this game is gonna test you... \n\nWelcome to everyone's favorite STATE CAPITAL QUIZ GAME!")

# *Initialize new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times the answer is wrong.
for state in states:
    state["correct"] = 0
    state["wrong"] = 0


def capital_game():
    # *Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.
    random.shuffle(states)
    game_correct=0
    game_wrong=0
    for state in states:
        # *Through all 50 states, prompt the user to name the capital of the state.
        answer = input(f"What is the capital of {state['name']}?\n\n")
        # *If the answer is correct, display a message saying so, and increment the correct key.
        if answer.lower() == state['capital'].lower():
            state['correct']+=1
            totals['correct']+=1
            game_correct+=1
            print(f"\nDING DING DING! That is correct!\n")
        # *If the answer is wrong, display a message saying so, and increment the wrong key.
        else:
            state['wrong']+=1
            totals['wrong']+=1
            game_wrong+=1
            print(f"BZZZZZZT! That is incorrect. The correct answer was {state['capital']}.")
        # *After each prompt, display a message telling the reader how many times the state was answered correctly out of the total number of times answered.
        print(f"You have correctly identified {state['name']}'s capital {state['correct']} times! You have misidentified it {state['wrong']} times.\n This round you have answered {game_correct} capitals correctly, and {game_wrong} capitals incorrectly\n")
    # *Once the user has gone through all 50 states, ask them if they'd like to play again.
    play_again = input(f"\nWhew! That's all of them! You answered {game_correct} capitals correctly, and {game_wrong} capitals incorrectly.\n Play again (y/n)?")
    if play_again.lower == 'y':
        print('Get Ready! HERE WE GO!')
        capital_game()
    else:
        print(f"Thanks for playing!\n\n Total Scores:\ncorrect: {totals['correct']}\nincorrect: {totals['wrong']}")
capital_game()