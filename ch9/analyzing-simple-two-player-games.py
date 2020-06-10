
import numpy as np
import nashpy as nash


you = np.array([[1, 3], [1, 4]])
colleague = np.array([[3, 2], [2, 2]])
dilemma = nash.Game(you, colleague)



print(dilemma[[1, 0], [1, 0]])  # [1 3]
print(dilemma[[1, 0], [0, 1]])  # [3 2]
print(dilemma[[0, 1], [1, 0]])  # [1 2]
print(dilemma[[0, 1], [0, 1]])  # [4 2]


print(dilemma[[0.1, 0.9], [0.5, 0.5]])  # [2.45 2.05]