# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:03:30 2020

@author: Sebastian Franzén
"""
import random
import matplotlib.pyplot as plt

# the function returns strategy one or two
def chose_strategy(n):
    '''
    Returns the function that is the chosen strategy
    '''
    if n == 1:
        return strategy_1
    elif n == 2:
        return strategy_2
    # SHOULD WE MAKE AN EXEPTION IF n IS DIFFERENT FROM 1 AND 2??    


def strategy_1(houses):
    '''
    Takes a list and randomly returns the index of one of the strictly 
    positive elements.
    '''
    # gets the indeces of nonzero houses
    nonempty_ind = [i for i, e in enumerate(houses) if e > 0]
    
    # SHOULD WE BUILD IN AN EXCEPTION IF LENGTH OF  nonempty_ind IS ZERO???
    
    # if we only have got one strictly positive element we return that index.
    if len(nonempty_ind) == 1:
        return nonempty_ind[0]
    
    # picks randomly a nonempty house index
    elif len(nonempty_ind) > 1:
        rand_index = nonempty_ind[random.randint(0, sum([x > 0 for x in houses]) - 1)]
    
        return rand_index
    

# code strategy 2
def strategy_2(houses):
    '''
    Returns the index of the greatest element of a list. If the greatest
    element isn't unique, it is chosen randomly, with uniform distribution,
    from the greatest elements.
    '''

    # list of indeces of houses with number of bins equal to max_bin
    ind_of_max_elem = [i for i,e in enumerate(houses) if e == max(houses)]
    
    if len(ind_of_max_elem) == 1:
        return ind_of_max_elem[0]
    elif len(ind_of_max_elem) > 1:
        rand_index = ind_of_max_elem[random.randint(0,len(ind_of_max_elem) - 1)]
        return rand_index


class kalaha_player():
    '''
    A class of kalaha players. Each instance of which contains the method of
    the players strategy and number of seeds in end zone
    '''
    def __init__(self, strategy):
        self.end_zone = 0
        self.strategy = chose_strategy(strategy)
        

def one_turn_of_kalaha(strategy, own_houses, opponent_houses, end_zone):
    '''
    function that simulates one turn of kalaha.
    '''
    # picks house to draw seeds from, and draws the seeds
    house = strategy(own_houses)
    seeds = own_houses[house]
    own_houses[house] = 0
    # player_1 starts putting a seed in the next house
    house += 1
    
    while seeds > 0:
        
        while house <= 5 and seeds > 0:
            own_houses[house] += 1
            seeds -= 1
            house += 1
        
        if seeds == 0:
            return own_houses, opponent_houses, end_zone, 1
        
        elif seeds == 1:
            end_zone += 1
            seeds -= 1
            # if player one puts the last seed in his end_zone he gets an other move
            #we return a zero to know if the player gets an other move
            return own_houses, opponent_houses, end_zone, 0
        
        elif seeds >= 1:
            end_zone += 1
            seeds -= 1
        
        # we now continuou on the opposite players side
        house = 0
        
        while house <= 5 and seeds > 0:
            opponent_houses[house] += 1
            seeds -= 1
            house += 1
            
        if seeds == 0:
            #player_1 turn is over
            return own_houses, opponent_houses, end_zone, 1
            
        house = 0    


       
# the following program simulates one instance of the game
def play_kalaha(number_of_seeds, strategy_1, strategy_2):
    '''
    The function simulates a game of kalaha by for each players turn calling
    the function one_turn_of_kalaha
    '''
    player_1 = kalaha_player(strategy_1)
    player_2 = kalaha_player(strategy_2)
    houses_1 = [number_of_seeds] * 6
    houses_2 = [number_of_seeds] * 6
    turn = 1
    
    # we play as long as no player has all empty houses
    while min(sum(houses_1), sum(houses_2)) > 0:
          
        # if turn is uneven player_1 makes his move
        if turn % 2 != 0:
            houses_1, houses_2, player_1.end_zone, extra = one_turn_of_kalaha(
                                            player_1.strategy,
                                            houses_1,
                                            houses_2,
                                            player_1.end_zone)
            turn += extra
        
        elif turn % 2 == 0:
            houses_2, houses_1, player_2.end_zone, extra = one_turn_of_kalaha(
                                            player_2.strategy,
                                            houses_2,
                                            houses_1,
                                            player_2.end_zone)
            turn += extra
    
    if min(houses_1) == 0:
        player_2.end_zone += sum(houses_2)
        
    elif min(houses_2) == 0:
        player_1.end_zone += sum(houses_1)
    
    #if player_1 wins we return zero
    if player_1.end_zone > player_2.end_zone:
        return 0, player_1.end_zone, player_2.end_zone, turn
    
    # if player_2 wins we return 1
    elif player_2.end_zone > player_1.end_zone:
        return 1, player_1.end_zone, player_2.end_zone, turn
    
    # if draw we return 2
    else:
        return 2, player_1.end_zone, player_2.end_zone, turn


if __name__ == "__main__":
    
    statement = 'y'
    
    while statement == 'y':
        
        pl_1_strategy = int(input('Chose strategy for player 1: '))
        pl_2_strategy = int(input('Chose strategy for player: 2 '))
        seeds = int(input('Chose number of seeds: '))
        simulations = int(input('Chose number of simulations to run: '))
        
        results = []
        
        # simulate 200 games
        for i in range(simulations):
            results.append(play_kalaha(seeds, pl_1_strategy, pl_2_strategy)[0])
            i += 1
        
        # We prepare a barplot by counting individual outcomes
        pl_1_wins = sum([x == 0 for x in results])
        pl_2_wins = sum([x == 1 for x in results])
        draws = sum([x == 2 for x in results])
        
        x_ticks_names = ['Player 1', 'Player 2', 'Draws']
        heights = [pl_1_wins, pl_2_wins, draws]
        
        plt.clf()
        plt.bar(range(3), heights)
        plt.xticks(range(3), x_ticks_names)
        
        plt.savefig('results.pdf')
        print(f'Player 1 won {pl_1_wins} times', f'Player 2 won {pl_2_wins} times', f'There were {draws} draws',
              'A histogram of the result is saved in the file "results.pdf"', sep = '\n')
        
        statement = input('Chose "y" to make an other simulation or enter to quit: ')


    