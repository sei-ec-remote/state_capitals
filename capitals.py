import random

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


answer=''
correct=0
incorrect=0

# random.shuffle(states)
# for i in range(len(states)):
#     states[i]['correct'] = 0
#     states[i]['incorrect'] = 0
#     states[i]['answered'] = 0

print('Welcome to the state captials game\nYou will be guessing the capital of each state that is given\n')

# while answer != 'quit':
#     for i in range(len(states)):   
#         # states[i]['correct'] = 0
#         # states[i]['incorrect'] = 0
        
#         # print(f"Total answered correctly: {correct}")
#         # print(f"Total answered incorrectly: {incorrect}")
#         answer = input(f"\nwhat is the capital of {states[i]['name']}: ")

#         if answer == states[i]['capital']:
#             print(f'{answer} is correct')
#             states[i]['correct'] += 1
#             states[i]['answered'] += 1
#             correct += 1
#         elif answer != states[i]['capital']:
#             print(f"{answer} is incorrect the correct answer is {states[i]['capital']}")
#             states[i]['incorrect'] += 1
#             states[i]['answered'] += 1
#             incorrect += 1
#         print(F"Total Answered for {states[i]['name']}: {states[i]['answered']}\nCorrect for {states[i]['name']}: {states[i]['correct']}\nIncorrect for {states[i]['name']}: {states[i]['incorrect']}")

#         if states[i] == states[-1]:
#             answer = input('would you like to start again\n\nenter quit if no: ')              

new_list = [{
    "name": "Delaware",
    "capital": "Dover",
}, {
    "name": "Florida",
    "capital": "Tallahassee",
}, {
    "name": "Georgia",
    "capital": "Atlanta",
}]

for i in range(len(new_list)):
    new_list[i]['correct'] = 0
    new_list[i]['incorrect'] = 0
    new_list[i]['answered'] = 0



random.shuffle(new_list)

while answer != 'quit':
    for i in range(len(new_list)):   
        # new_list[i]['correct'] = 0
        # new_list[i]['incorrect'] = 0
        
        # print(f"Total answered correctly: {correct}")
        # print(f"Total answered incorrectly: {incorrect}")
        answer = input(f"\nwhat is the capital of {new_list[i]['name']}: ")

        if answer == new_list[i]['capital']:
            print(f'{answer} is correct')
            new_list[i]['correct'] += 1
            new_list[i]['answered'] += 1
            correct += 1
        elif answer != new_list[i]['capital']:
            print(f"{answer} is incorrect the correct answer is {new_list[i]['capital']}")
            new_list[i]['incorrect'] += 1
            new_list[i]['answered'] += 1
            incorrect += 1
        print(F"Total Answered for {new_list[i]['name']}: {new_list[i]['answered']}\nCorrect for {new_list[i]['name']}: {new_list[i]['correct']}\nIncorrect for {new_list[i]['name']}: {new_list[i]['incorrect']}")

        if new_list[i] == new_list[-1]:
            answer = input('would you like to start again\n\nenter quit if no: ')      
              