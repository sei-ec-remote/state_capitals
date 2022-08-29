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


# global variables
# might need to input more...not sure yet
answer_correct = 0
answer_wrong = 0
continue_playing = "yes"

# print welcome message for game
# remember to space out codes to help me with view
print("Welcome to Guess the Capital Game! Are you ready playa!?")
while continue_playing == "yes":

    random.shuffle(states)

    for state in states:

        question = input(f"What is the capital of {state['name']}? \n")

        if question == state["capital"]:

            answer_correct = answer_correct + 1
            print(f"Correct playa! Keep rolling! You have {answer_correct} correct!")

            if answer_correct == 10:
                print("Yoo! You are smacking this game!")

            elif answer_correct == 20:
                print("You are amazing! Keep the ball rolling!")

        else:

            answer_wrong = answer_wrong + 1
            print(f"That is wrong my friend. The correct answer is {state['capital']}.")

    if answer_correct <= 10:
        continue_playing == input(f"Game over. You got {answer_correct} correct and {answer_wrong} wrong. Try harder next time!")

    elif answer_correct >= 10 <= 20:
        continue_playing == input(f"Game over. You got {answer_correct} correct and {answer_wrong} wrong. You are doing better! Keep pushing playa!")

    elif answer_correct == 30:
        continue_playing == input(f"Game over. You got {answer_correct} correct and {answer_wrong} wrong. Wow! Look at your progress! Now try for all 50 states!")

    elif answer_correct == 50:
        continue_playing == input(f"Yo!!!! You busted up all 50 questions! You must be a capitals prodigy! Do you want to school this game again!?")

        if continue_playing == "yes":
            continue_playing == "yes"

        else: print("Play again if you enjoyed the game!")