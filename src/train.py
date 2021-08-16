from GameLearn import GameLearn
from Learner import Learner
from Player import WHITE_PLAYER_CODE, BLACK_PLAYER_CODE
import numpy as np

game = GameLearn(Learner(WHITE_PLAYER_CODE), Learner(BLACK_PLAYER_CODE))

for i in range(10000):
  if i % 1000 == 0:
    print(i)
  game.init()
  game.learn_game()

np.save('white_q_table.npy', game.white_learner.q_table)
np.save('black_q_table.npy', game.black_learner.q_table)
