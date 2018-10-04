# -*- Utf-8 -*-

"""

"""
import random
import numpy

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'

ladders = [(1, 40), (8, 10), (36, 52), (43, 62), (49, 79), (65, 82), (68, 85)]
chutes = [(24, 5), (33, 3), (42, 30), (56, 37), (64, 27), (74, 12), (87, 70)]


def single_game(num_players):
    """
    Returns duration of single game.

    :param num_players: number of players in game
    :return: number of moves the winning player needed to reach the goal
    """
    players = [{'player_no': number,
                'current_position': 0,
                'position_hist': [0]}
               for number in range(num_players)]
    winning = None
    while True:
        for player in range(num_players):
            dice = random.randint(1, 6)
            players[player]['current_position'] += dice
            # Increments 'current position
            for chute in chutes:
                if players[player]['current_position'] == chute[0]:
                    players[player]['current_position'] = chute[1]
            for ladder in ladders:
                if players[player]['current_position'] == ladder[0]:
                    players[player]['current_position'] = ladder[1]
            players[player]['position_hist'].append(players[player]
                                                    ['current_position'])
            current_pos = players[player]['current_position']
            if current_pos >= 90:
                winning = len(players[player]['position_hist'])
                break
        if winning is not None:
            break
    return winning


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    :param num_games: number of games to play
    :param num_players: number of players in each game
    :return: sequence with number of moves needed in each game
    """
    return [(single_game(num_players)) for _ in range(num_games)]


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    :param num_games: number of games to play
    :param num_players: number of players in each game
    :param seed: random number seed for experiment
    :return: sequence with number of moves needed in each game
    """
    random.seed(seed)
    return multiple_games(num_games, num_players)  # (total_sequence of moves)


if __name__ == '__main__':
    result = multi_game_experiment(100, 4, 31415)
    printable = {'Max': max(result),
                 'Min': min(result),
                 'Mean': numpy.mean(result),
                 'Standard deviation': round(numpy.std(result), 2),
                 'Median': numpy.median(result)}
    for a in printable:
        print '{:20}=> {}'.format(a, printable[a])
