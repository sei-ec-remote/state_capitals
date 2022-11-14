#run this file to "play" the "game"

# from capitals import states
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
}
]


for state in states:
    state["wrong"] = 0
    state["correct"] = 0


print("Hello and welcome to the state capitals quiz game.")
yesOrNo = input("Would you like to play? y/n: ")

if yesOrNo.lower() == "y" or yesOrNo.lower() == "yes":
    print("Awesome!  Let's begin.\nFor each state, answer with the capital.\nIf you're stumped, type 'hint'.")


    random.shuffle(states)
    for state in states:
        answer = input(state["name"] + "?  ")
        if answer == "hint":
            answer = input(f'The first letter of the capital is {state["capital"][0]}.\n')
        if answer == "hint":
            answer = input(f'The first three letters of the capital are {state["capital"][0:3]}.\nNo more hints!  What is the capitol of {state["name"]}?\n')
        if answer == state["capital"]:
            print("That's right!")
            state["correct"] += 1
            print(f'You knew the capital of {state["name"]} {state["correct"]} out of {state["correct"] + state["wrong"]} times.')
        else:
            print("Oops, not quite.")
            state["wrong"] += 1
            print(f'You knew the capital of {state["name"]} {state["correct"]} out of {state["correct"] + state["wrong"]} times.')
    

    
    







elif yesOrNo.lower() == "n" or yesOrNo.lower() == "no":
    print("Nevermind, then.  Seeya!")
else:
    print("What the heck does that mean?\nStart over, but answer yes or no.\nGoodbye.")