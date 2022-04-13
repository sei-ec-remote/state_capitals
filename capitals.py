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

# test_states = [
#     {
#         "name": "Alabama",
#         "capital": "Montgomery"
#     },
#     {
#         "name": "Florida",
#         "capital": "Tallahassee"
#     },
#     {
#         "name": "Maine",
#         "capital": "Augusta"
#     },
#     {
#         "name": "Texas",
#         "capital": "Austin"
#     },
#     {
#         "name": "Wyoming",
#         "capital": "Cheyenne"
#     }
# ]

correct = 0
incorrect = 0
    
def restart_game():
    play = input("Would you like to restart the game? Please type 'yes' if would like to play again! \n")
    if (play == 'yes'):
        print("New Game!")
        global correct
        correct = 0
        global incorrect
        incorrect = 0
        new_game()
    else:
        print("We hate to see you go... come back and play again soon!")


def new_game():
    play_game = 'yes'
    
    print("Welcome to the State Capitals Quiz!")
    play = input("Would you like to play the game? Please type 'yes' if would like to play\n")
    if (play == 'yes' and play_game == 'yes'):
        while(play_game == 'yes'):
            random.shuffle(states)
            for state in states:
                randomState = state["name"]
                correct_answer = state["capital"]
                answer = input(f"What is the capital of {randomState} ?\n")
                if (answer == correct_answer):
                    global correct
                    global incorrect
                    correct += 1
                    print("That is correct!")
                    print(f"Correct: {correct}\nIncorrect: {incorrect}")
                elif (answer != correct_answer):
                    incorrect += 1
                    print("That is incorrect :(")
                    print(f"Correct: {correct}\nIncorrect: {incorrect}")
            else:
                print(f"THE FINAL SCORE IS: \nCorrect: {correct}\nIncorrect: {incorrect}")
                play_game = input("The game is over... Would you like to play again?\n")
                if (play_game == 'no'):
                    print("We hate to see you go... come back and play again soon!")
                    
                    
new_game()
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     used_States_Arr = []

#     play = 'y'

#     while(play == 'y'):
#         random_index = random.randint(0, 49)
#         random_state = states[random_index]['name']
#         print(f'\n {random_state}')
#         answer = input("Enter the capital of this state: \n")
#         if (answer == random_state):
#             correct += 1
#             print('Correct!')
#             play = input('Type y to play again and any other letter to stop: \n')
#         else:
#             incorrect += 1
#             print('Better luck next time!')
#             play = input('Type y to play again and any other letter to stop: \n')
            
#         used_State = slice(states[random_index])
#         used_States_Arr.append(used_State)

#     print(f'You have {correct} correct answers!')
#     print(f'You have {incorrect} incorrect answers :(')
    
# stateCapitalGame()