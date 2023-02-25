from capitals import states
import random, json

class StateCapitalsGame():
    def __init__(self):
        """Initializes the game class"""
        self.score = {"win": 0, "loss": 0, "percentage": 0, "incorrect": []}
        self.game_record = {}
        self.answered = []
        # Copy the states list
        self.questions = states.copy()
        self.name = ''
        self.active = False
        self.round = 0

    def start_game(self):
        """Welcomes player and proceeds to the first round"""
        print(f"Welcome to the State Capitals Game!")
        # Get player name for personalized messages
        self.name = input(f"Please enter your name: ")
        print(f"Wonderful, now we can get to know each other a little better, {self.name}!")
        # Ask player if they are ready to start
        start = input(f"Now, when I give you a State, you must type in the capital on the next line (or type hint if you need a little help!)! \nReady, {self.name}? (y/n)\n")
        if start in 'Yy':
            # Set gameplay state to true and start game loop
            self.active = True
            self.gameplay()
        else:
            exit()
    
    def gameplay(self): 
        """Creates game loop"""
        # Reset game statistics
        self.reset_between_games()
        while self.active: 
            #Retrieve a question
            question = self.get_state()
            state = question["name"]
            capital = question["capital"]
            #Ask player
            answer = input(f"\nThe capital of {state} is...\n")
            #Check if player wants hint
            if answer.lower() == "hint":
                answer = input(f"Hint: {capital[:3]}\n")
            #Normalize & Check answer against correct capital
            if answer.lower() == capital.lower():
                self.score_answer("win")
            else:
                # Create a temporary response object
                response = {}
                print("capital", capital)
                self.score_answer("loss")
                response["state"] = state
                # Create a hint based on the round & add to game record
                response["capital_hint"] = capital[:(self.round)] or capital
                response["player_response"] = answer
                # Push response into the array
                self.game_record[self.round]["incorrect"].append(response)
            self.check_win()

    def reset_between_games(self):
        """Resets statistics in between rounds"""
        self.round += 1
        self.questions = states.copy()
        self.score = {"win": 0, "loss": 0, "percentage": 0, "incorrect": []}
        self.game_record[self.round] = self.score

    def get_state(self):
        """Get a random state from the states list"""
        question_num = random.randint(0, len(self.questions)-1)
        # Remove it from the questions array
        question = self.questions.pop(question_num)
        # Append it to the answered array
        self.answered.append(question)
        return question
    
    def score_answer(self, result):
        """Score the game after each question and check if all questions have been answered"""
        # Tally & message appropriate result
        if result == "win":
            self.score["win"] += 1
            print("\nHuzzah!")
        else:
            self.score["loss"] += 1
            print("\nOh No!")

    def check_win(self):
        wins = self.game_record[self.round]["win"]
        losses = self.game_record[self.round]["loss"]
        # Calculate how many rounds have been played and win %
        num_rounds = wins + losses
        win_percent = wins/num_rounds
        win_percent = int(win_percent*100)
        self.game_record[self.round]["percentage"] = win_percent
        #Print appropriate message if user completes game or continues to next question
        if len(self.questions) == 0:
            print(f"\nGame Over!\nNice work {self.name}, you answered {wins} correctly!")
            print(f"---That's {win_percent}% correct!---")
            self.active = False
            self.ask_next()
        else:
            print(f"Current score is {wins} wins : {losses} losses, for {win_percent}% overall")

    def ask_next(self):
        """Presents a menu after each game to ask player what they would like to do next"""
        # Set menu state to active
        menu = True
        while menu:
            print(f"\nWell done, {self.name}!\nWould you like to:")
            play_again = input("1) Play Again,\n2) See Prior Games\n3) Leave\n")
            if play_again == "1":
                # Restart game
                self.active = True
                menu = False
                self.gameplay()
            elif play_again == "2":
                pretty_record = json.dumps(self.game_record, indent=4)
                print(pretty_record)
            else:
                menu = False
                exit()

play_game = StateCapitalsGame()
play_game.start_game()