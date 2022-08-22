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

class GameSession():
    def __init__(self):
        # self.questions_asked = questions_asked
        for state in states:
            state['correct'] = 0
            state['wrong'] = 0
        # random.shuffle(short_state_list)
        # print(randrange(0, len(short_state_list)))
        # print(short_state_list)
        print("Welcome to the State Capital Quiz Game!")
        print("We will give you the name of a state and you try to guess its capital city.")
        print("Good luck!")
        self.ask_question()
    def ask_question(self):
        random_index = randrange(0, len(states))
        answer = input(f"State capital of {states[random_index]['name']} is:\n")
        if(answer == states[random_index]["capital"]):
            print("Correct!")
            states[random_index]['correct'] += 1
        else: 
            print("Wrong...")
            states[random_index]['wrong'] += 1
        correct = states[random_index]['correct']
        total = states[random_index]['correct'] + states[random_index]['wrong']
        print(f"You got the state of {states[random_index]['name']} right {correct}/{total} times")
        # self.questions_asked += 1
        quiz_user_on = filter(self.left_to_be_quizzed_on, states)
        list_to_be_quizzed_on = len(list(quiz_user_on))
        # print(list_to_be_quizzed_on)
        if(list_to_be_quizzed_on > 0):
            self.ask_question()
        else:
            self.play_again()
    def play_again(self):
        print("You have been quizzed on all our states!")
        play_again = input("Want to play again?\n")
        if(play_again.lower() == 'no'):
            # print('Thanks for playing!')
            stop_game()
            # stop_game()
        else:
            # this_game_number = this_game_number + 1
            # games_played = this_game_number
            this_game = GameSession()
    def left_to_be_quizzed_on(self, item):
        # to_be_asked = list(filter(lambda item: short_state_list['correct'] == 0 and short_state_list['wrong'] == 0, short_state_list))
        # print(to_be_asked)
        if(item['correct'] == 0 and item['wrong'] == 0):
            return True
        else:
            return False
    

def stop_game():
    print('Thanks for playing!')
  
this_game = GameSession()