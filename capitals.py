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
# shuffle all 50 states
import random
#  VERSION 2 IN WORK--------------------------------------------------------------------------------------------------------------------------------------------
# min = 0
# max = 49
# Tally Score and Welcome message:
# scoreBoard = {
#     "Answered Correct": 0,
#     "Answered Incorrect": 0

# class Capital:
#     def __init__(self):
#         self.state = states

#     def capitalsGame(self,):
#         print('Welcome to the State Capitals Python Game! We are going to play a guessing game to help us memorize the names of the capitals of all 50 states! \n Let us Start!'),
#         for state in states:
#             random.shuffle(states)
#             question = input(f"what is the Capital of {self.state}?")
#     def questions(self):
#         if question == states['capital']:
#             correct += 1
#             print("You have earned a point!", scoreBoard)
#         else:
#             incorrect -= 1
#             print('You earned a point! Jk u lost a point :( ....', scoreBoard)

#         if correct == 50:
#             print('Seems like you know your States well enough. Would you like to play again?')
#             if play_again == 'y':
#                 Capital()
#             else:
#                 print('Have a great day')
# Capital().capitalsGame()
#  VERSION 2 IN WORK--------------------------------------------------------------------------------------------------------------------------------------------

# vr1
setGame = True

while setGame:
    random.shuffle(states)
    # Scoreboard
    incorrect = 0
    correct = 0
    # print("tally board")

    question = input("Would you like to play a hard python terminal game meant for only high IQ people? please answer with [y/n]")
    if question == "n":
        setGame = False
        print("Idiot, I knew you would back out.")

    if question == "y":
        print("Welcome to the State Capitals Python Game! We are going to play a guessing game to test you 'high IQ' with the names of the capitals of all 50 states. \n Let's start shall we?")
        
        for state in (states[:50]):
            question = input("What is the capital of " + state["name"]+ "? ")
           
            if question == state["capital"]:
                correct = correct + 1
                print("Hmmm that was lucky guess you got yourself a point. You have earned a point.")
            
            if question != state["capital"]:
                incorrect = incorrect + 1 
                print("Not a shocker you weren't going to get that point with that IQ. No points.")
            # if question != state["capital"]:
            #     correct != 50
            #     print("Seems like you know your States well enough. Would you like to play again? [y/n]")
        print("GAME OVER you have ", correct,  "correct and ",(incorrect), "incorrect" )
        question = input("Do you want to play again? [y/n]")
        if question == "y":
            setGame = True
        if question == "n":
            print("Idiot, come back next time you are ready....")
            setGame = False