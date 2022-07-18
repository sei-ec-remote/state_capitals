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

prompt = ''
state_answers = {}
test_states = [
    {'name': 'Oregon', 'capital': 'Salem'},
    {'name': 'Wyoming', 'capital': 'Cheyenne'},
    {'name': 'Vermont', 'capital': 'Montpelier'},
]

print('Welcome to my State Capitals Game!')
for i in range(len(test_states)):
    state_answers[test_states[i] ['name']] = {
        'right': 0, 'wrong': 0, 'number_answered': 0}

    while(prompt != 'n'):
        answers = {
            'correct_count': 0,
            'wrong_count': 0,
        }
        
        def correct(state):
            answers['correct_count'] += 1
            state_answers[f'{state}'] ['right']  += 1
            state_answers[f'{state}'] ['number_answered'] +=1

            def wrong(state):
                answers['wrong_count'] += 1
                state_answers[f'{state}'] ['wrong'] += 1
                state_answers[f'{state}'] ['number_answered'] += 1

                state_questions = []
                for i in range(len(test_states)) :
                    current_state = test_states[i] ['name']
                    current_capital = test_states[i] ['capital']
                    state_questions.append({'state': current_state, 'result': correct(current_state) or print(f"You are correct! Currently you have {scores['correct_count']} correct and {scores['wrong_count']} wrong. - You got this question right {state_scores[current_state]['right']} time(s) out of {state_scores[current_state]['num_answered']}") or True if str(input(
            f'What is the capital of {current_state}? [Hint:{current_capital[0:3]}]  :')).lower() == current_capital else wrong(current_state) or print(f"You are incorrect! Currently you have {scores['correct_count']} correct and {scores['wrong_count']} wrong. - You got this question right {state_scores[current_state]['right']} time(s) out of {state_scores[current_state]['num_answered']}")})

    print(f"Total correct answers: {scores['correct_count']}")
    print(f"Total Wrong answers: {scores['wrong_count']}")
    prompt = input('Do you wanna play again? Yes/No :')

