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

for obj in states:
    obj["correct"] = 0
    obj["incorrect"] = 0


user = input("Wanna play StatR the hottest state capitol game? ")

if user.casefold() == "yes" or user.casefold() == 'y':
    playing = True
    print(playing, "huh?")
    print("play")
elif user.casefold() != "yes" or user.casefold() != 'y':
    playing = False


def game_loop():
    global playing
    while playing == True:
        random.shuffle(states)
        counter = 0
        for state in states:
            if counter < 5:
                curr_state = states[counter]["name"]
                question = input(
                    f"What is the capital of {curr_state}? ").lower()
                if question == states[counter]["capital"].lower():
                    print(f"Correct!")
                    states[counter]["correct"] += 1
                    counter += 1
                else:
                    print("Incorrect! next question...")
                    counter += 1
                    state["incorrect"] += 1
            elif counter >= 5:
                print("greater than 5")
                user = input("Wanna play again? ")
                if user.casefold() == "yes" or user.casefold() == 'y':
                    counter = 0
                    playing = True
                    random.shuffle(states)
                    print("play")
                elif user.casefold() != "yes" or user.casefold() != 'y':
                    counter = 0
                    playing = False
                    break


if playing == True:
    game_loop()
