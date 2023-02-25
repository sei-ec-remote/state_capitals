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

# print(states[0]["name"]) accesses state name
# print(states[0]["capital"]) accesses state capital
# print(states[0]) accesses full state dictionary

# import random
import random

# provide a welcome message
print("**************************************************\nLet's test your knowledge of all 50 state capitals \n**************************************************")

# initializes new keys in the dictionaries that store the number of times a user gets a capital correct and the number of times they get it wrong
for i in range(len(states)):
        states[i]["correct"] = 0
        states[i]["wrong"] = 0

def game_loop():
    # randomize order that states appear
    random.shuffle(states)

    for i in range(len(states)):
        # through all 50 states prompt the user to name the capital of the state
        answer = input("What is the capital of {}? \n".format(states[i]["name"])).lower()
        # if the answer is correct, display a message saying so and increment the correct key
        if answer == states[i]["capital"].lower():
            states[i]["correct"] += 1
            print("Correct!")
        # if the answer is wrong, display a message saying so, and increment the wrong key
        else:
            states[i]["wrong"] += 1
            print("Wrong!")
            
        # after each prompt, display a message telling the player how many times the state was answered correctly out of the total number of times answered
        print("***You have guessed {0}'s capital correct {1} times and wrong {2} times***".format(states[i]["name"], states[i]["correct"], states[i]["wrong"]))

    # ask user if they would like to play again
    play_again = input("Would you like to play again? Y/N \n")
    if play_again == "Y":
        random.shuffle(states)
        game_loop()
    else:
        print("******************************\nScore Totals: \n******************************")
        for i in range(len(states)):
            print("{0}: Correct: {1} Wrong: {2}".format(states[i]["name"], states[i]["correct"], states[i]["wrong"]))

game_loop()

