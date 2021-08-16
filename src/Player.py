import numpy as np

# state[y][x]: 0 -> no, 1 -> white, 2 -> black
# PLAYER_CODE: 1 -> white, 2 -> black

WHITE_PLAYER_CODE = 1
BLACK_PLAYER_CODE = 2

class Player:
  def __init__ (self, PLAYER_CODE, eps=0.5):
    self.eps = eps

    self.PLAYER_CODE = PLAYER_CODE
    self.q_table = np.zeros((3 ** 9, 3, 3), dtype=np.float64)

  def play_one_step (self, state):
    action = self.select_action(state)
    return self.get_state_after_action(state, action)

  def get_state_after_action (self, state, action):
    ret = np.array(state)
    ret[action[1]][action[0]] = self.PLAYER_CODE
    return ret

  def select_action (self, state):
    action_possible = self.get_action_possible(state)
    argmax = self.get_optimal_idx_from_action_list(state, action_possible)
    probability = np.array([1 - self.eps + self.eps / len(action_possible) if argmax == idx else self.eps / len(action_possible) for idx, value in enumerate(action_possible)])
    return action_possible[np.random.choice(len(action_possible), 1, p=probability)[0]]

  def get_action_possible (self, state):
    action_possible = []
    for y in range(3):
      for x in range(3):
        if state[y][x] == 0:
          action_possible.append((x, y))

    return action_possible

  def get_optimal_idx_from_action_list (self, state, action_list):
    return np.argmax(np.array([self.q_table[self.convert_state_to_number(state)][action[1]][action[0]] for action in action_list]))

  def convert_state_to_number (self, state):
    ret = 0
    for y in range(3):
      for x in range(3):
        ret += state[y][x] * (3 ** self.convert_pos_to_idx((x, y)))
    
    return ret
    
  def convert_pos_to_idx (self, xy):
    return xy[0] + xy[1] * 3
