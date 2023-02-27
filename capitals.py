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

answered_correct = []
answered_incorrect = []

User = {}
User["correct"] = 0
User["incorrect"] = 0

print("Welcome to the state capitals game.\n")
User["name"] = input("Please enter your username.\n")
print("\nWelcome, {}!\n".format(User["name"]))
print("Let's begin.\n")

random.shuffle(states)

def game_over(User, states, answered_correct, answered_incorrect):
    print("Game over. You had {} correct answers and {} incorrect answers.\n".format(User["correct"], User["incorrect"]))

    play_again = input("Would you like to play again? Y/n \n")

    if play_again == "Y":
        states = answered_incorrect + answered_correct
        answered_correct = []
        answered_incorrect = []
        game_loop(User, states, answered_correct, answered_incorrect)
    else:
        print("\nThank you for playing.")

def game_loop(User, states, answered_correct, answered_incorrect):
    for index in range(len(states)):
        current = states[index]
        answer = input("What is the capital of {}? \n".format(current["name"]))

        if answer == current["capital"]:
            User["correct"] += 1
            print("\nCorrect! The capital of {} is {}. \n".format(current["name"], current["capital"]))
            answered_correct.append(current)
        elif answer != current["capital"]:
            User["incorrect"] += 1
            print("\nIncorrect. {} is not the capital of {}. \n".format(answer, current["name"]))
            answered_incorrect.append(current)
        
        del current
        
        print("Score - Correct: {} Incorrect: {} \n".format(User["correct"], User["incorrect"]))
    
    game_over(User, states, answered_correct, answered_incorrect)

game_loop(User, states, answered_correct, answered_incorrect)