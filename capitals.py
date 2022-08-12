import random
import math

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

capitals_stub = [
    {
        "name": "Virginia",
        "capital": "Richmond"
    }, {
        "name": "Washington",
        "capital": "Olympia"
    }, {
        "name": "West Virginia",
        "capital": "Charleston"
    }
]

class Question():
    def __init__(self, state):
        self.state = state
        self.correct_history = 0
        self.wrong_history = 0
    def __str__(self):
        return f'this is a question pertaining to {self.state["capital"]}, {self.state["name"]}. It has been answered correctly {self.correct_history} times and incorrectly {self.wrong_history} times.'
    def ask_the_question(self):
        answer = input(f'What is the capital of {self.state["name"]}?\n')
        if answer.lower() == self.state["capital"].lower():
            self.correct_history += 1
            return True
        else:
            self.wrong_history += 1
            return False

def sort_questions(question):
    return question.wrong_history

def guessing_game():
    question_list = []
    for state in states:
        question_list.append(Question(state))
    random.shuffle(question_list)
    rounds_played = 1
    play_again = 'y'
    while play_again == 'y':
        correct_answers = 0
        wrong_answers = 0
        if rounds_played > 1:
            question_list.sort(reverse=True, key=sort_questions)
        print("Welcome to Guess the Capitals!")
        print("You will be given the name of a state, one at a time.")
        print("Simply type the name of the capital of that state.")
        print("You'll see if you got it right immediately!")
        print(f'Round {rounds_played}! Let\'s go!')
        for question in question_list:
            ask = question.ask_the_question()
            if ask == True:
                correct_answers += 1
                print('Correct!')
                print(f'You\'ve answered that question {question.correct_history} times correctly and {question.wrong_history} times incorrectly in the past.')
            else:
                wrong_answers += 1
                print('Sorry, that\'s not correct.')
                print(f'You\'ve answered that question {question.correct_history} times correctly and {question.wrong_history} times incorrectly in the past.')
        print('You made it to the end!')
        print(f'Correct answers: {correct_answers}')
        print(f'Incorrect answers: {wrong_answers}')
        play_again = input('Would you like to play again? Y/N\n')
        if play_again.lower() == 'y':
            rounds_played += 1
            continue
        elif play_again.lower() == 'n':
            print('Thanks for playing!')
            return
        else:
            print('Not sure what that means. Guess you\'re going again!')
            continue

guessing_game()