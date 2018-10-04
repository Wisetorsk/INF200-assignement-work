# -*- Utf-8 -*-
import random

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Walker(object):
    
    def __init__(self, start, home, llim, rlim):
        self.position = start
        self.home = home
        self.llim = llim
        self.rlim = rlim
        self.steps = 0
        
    def am_i_home(self):
        return True if self.position == self.home else False
    
    def get_position(self):
        return self.position
    
    def move(self):
        if self.position == self.llim:
            self.position += 1
        elif self.position == self.rlim:
            self.position -= 1
        else:
            if random.randint(1, 2) == 1:
                self.position += 1
            else:
                self.position -= 1
        self.steps += 1


class Simulation(Walker):
    
    def __init__(self, start, home, llim, rlim, seed=None):
        super(Walker, self).__init__()
        self.start = start
        self.home = home
        self.seed = seed
        if llim > start or rlim < home:
            raise ValueError
        self.rlim = rlim
        self.llim = llim
        
    def single_walk(self):
        instance = Walker(self.start, self.home, self.llim, self.rlim)
        while not instance.am_i_home():
            instance.move()
        return instance.steps
    
    def run_simulation(self, walks):
        if self.seed is not None:
            random.seed(self.seed) 
        return [self.single_walk() for _ in range(walks)]


if __name__ == '__main__':
    Right_limit = 20
    Left_limits = [0, -10, -100, -1000, -100000]
    start_val = 0
    home_val = 20
    simulations = [Simulation(start_val, home_val, left, Right_limit)
                   for left in Left_limits]

    results = [sim.run_simulation(20) for sim in simulations]
    i = 0
    for res in results:
        print 'Walk 0 => 20 with left limit {}: {:100}'\
            .format(Left_limits[i], res)
        i += 1
