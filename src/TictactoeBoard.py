from GridCanvas import GridCanvas
import numpy as np
from Player import WHITE_PLAYER_CODE, BLACK_PLAYER_CODE

class TictactoeBoard (GridCanvas):
  def __init__ (self, master):
    super().__init__(master)

  def draw_stones (self, state):
    for y in range(3):
      for x in range(3):
        if state[y][x] == BLACK_PLAYER_CODE:
          self.draw_black_stone((x, y))
        elif state[y][x] == WHITE_PLAYER_CODE:
          self.draw_white_stone((x, y))
    
  def draw_white_stone (self, xy):
    self.create_oval(
      *self.convert_grid_pos_to_canvas_start_pos(xy),
      *self.convert_grid_pos_to_canvas_end_pos(xy),
      fill='white'
    )
  
  def draw_black_stone (self, xy):
    self.create_oval(
      *self.convert_grid_pos_to_canvas_start_pos(xy),
      *self.convert_grid_pos_to_canvas_end_pos(xy),
      fill='black'
    )