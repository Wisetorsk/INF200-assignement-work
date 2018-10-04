# -*- Utf-8 -*-
import random

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Walker(object):
    
    def __init__(self, start, home):
        self.position = start
        self.home = home
        self.steps = 0
        
    def am_i_home(self):
        return True if self.position == self.home else False
    
    def get_position(self):
        return self.position
    
    def move(self):
        if random.randint(1, 2) == 1:
            self.position += 1
        else:
            self.position -= 1
        self.steps += 1


class Simulation(Walker):
    
    def __init__(self, start, home, seed=None):
        super(Walker, self).__init__()
        self.start = start
        self.home = home
        self.seed = seed
        
    def single_walk(self):
        instance = Walker(self.start, self.home)
        while not instance.am_i_home():
            instance.move()
        return instance.steps
    
    def run_simulation(self, walks):
        if self.seed is not None:
            random.seed(self.seed) 
        return [self.single_walk() for _ in range(walks)]


if __name__ == '__main__':
    simulations = [Simulation(0, 10, 12345),
                   Simulation(0, 10, 12345),
                   Simulation(10, 0, 12345),
                   Simulation(10, 0, 12345),
                   Simulation(0, 10, 54321),
                   Simulation(10, 0, 54321), ]
    results = [sim.run_simulation(20) for sim in simulations]
    i = 0
    for res in results:
        print 'Walk {:2} => {:2} with seed {:5}: {:100}'\
            .format(simulations[i].start, simulations[i].home,
                    simulations[i].seed, res)
        i += 1
