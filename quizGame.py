#run this file to "play" the "game"



from capitals import states
import random


# Create all-time tallies for each state
for state in states:
    state["wrong"] = 0
    state["correct"] = 0

# Count number of games played
times_played = 0


# a function that can be repeated for each game
def game_loop():
    # set/reset tallies for current game
    current_game = {"correct": 0, "wrong": 0}

    # increase count of times played
    global times_played
    times_played += 1

    # randomize prompt order
    random.shuffle(states)

    # when game is being played extra times, sort prompts to start with ones answered wrong the most, also print message that game is starting again
    if times_played > 1:
        states.sort(key=lambda state: state["wrong"], reverse=True)
        print(f'Starting game {times_played}...')

    # for each state, prompt with state name
    for state in states:
        answer = input(f'\n{state["name"]}?\n')

        # accept "hint" as an answer three times, giving hints the first two times
        if answer == "hint":
            answer = input(f'The first letter of the capital is {state["capital"][0]}.  {state["name"]}?\n')
        if answer == "hint":
            answer = input(f'The first three letters of the capital are {state["capital"][0:3]}.  {state["name"]}?\n')
        if answer == "hint":
            answer = input(f'No more hints!  What is the capital of {state["name"]}?\n')

        # if correct, add to correct tallies and give current tallies (only show all-game tallies after first time)
        if answer == state["capital"]:
            print("\nThat's right!\n")
            state["correct"] += 1
            if times_played > 1:
                print(f'You knew the capital of {state["name"]} {state["correct"]} out of {state["correct"] + state["wrong"]} times.')
            current_game["correct"] += 1
            print(f'So far this game: {current_game["correct"]} right answers and {current_game["wrong"]} wrong answers')
        
        # if incorrect, add to wrong tallies
        else:
            print(f'\nOops, not quite.\nThe capital of {state["name"]} is {state["capital"]}.')
            state["wrong"] += 1
            if times_played > 1:
                print(f'You knew the capital of {state["name"]} {state["correct"]} out of {state["correct"] + state["wrong"]} times.')
            current_game["wrong"] += 1
            print(f'So far this game: {current_game["correct"]} right and {current_game["wrong"]} wrong answers')

    # When all states have been completed, give total and prompt for new game
    print(f'\nThat\'s it!\nOut of {len(states)} states, you got {current_game["correct"]} capitals right.')
    again = input("\nPlay again?\ny/n:  ")
    if again.lower() == "y" or  again.lower() == "yes":
        game_loop()
    else:
        average_correct = sum(state["correct"] for state in states) // times_played
        print(f"Thanks for playing!\nOn average you got {average_correct} capitals correct.\nGoodbye!")



# Here is where the terminal prompts start
print("Hello and welcome to the state capitals quiz game.")
yes_or_no = input("Would you like to play?\ny/n: ")

if yes_or_no.lower() == "y" or yes_or_no.lower() == "yes":
    print("\nAwesome!  Let's begin.\nFor each state, answer with the capital.\nIf you're stumped, type 'hint'.")    

    # run game loop for the first time
    game_loop()

# If user doesn't say they want to play
elif yes_or_no.lower() == "n" or yes_or_no.lower() == "no":
    print("Nevermind, then.  Seeya!")
else:
    print("What the heck does that mean?\nStart over, but answer yes or no.\nGoodbye.")