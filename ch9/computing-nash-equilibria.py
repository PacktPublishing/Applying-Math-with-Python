

import numpy as np
import nashpy as nash


rps_p1 = np.array([
    [ 0, -1,  1],  # rock payoff
    [ 1,  0, -1],  # papper payoff
    [-1,  1,  0]   # scissors payoff
])

rps_p2 = rps_p1.transpose()

rock_paper_scissors = nash.Game(rps_p1, rps_p2)

equilibria = rock_paper_scissors.support_enumeration()

for p1, p2 in equilibria:
    print("Player 1", p1)
    print("Player 2", p2)