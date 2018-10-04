# -*- coding: utf-8 -*-

"""
Chutes & Ladders: A fully object-oriented simulation setup.
"""

import random

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Board(object):
    """
    Represents game board.
    """

    def __init__(self, ladders=None, chutes=None, goal=90):
        """
        :param ladders: list of (start, end) tuples representing ladders
        :param chutes: list of (start, end) tuples representing chutes
        :param goal: destination square
        """
        if ladders is None:  # not necessary, but error if default argument
            self._ladders = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79),
                             (65, 82), (68, 85)]
        else:
            self._ladders = ladders
        if chutes is None:  # not necessary, but error if default argument
            self._chutes = [(24, 5), (33, 3), (42, 30), (56, 37),
                            (64, 27), (74, 12), (87, 70)]
        else:
            self._chutes = chutes
        if goal is None:  # not necessary, but error if default argument
            self._goal = 90
        else:
            self._goal = goal

    def goal_reached(self, player):
        """
        Returns True if player has reached goal.

        :param player: Player instance
        """
        return player._current_position >= self._goal

    def position_adjustment(self, position):
        """
        Return change to position due to chute or ladder.

        If the player is not at the start of a chute/ladder, it returns 0.

        :param position: Player position
        :returns: number of fields player must move to get to correct position
        """
        for pair in self._ladders + self._chutes:
            if pair[0] == position:
                return pair[1] - position
        return 0


class Player(object):
    """
    Implements single player.
    """

    def __init__(self, board):
        """
        :param board: board on which player is living
        """
        self._board = board
        self._current_position = 0
        self.moves = 0

    def move(self):
        """
        Moves player to new position.
        """
        dice = random.randint(1, 6)
        self._current_position += dice
        self._current_position += \
            self._board.position_adjustment(self._current_position)
        self.moves += 1


class ResilientPlayer(Player):
    """
    Implements a player who makes extra efforts after sliding down.

    At the step after sliding down a slide, this player moves
    extra_steps squares more than the result of the die cast
    at the next move.
    """

    def __init__(self, board, extra_steps=1):
        """
        :param extra_steps: number of extra steps on move after sliding down
        """
        super(Player, self).__init__()  # self, board
        self._current_position = 0
        self._board = board
        self._extra = extra_steps
        self.moves = 0

    def move(self):
        dice = random.randint(1, 6)
        self._current_position += dice
        before_chute = self._current_position
        self._current_position += \
            self._board.position_adjustment(self._current_position)
        after_chute = self._current_position
        if after_chute - before_chute < 0:
            self._current_position += self._extra


class LazyPlayer(Player):
    """
    Implements a player who makes a lesser effort after climbing up.

    At the step after climbing a slide, this player moves
    dropped_steps squares less than the result of the die cast
    at the next move (but never backward).
    """

    def __init__(self, board, dropped_steps=1):
        """
        :param dropped_steps: number of steps dropped after climbing up
        """
        super(Player, self).__init__()  # self, board
        self._dropped = dropped_steps
        self._board = board
        self.moves = 0
        self._current_position = 0

    def move(self):
        dice = random.randint(1, 6)
        self._current_position += dice
        before_ladder = self._current_position
        self._current_position += \
            self._board.position_adjustment(self._current_position)
        after_ladder = self._current_position
        if after_ladder - before_ladder > 0:
            self._current_position -= self._dropped


class Simulation(object):
    """
    Implements a complete Chutes & Ladders simulation.
    """

    def __init__(self, player_field, board=Board(), seed=1234567,
                 randomize_players=False):
        """
        :param player_field: list of player classes, one per player to use
        :param board: Board instance (default: standard board)
        :param seed: random generator seed
        :param randomize_players: randomize player order at start of game
        """
        self._seed = seed
        self._board = board
        self._randomize_players = randomize_players
        self._players = [pl(board) for pl in player_field]
        self._outcomes = {'LazyPlayer': {'wins': 0, 'moves': []},
                          'ResilientPlayer': {'wins': 0, 'moves': []},
                          'Player': {'wins': 0, 'moves': []}}

    def single_game(self):
        """
        Returns winner type and number of steps for single game.

        :returns: (number_of_steps, winner_class) tuple
        """
        if self._randomize_players:
            random.shuffle(self._players)

        while True:
            for player in self._players:
                player.move()
                if self._board.goal_reached(player):
                    a = (player.moves, player.__class__.__name__)
                    return a

    def run_simulation(self, num_games):
        """
        Run a set of games, store results in Simulation.

        If results exist from before, new data will be added to existing data.

        :param num_games: number of games to play
        """
        if self._seed is not None:
            random.seed(self._seed)

        for _ in range(num_games):
            outcome = self.single_game()
            self._outcomes[outcome[1]]['wins'] += 1
            self._outcomes[outcome[1]]['moves'].append(outcome[0])
        print self._outcomes

    def players_per_type(self):
        """
        Returns a dict mapping player classes to number of players.
        """
        out = {'LazyPlayer': 0, 'ResilientPlayer': 0, 'Player': 0}
        for p in self._players:
            out[p.__class__.__name__] += 1
        return out

    def winners_per_type(self):
        """
        Returns dict showing number of winners for each type of player.
        """
        out = {'LazyPlayer': 0, 'ResilientPlayer': 0, 'Player': 0}
        for p in out:
            out[p] = self._outcomes[p]['wins']
        return out

    def durations_per_type(self):
        """
        Returns dict mapping winner type to list of game durations for type.
        """
        out = {'LazyPlayer': 0, 'ResilientPlayer': 0, 'Player': 0}
        for p in out:
            out[p] = self._outcomes[p]['moves']
        return out


if __name__ == '__main__':
    # The following code should work (and print something else than None)

    print '**** First Simulation: Single player, standard board ****'
    sim = Simulation([Player])
    print sim.single_game()
    sim.run_simulation(10)
    print sim.players_per_type()
    print sim.winners_per_type()
    print sim.durations_per_type()

    print '\n**** Second Simulation: Four players, standard board ****'
    sim = Simulation([Player, Player, LazyPlayer, ResilientPlayer])
    print sim.single_game()
    sim.run_simulation(10)
    print sim.players_per_type()
    print sim.winners_per_type()
    print sim.durations_per_type()

    print '\n**** Third Simulation: Four players, small board ****'
    my_board = Board(ladders=[(3, 10), (5, 8)], chutes=[(9, 2)], goal=20)
    sim = Simulation([Player, Player, LazyPlayer, ResilientPlayer],
                     board=my_board)
    print sim.single_game()
    sim.run_simulation(10)
    print sim.players_per_type()
    print sim.winners_per_type()
    print sim.durations_per_type()
