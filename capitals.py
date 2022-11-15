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
import random
states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
    }, {
    "name": "Massachusetts",
    "capital": "Boston"
    }, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

# randomize the order of states
# print(states)
# welcome message

#  initialize new keys in the dictionaries that store the number of times a user gets a capital correct  and the number of times the answer is wrong


# state_list=(states.keys())
# def question(state):
#  loop through and display a state
# through all 50 states, prompt the user to name the capital of the state
random.shuffle(states)
def play(states):
    welcome_message = 'Welcome! It is time to play the State Capital game.'
    print(welcome_message)
    right = 0
    wrong = 0 
    for i in range(3):
        capital = states[i]['capital']
        # start question function
        question_state = ('What is the capital of: ' + states[i]['name'])
        print(question_state)
    #  recieve response
        answer = input('Please type your response in lowercase: ').lower()
    # if the answer is correct display a message saying so and increment the correct key
        if (answer == states[i]['capital'].lower()):
            right += 1
            print('correct!', 'you got ', right,' correct and' ,wrong, 'incorrect' )

    # if the answer is wrong, display a message saying so and increment the wrong key
        else: 
            wrong += 1
            print('sorry the answer is', capital, 'you got ', right,' correct and' ,wrong, 'incorrect')
play(states)


question = input('Would you like to play again? yes/no ')
if (question == 'yes'):
    play(states)
else: 
    print('Thanks for playing')
# print('you got ', right,' correct and' ,wrong, 'incorrect')


# after wach prompt display a message telling the reader how many times the state was answered correctly 
# after wach prompt display a message telling the reader how many times the state was answered correctly out of the total number of times answered


# after all 50 states answered ask if they would like to play again


