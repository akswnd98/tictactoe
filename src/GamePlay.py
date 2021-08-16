import numpy as np
from Player import BLACK_PLAYER_CODE, WHITE_PLAYER_CODE

class GamePlay:
  def __init__ (self, white_player, black_player):
    self.white_player = white_player
    self.black_player = black_player
    self.state = np.zeros((3, 3), dtype=np.int64)
    self.cur_turn = 'black'

  def init (self):
    self.state = np.zeros((3, 3), dtype=np.int64)
    self.cur_turn = 'black'

  def do_game (self):
    while not self.check_is_over():
      if self.cur_turn == 'black':
        self.state = self.black_player.play_one_step(self.state)
      else:
        self.state = self.white_player.play_one_step(self.state)

  def check_is_over (self):
    return self.check_is_draw() or self.check_is_win(BLACK_PLAYER_CODE) or self.check_is_win(WHITE_PLAYER_CODE)

  def check_is_draw (self):
    is_full = True
    for y in range(3):
      for x in range(3):
        is_full = is_full and (self.state[y][x] != 0)

    return is_full and not self.check_is_win(BLACK_PLAYER_CODE) and not self.check_is_win(WHITE_PLAYER_CODE)

  def check_is_win (self, PLAYER_CODE):
    return self.check_is_vertical_win(PLAYER_CODE) or \
      self.check_is_horizontal_win(PLAYER_CODE) or \
        self.check_is_diagonal_win(PLAYER_CODE)
  
  def check_is_vertical_win (self, PLAYER_CODE):
    for x in range(3):
      is_over = True
      for y in range(3):
        is_over = is_over and (self.state[y][x] == PLAYER_CODE)
      if is_over:
        return True
    return False
  
  def check_is_horizontal_win (self, PLAYER_CODE):
    for y in range(3):
      is_over = True
      for x in range(3):
        is_over = is_over and (self.state[y][x] == PLAYER_CODE)
      if is_over:
        return True
    return False
  
  def check_is_diagonal_win (self, PLAYER_CODE):
    return (self.state[0][0] == PLAYER_CODE and self.state[1][1] == PLAYER_CODE and self.state[2][2] == PLAYER_CODE) or \
      (self.state[2][0] == PLAYER_CODE and self.state[1][1] == PLAYER_CODE and self.state[0][2] == PLAYER_CODE)

