from GamePlay import GamePlay
from Player import Player
import numpy as np

class GameLearn (GamePlay):
  def __init__ (self, white_learner, black_learner):
    super().__init__(white_learner, black_learner)
    self.white_learner = white_learner
    self.black_learner = black_learner
    self.black_player_state_action_pair_backup = None
    self.white_player_state_action_pair_backup = None

  def init (self):
    super().init()
    self.black_player_state_action_pair_backup = None
    self.white_player_state_action_pair_backup = None

  def learn_game (self):
    while True:
      if self.cur_turn == 'black':
        self.black_player_state_action_pair_backup = (np.array(self.state), self.black_learner.select_action(self.state))
        self.state = self.black_learner.get_state_after_action(self.state, self.black_player_state_action_pair_backup[1])
        if self.check_is_over():
          break
        self.cur_turn = 'white'
        if self.white_player_state_action_pair_backup != None:
          self.white_learner.learn_one_step(*self.white_player_state_action_pair_backup, -0.01)
      else:
        self.white_player_state_action_pair_backup = (np.array(self.state), self.white_learner.select_action(self.state))
        self.state = self.white_learner.get_state_after_action(self.state, self.white_player_state_action_pair_backup[1])
        if self.check_is_over():
          break
        self.cur_turn = 'black'
        if self.black_player_state_action_pair_backup != None:
          self.black_learner.learn_one_step(*self.black_player_state_action_pair_backup, -0.01)

    if self.check_is_draw():
      if self.black_player_state_action_pair_backup != None:
        self.black_learner.learn_one_step_over(*self.black_player_state_action_pair_backup, 1)
      if self.white_player_state_action_pair_backup != None:
        self.white_learner.learn_one_step_over(*self.white_player_state_action_pair_backup, 1)
    else:
      if self.cur_turn == 'black':
        if self.black_player_state_action_pair_backup != None:
          self.black_learner.learn_one_step_over(*self.black_player_state_action_pair_backup, 1)
        if self.white_player_state_action_pair_backup != None:
          self.white_learner.learn_one_step_over(*self.white_player_state_action_pair_backup, -1)
      else:
        if self.white_player_state_action_pair_backup != None:
          self.white_learner.learn_one_step_over(*self.white_player_state_action_pair_backup, 1)
        if self.black_player_state_action_pair_backup != None:
          self.black_learner.learn_one_step_over(*self.black_player_state_action_pair_backup, -1)
  
  