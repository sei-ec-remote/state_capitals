import random

# https://www.w3schools.com/python/module_random.asp
# possibly use choice() to get a random state
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
}]

first_time = True
index_number = 0
correct_answered = 0
wrong_answered = 0



# print(states)

# We need to start the game, which will involve shuffling the states
# We then need to ask the state capital of a given state
# We need to give the user an option to input their answer then compare to the value of the state capital
# if it is correct, they get a correct point, if it is wrong they get a wrong point
# after getting a point the next question needs to be asked
# once all of the states have been asked and answered, we need to ask if the player wants to play again, if they do the game loop needs to happen again
# If they don't the game loop will end. 


# Primary game loop that shuffles the states
def game_loop():
    

    global index_number
    # shuffles the states
    random.shuffle(states)

    #  function for asking the questions 
    def question():

        # define global values
        global index_number
        global wrong_answered
        global correct_answered

        # handle correct answer
        answer = input("What is the capital of " + states[index_number]["name"] + "\n" )
        if (answer.lower() == states[index_number]["capital"].lower()):
            correct_answered += 1
            print(f"That is correct! Correct: {correct_answered} Incorrect: {wrong_answered}")
            index_number += 1
            # asks the next question
            if (index_number != len(states)):
                question()
            # determines if we want to run the game_loop again
            elif (index_number == len(states)):
                play_again = input("Do you want to play again? (yes or no) \n")
                if (play_again == "yes"):  
                    index_number = 0
                    correct_answered = 0
                    wrong_answered = 0
                    game_loop()
                elif (play_again == "no"):
                    print("Have a nice life")
        # handle incorrect answer
        elif (answer.lower() != states[index_number]["capital"].lower() ):
            wrong_answered += 1
            print(f"That is incorrect! Correct: {correct_answered} Incorrect: {wrong_answered}")
            index_number += 1    
            # asks the next question
            if (index_number != len(states)):
                question()
            # determines if we want to run the game_loop again
            elif (index_number == len(states)):
                play_again = input("Do you want to play again? (yes or no) \n")
                if (play_again == "yes"):  
                    index_number = 0
                    correct_answered = 0
                    wrong_answered = 0
                    game_loop()
                elif (play_again == "no"):
                    print("Have a nice life")

    if (index_number == 0):
        question()
    
    
if (first_time == True):
    game_loop()
    first_time = False
