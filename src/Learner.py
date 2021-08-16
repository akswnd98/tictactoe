from Player import Player
import numpy as np

class Learner (Player):
  def __init__ (self, PLAYER_CODE):
    super().__init__(PLAYER_CODE)
    self.gamma = 0.9
    self.learning_rate = 0.1

  def learn_one_step (self, state, action, reward):
    self.q_table[self.convert_state_to_number(state)][action[1]][action[0]] += \
      self.learning_rate * (self.get_target_q_value(state, action, reward) - self.get_cur_q_value(state, action))

  def learn_one_step_over (self, state, action, reward):
    self.q_table[self.convert_state_to_number(state)][action[1]][action[0]] += \
      self.learning_rate * (reward - self.get_cur_q_value(state, action))

  def get_cur_q_value (self, state, action):
    return self.q_table[self.convert_state_to_number(state)][action[1]][action[0]]

  def get_target_q_value (self, state, action, reward):
    new_state = self.get_state_after_action(state, action)
    optimal_action = self.get_optimal_action(new_state)
    return reward + self.gamma * (self.q_table[self.convert_state_to_number(new_state)][optimal_action[1]][optimal_action[0]])

  def get_optimal_action (self, state):
    action_list = self.get_action_possible(state)
    argmax = self.get_optimal_idx_from_action_list(state, action_list)
    return action_list[argmax]
