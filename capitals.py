states = [
{
    "name": "Alabama",
    "capital": "Montgomery",
    "wrong_times": 0
}, {
    "name": "Alaska",
    "capital": "Juneau",
    "wrong_times": 0
}, {
    "name": "Arizona",
    "capital": "Phoenix",
    "wrong_times": 0
}, 
{
    "name": "Arkansas",
    "capital": "Little Rock",
    "wrong_times": 0
}, {
    "name": "California",
    "capital": "Sacramento",
    "wrong_times": 0
}, {
    "name": "Colorado",
    "capital": "Denver",
    "wrong_times": 0
}, {
    "name": "Connecticut",
    "capital": "Hartford",
    "wrong_times": 0
}, {
    "name": "Delaware",
    "capital": "Dover",
    "wrong_times": 0
}, {
    "name": "Florida",
    "capital": "Tallahassee",
    "wrong_times": 0
}, {
    "name": "Georgia",
    "capital": "Atlanta",
    "wrong_times": 0
}, {
    "name": "Hawaii",
    "capital": "Honolulu",
    "wrong_times": 0
}, {
    "name": "Idaho",
    "capital": "Boise",
    "wrong_times": 0
}, {
    "name": "Illinois",
    "capital": "Springfield",
    "wrong_times": 0
}, {
    "name": "Indiana",
    "capital": "Indianapolis",
    "wrong_times": 0
}, {
    "name": "Iowa",
    "capital": "Des Moines",
    "wrong_times": 0
}, {
    "name": "Kansas",
    "capital": "Topeka",
    "wrong_times": 0
}, {
    "name": "Kentucky",
    "capital": "Frankfort",
    "wrong_times": 0
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge",
    "wrong_times": 0
}, {
    "name": "Maine",
    "capital": "Augusta",
    "wrong_times": 0
}, {
    "name": "Maryland",
    "capital": "Annapolis",
    "wrong_times": 0
}, {
    "name": "Massachusetts",
    "capital": "Boston",
    "wrong_times": 0
}, {
    "name": "Michigan",
    "capital": "Lansing",
    "wrong_times": 0
}, {
    "name": "Minnesota",
    "capital": "St. Paul",
    "wrong_times": 0
}, {
    "name": "Mississippi",
    "capital": "Jackson",
    "wrong_times": 0
}, {
    "name": "Missouri",
    "capital": "Jefferson City",
    "wrong_times": 0
}, {
    "name": "Montana",
    "capital": "Helena",
    "wrong_times": 0
}, {
    "name": "Nebraska",
    "capital": "Lincoln",
    "wrong_times": 0
}, {
    "name": "Nevada",
    "capital": "Carson City",
    "wrong_times": 0
}, {
    "name": "New Hampshire",
    "capital": "Concord",
    "wrong_times": 0
}, {
    "name": "New Jersey",
    "capital": "Trenton",
    "wrong_times": 0
}, {
    "name": "New Mexico",
    "capital": "Santa Fe",
    "wrong_times": 0
}, {
    "name": "New York",
    "capital": "Albany",
    "wrong_times": 0
}, {
    "name": "North Carolina",
    "capital": "Raleigh",
    "wrong_times": 0
}, {
    "name": "North Dakota",
    "capital": "Bismarck",
    "wrong_times": 0
}, {
    "name": "Ohio",
    "capital": "Columbus",
    "wrong_times": 0
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City",
    "wrong_times": 0
}, {
    "name": "Oregon",
    "capital": "Salem",
    "wrong_times": 0
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg",
    "wrong_times": 0
}, {
    "name": "Rhode Island",
    "capital": "Providence",
    "wrong_times": 0
}, {
    "name": "South Carolina",
    "capital": "Columbia",
    "wrong_times": 0
}, {
    "name": "South Dakota",
    "capital": "Pierre",
    "wrong_times": 0
}, {
    "name": "Tennessee",
    "capital": "Nashville",
    "wrong_times": 0
}, {
    "name": "Texas",
    "capital": "Austin",
    "wrong_times": 0
}, {
    "name": "Utah",
    "capital": "Salt Lake City",
    "wrong_times": 0
}, {
    "name": "Vermont",
    "capital": "Montpelier",
    "wrong_times": 0
}, {
    "name": "Virginia",
    "capital": "Richmond",
    "wrong_times": 0
}, {
    "name": "Washington",
    "capital": "Olympia",
    "wrong_times": 0
}, {
    "name": "West Virginia",
    "capital": "Charleston",
    "wrong_times": 0
}, {
    "name": "Wisconsin",
    "capital": "Madison",
    "wrong_times": 0
}, {
    "name": "Wyoming",
    "capital": "Cheyenne",
    "wrong_times": 0
}]
import random
import re
print(' > Welcome to state capitals')
print('|************===============|')
print('|************===============|')
print('|************===============|')
print('|===========================|')
print('|===========================|')
print('|===========================|')
print(' > guess the capital of each US state')

game = {
    'right': 0,
    'wrong': 0
}

def convert_into_uppercase(a):
    return a.group(1) + a.group(2).upper()

def retry():
    try_again = input('You wanna try again? (y/n)')
    if try_again == 'y':
        game["right"] = 0
        game["wrong"] = 0
        game_start()
    elif try_again == 'n':
        print('see you next time!')
    else:
        print('I did not understand...')
        retry()


def final_score():
    print(f' > You guessed {game["right"]} capitals out of 50 states ')
    if game["right"] < 1:
        print('that is like... not even a capital.. wow...')
    elif game["right"] < 25:
        print('well.. you got some right. You could use some study.')
    elif game["right"] < 30:
        (print('not bad, you nailed more than half, keep studying!'))
    elif game["right"] < 40:
        print('Wow, you are pretty good! you are almost there')
    elif game["right"]< 50:
        print('AWWW you just missed one! try again, you are so close!')
    else:
        print('now that is a true american! CONGRATULATIONS! you know every capital of every state!')
    retry()


def game_start():
    random.shuffle(states)
    for state in states:
        if state["wrong_times"] == 1:
            hint = state["capital"][:1]
            print(f' What is the capital of {state["name"]}?')
            answer = input(f'a little hint.. starts with the letter "{hint}" ---> ')
            result = re.sub("(^|\s)(\S)", convert_into_uppercase, answer)
        elif state["wrong_times"] > 1:
            hint = state["capital"][:3]
            print(f' What is the capital of {state["name"]}?')
            answer = input(f'a little hint.. it starts by "{hint}..." ---> ')
            result = re.sub("(^|\s)(\S)", convert_into_uppercase, answer)
        else:
            answer = input(f' What is the capital of {state["name"]}? ---> ')
            result = re.sub("(^|\s)(\S)", convert_into_uppercase, answer)
        if result == state["capital"]:
            game["right"] += 1
            state['wrong_times'] = 0
            print(f'Your answer is {result}...')
            print(' > That is correct!')
            print(f' > SCORE: correct: {game["right"]} - wrong: {game["wrong"]} ')
        else:
            game['wrong']+= 1
            state["wrong_times"]+= 1
            print(f' > Your answer is {result}...')
            print(f' > That is wrong, the right answer is {state["capital"]}')
            print(f' > SCORE: correct: {game["right"]} - wrong: {game["wrong"]} ')
    final_score()
game_start()


