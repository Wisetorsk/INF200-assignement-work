# -*- Utf-8 -*-
import random

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Gambler(object):
    def __init__(self, probability, money_total, m):
        self.probability = probability
        self.M = money_total
        self.m = m 
        self.bank = self.M - self.m
        self.turns = 0
        
    def coin_toss(self):
        return random.random() < self.probability
    
    def one_turn(self):
        if self.coin_toss():
            self.m += 1
        else:
            self.m -= 1
        self.turns += 1
        
    def game_over(self):
        if self.M - self.m == 0:
            return True
        elif self.m == 0:
            return True


class Simulation(Gambler):
    def __init__(self, probability, money_total, m, seed=None):
        super(Gambler, self).__init__()
        self.probability = probability
        self.M = money_total
        self.m = m
        self.seed = seed
        self.results = {'broke': [0, []], 'ruined': [0, []]}

    def one_game(self):
        instance = Gambler(self.probability, self.M, self.m)
        while not instance.game_over():
            instance.one_turn()
        if instance.M - instance.m == 0:
            self.results['broke'][0] += 1
            self.results['broke'][1].append(instance.turns)
        else:
            self.results['ruined'][0] += 1
            self.results['ruined'][1].append(instance.turns)   
            
    def run_simulation(self, games):
        if self.seed is not None:
            random.seed(self.seed)
        for _ in range(games):
            self.one_game()
        return self.results
        
if __name__ == '__main__':
    total = 100
    gambler = 25
    probabilities = [0.0, 0.1, 0.2, 0.4, 0.45, 0.49, 0.5, 0.9]
    simulations = [Simulation(p, total, gambler) for p in probabilities]
    results = [sim.run_simulation(20) for sim in simulations]
    i = 0
    print results
    for di in results:
        ruin_games = None if len(di['ruined'][1]) == 0 else di['ruined'][1]
        broke_games = None if len(di['broke'][1]) == 0 else di['broke'][0]
        print 'Probability {:4} Times Broke: {:2} Times Ruined: {:2} \nMoves' \
              ' resulting in Breaking the bank: {}\nMoves resulting in ruin:' \
              ' {}\n'.format(probabilities[i], di['broke'][0], di['ruined'][0],
                             ruin_games, di['broke'][1])
        i += 1
