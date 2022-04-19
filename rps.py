import random

# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
wins = {'player_one_score': 0, 'player_two_score': 0}


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, their_move):
        pass


"""The Human Player class is a subclass for the Players class"""


class HumanPlayer(Player):
    def move(self):
        self.player_choice = validate_input(
             "Rock, Paper, Scissors? > \n", moves)
        if self.player_choice in moves:
            play_response('You played', self.player_choice)
        return self.player_choice


# The Random Player class is a subclass for the Players class
class RandomPlayer(Player):
    def move(self):
        choice = random.choice(moves)
        self.random_choice = choice
        play_response('Opponent played', self.random_choice)
        return self.random_choice


"""The Reflect Player class is a subclass for the Players class"""


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()

        self.reflect_move = ''

    def move(self):
        if self.reflect_move == '':
            self.their_move = random.choice(moves)
            play_response('Opponent played', self.their_move)
            return self.their_move
        else:
            self.my_move = self.reflect_move
            play_response('Opponent played', self.my_move)
            return self.my_move

    def learn(self, move1):
        self.reflect_move = move1


# The Cycle Player class is a subclass for the Players class
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

        self.next_move = ''

    def move(self):
        if self.next_move == '':
            self.their_move = random.choice(moves)
            play_response("Opponent played", self.their_move)
            return self.their_move
        else:
            next_move = moves[self.index]
            self.index = (self.index + 1) % len(moves)


class RockPlayer(Player):
    def move(self):
        choice = moves[0]
        self.random_choice = choice
        play_response('Opponent played', self.random_choice)
        return self.random_choice


# The Game class
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        score(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play_game(self):
        round = 1
        num = int(validate_round('How many rounds do you want to play?'))
        # num = int(input('How many rounds do you want to play?'))
        while round <= num:
            print(f"Round {round} --")
            round += 1
            self.play_round()
        return round


def validate_round(prompt):
    while True:
        try:
            option = input(prompt)
            if 0 < int(option) < 100:
                return option
        except (ValueError, TypeError):
            pass


def validate_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        elif option == 'quit':
            quit_game()


# Validates the winner
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Keeps note of winner
def score(move1, move2):
    if beats(move1, move2):
        wins['player_one_score'] += 1
        print(f'** PLAYER ONE WINS **')
        # return player_one_score

    elif beats(move2, move1):
        wins['player_two_score'] += 1
        print(f"** PLAYER TWO WINS **")
        # return player_two_score

    else:
        print('** DRAW **')

    print(f"Score: You {wins['player_one_score']},"
          f"Opponent {wins['player_two_score']}")


# function to give response of what each player played
def play_response(respond, player_move):
    print(f"{respond} {player_move}")


# Function that ends the game
def quit_game():
    print("Game over!")
    print('Thanks for playing! Goodbye!')
    exit(0)


# Function that begins the game
def game():
    print("Game start!")
    print('Rock Paper Scissors, Go! \n')

    # Infinite loop.
    while True:

        game = Game(HumanPlayer(), random.choice(
                    [ReflectPlayer(), RandomPlayer(),
                     CyclePlayer(), RockPlayer()]))
        game.play_game()


if __name__ == '__main__':
    game()
