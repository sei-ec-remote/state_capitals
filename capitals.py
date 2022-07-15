import random
from states_data import states

class Game():

    def __init__(self,states):
        self.statesArr = states
        self.states = self.statesArr[:]
        self.right = 0
        self.total = 0
        print("Welcome to the state capitol naming game!")
        self.game_round()

    def game_round(self):
        round_state = self.states.pop(random.randint(0,len(self.states)-1))
        resp = input(f"What is the capitol of {round_state['name']}? Or type 'quit' to exit.\n").lower()
        self.total += 1
        if resp == 'quit':
            return
        elif resp == round_state['capital'].lower():
            print(f"WOW! EXCELLENT. YOU ARE SPECTACULAR!")
            self.right += 1
            self.display_points()
        else:
            print(f"Incorrect. I really think you need to study more... How could you miss this one! It's sooooooooo easy! It's {round_state['capital']}")
            self.display_points()

        #print(f"remaining states are {self.states}")

        if self.states:
            self.game_round()
        else:
            cont = input("Would you like to continue? y/n\n").lower()
            if cont == 'y':
                self.states = self.statesArr[:]
                self.game_round()
            else:
                return


    
    def display_points(self):
        print(f"You've scored {self.right} out of {self.total} attempts.")
        if self.right/self.total < 0.7:
            print(f"I think you need to study your capitols a bit more. Keep trying!")
        else:
            print(f"You're doing great! Nice score. Keep going.")

gameTIIIIMMMMMEEEE = Game(states)


