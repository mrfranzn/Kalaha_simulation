# Kalaha_simulation

A simple simulation in Python of the board game Kalaha under two different strategies for the two players. The first strategy is to choose randomly which hose to sow the seeds from  (with equal probability assigned to each nonempty house). The second strategy is to sow from the house with the maximum number of seeds, and if there is more than one house with a maximum number of seeds, chose randomly among these houses. 

The program asks the user for input and prints the result of the simulation. A bar plot is also generated in the folder of the program. 

There are four inputs: 1) the strategy of player 1, 2) the strategy of player 2, 3) the number of seeds in each house, 4) the number of rounds that should be simulated. Player 1 always makes the first move. The strategies are given as either ‘1’ or ‘2’.  The number of seeds are customarily chosen to be 3-6, but any other positive integer is acceptable. 

The program utilizes the random and the matplotlib.pyplot packages.

The program is structured as follows: each strategy is a function that takes a list (with the number of seeds in that player's houses) and generates an index that is the house the player has chosen. Each player is represented by an instance of a class of players. The instance holds the number of seeds in the endzone of the player as an attribute, and the player's strategy as a method. Each turn of a player is represented by a function. One round is represented by a function that repeatedly calls the function for one turn. 
