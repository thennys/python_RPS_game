import random
import sys


class RPS:
    def __init__(self):
        print('welcome to Rock🪨, Paper📜, Scissors✂️')

        self.moves = {'rock': '🪨🪨🪨', 'paper': '📜📜📜', 'scissors': '✂️✂️✂️'}

        self.valid_moves = list(self.moves.keys())

    def play_game(self):
        user_move = input("Rock, Paper, Scissors").lower()
        
        if user_move == 'exit':
            print("Thanks for playing, see you soon")
            sys.exit()

        if user_move not in self.valid_moves:
            print('invalid moves...')
            return self.play_game()

        ai_move = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self,):
        ...
        
    def check_moves(self,):
        ...