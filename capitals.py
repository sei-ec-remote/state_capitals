from random import*

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

short_state_list = [{
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

class GameSession():
    def __init__(self, questions_asked=0):
        self.questions_asked = questions_asked
        for state in short_state_list:
            state['correct'] = 0
            state['wrong'] = 0
        # random.shuffle(short_state_list)
        # print(randrange(0, len(short_state_list)))
        # print(short_state_list)
        print("Welcome to the State Capital Quiz Game!")
        print("We will give you the name of a state and you try to guess its capital city.")
        print("Good luck!")
    def ask_question(self):
        random_index = randrange(0, len(short_state_list))
        answer = input(f"State capital of {short_state_list[random_index]['name']} is:\n")
        if(answer == short_state_list[random_index]["capital"]):
            print("Correct!")
            short_state_list[random_index]['correct'] += 1
        else: 
            print("Wrong...")
            short_state_list[random_index]['wrong'] += 1
        correct = short_state_list[random_index]['correct']
        total = short_state_list[random_index]['correct'] + short_state_list[random_index]['wrong']
        print(f"You got the state of {short_state_list[random_index]['name']} right {correct}/{total} times")
        self.questions_asked += 1
        return
    def number_of_questions(self):
        return self.questions_asked



this_game = GameSession()

def play_game():
    this_game.ask_question()
    for state in short_state_list:
        if(state['correct'] == 0 and state['wrong'] == 0):
            play_game()
    
    # for i, state in enumerate(short_state_list):
    #     if((state['correct'] + state['wrong']) == 0):
    #         global number_of_states_quizzed_on += 1
    #         continue
    #     else:
    #         global number_of_states_quizzed_on = i
    #         break
    # if(len(short_state_list) < this_game.number_of_questions()):
    play_again = input("Want to play again?\n")

    if(play_again.lower() == 'no'):
        print("Thanks for playing!")
    elif(play_again.lower() == 'yes'):
        this_game
        play_game()

# if(number_of_states_quizzed_on < len(short_state_list)):
#     play_game()
play_game()

    
# print(len(short_state_list))
# print(this_game.number_of_questions())


# if(len(short_state_list) > number_of_states_quizzed_on):
#     play_again = input("Want to play again?")
#     if(play_again.lower() == 'no'):
#         print("Thanks for playing!")
#     else:
#         this_game = GameSession()
#         play_game()
# else:
#     print("keep on playing..")
#     play_game()
# random.shuffle(short_state_list)
# this_game.ask_question()



