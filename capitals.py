from random import shuffle


all_states = [
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


# Test dictionary for states
test_states = [
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
}]


# Setup the states dictionary for holding correct and wrong guesses for each
#   state.  This adds correct: 0 and wrong: 0 for each state in the states 
#   dictionary
for state in all_states:
    state["correct"] = 0
    state["wrong"] = 0

# Make sure the dictionary is setup correctly
#print(test_states)

# Function to execute the game and track the wins and losses (correct and wrongs)
def begin_game():
    # Shuffle the order of the states to make things harder
    shuffle(all_states)
    total_correct = 0

    for state in all_states:
        keep_guessing = True
        while keep_guessing:
            guess = input("\nPlease enter the Capital of " + state["name"] + "\n")
            # Make it case insensitive so not typing capital letters does not
            # make you lose
            if guess.casefold() == state["capital"].casefold():
                print("Amazing! That was a correct answer!")
                state["correct"] += 1
                total_correct += 1
                keep_guessing = False
            else:
                print("Sorry, that was incorrect.")
                state["wrong"] += 1
                yes_or_no = input("Would you like to try another guess? (yes or no) ")
                if yes_or_no.casefold() == 'no':
                    yes_or_no_hint = input("Would you like a hint to help? (yes or no) ")
                    if yes_or_no_hint == 'no':
                        keep_guessing = False
                    else:
                        capital = state["capital"]
                        name = state["name"]
                        print(f"Here is your Hint for {name}: {capital[0]}{capital[1]}{capital[2]}\n")
                        continue
                else: continue

        print("For {} your score is: ".format(state["name"]))
        print("     Correct: {}".format(state["correct"]))
        print("     Wrong: {} \n".format(state["wrong"]))

    print("\nTotal Score:  Out of 50 states you answered: {} correctly.".format(total_correct))


print("Let's learn our State Capitals! This game will help you memorize")
print("the names of the Capitals of all 50 States.")
begin_game()
