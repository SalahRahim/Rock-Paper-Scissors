import random

rounds = input("Hom many rounds do you want to play?")


class Player:
    """A player that always plays 'rock'"""
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    """A player that chooses its moves randomly."""
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """Player number one"""
    def move(self):
        my_move = input("rock, paper, scissors?").lower()
        while my_move not in moves:
            my_move = input("rock, paper, scissors?").lower()
        return my_move


class ReflectPlayer(Player):
    """A player that remembers and imitates what the human player did in the previous round."""
    def __init__(self):
        """first move of ReflectPlayer is random"""
        self.reflect_move = random.choice(moves)

    def move(self):
        return self.reflect_move

    def learn(self, my_move, their_move):
        self.reflect_move = their_move
        return self.reflect_move


class CyclePlayer(Player):
    """A player that cycles through the three moves."""
    def __init__(self):
        self.cycle_move = random.choice(moves)

    def move(self):
        return self.cycle_move

    def learn(self, my_move, their_move):
        self.cycle_move = their_move
        if their_move == "rock":
            return "paper"
        elif their_move == "paper":
            return "scissors"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2) is True:
            self.p1_score += 1
            print("player one win")
            print(f"score:\n Player one: {self.p1_score} "
                  f"player two:{self.p2_score}\n")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print("player two win")
            print(f"Score:\n Player one: {self.p1_score} "
                  f"player two:{self.p2_score}\n")

        else:
            print("Oh, it's a tie.")
            print(f"Score:\n Player one: {self.p1_score} "
                  f"player two:{self.p2_score}\n")

    def play_game(self):
        print("Game start!")
        for round in range(int(rounds)):
            round += 1
            print(f"Round {round}--")
            self.play_round()
        self.final_score()
        print("Game over!\n")

    def final_score(self):
        if self.p1_score > self.p2_score:
            print(f"The champion is player one")
        elif self.p1_score < self.p2_score:
            print(f"The champion is player two")
        else:
            print("You both champions")



if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    behaviors = [RandomPlayer(), HumanPlayer(), ReflectPlayer(), CyclePlayer()]
    behavior = random.choice(behaviors)
    human = HumanPlayer()
    game = Game(human, behavior)
    game.play_game()
