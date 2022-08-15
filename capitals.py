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


# print(states["names"])

number_correct = 0

number_wrong = 0

keep_playing = "yes"



print('Let\'s play a game to learn our state capitals! Ready? Let\'s being!' )
while keep_playing == "yes": 

    random.shuffle(states)

    for state in states: 

        question = input(f'What is the capital of {state["name"]}? \n')

        if question == state["capital"]:

            number_correct += 1
            print(f'That\'s correct! Great job! You have {number_correct} correct.')

            if number_correct == 5:
                print('Wow you\'re on a roll!')

            elif number_correct == 15: 
                print('Incredible! You\'re a capitals master! Keep it up!')
        
        else :

            number_wrong += 1
            print(f'Sorry that\'s incorrect. The correct answer is {state["capital"]}.')

    if number_correct <= 4: 
        keep_playing == input(f'Game over. You got {number_correct} correct and {number_wrong} wrong. Better luck next time!')


    elif number_correct >= 5 <= 15: 

        keep_playing == input(f'Game over. You got {number_correct} correct and {number_wrong} wrong. You were on a roll! You\'ve got it next time!')

    elif number_correct == 15: 

        keep_playing == input(f'Game over. You got {number_correct} correct and {number_wrong} wrong. Great job! You\'re a capitals expert!')

    elif number_correct == 50: 

        keep_playing == input(f'Wow you answered all 50 questions correctly! You are a capitals genius! Do you want to play again?')
         
        if keep_playing == "yes":

            keep_playing == "yes"

        else: print('That was fun! Come again soon!')



    