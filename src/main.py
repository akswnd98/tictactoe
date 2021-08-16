from Player import Player, WHITE_PLAYER_CODE, BLACK_PLAYER_CODE
from TictactoeBoard import TictactoeBoard
import tkinter as tk
import numpy as np

class Application (tk.Frame):
  def __init__ (self, master=None):
    super().__init__(master)
    self.master = master
    self.create_widgets()
    self.pack()
    self.state = np.zeros((3, 3), np.int64)
    self.black_player = Player(BLACK_PLAYER_CODE, 0)
    self.black_player.q_table = np.load('./black_q_table.npy')
    self.state = self.black_player.play_one_step(self.state)
    self.tictactoe_board.draw_stones(self.state)
  
  def create_widgets (self):
    self.tictactoe_board = TictactoeBoard(self)
    self.tictactoe_board.handle_grid_click = self.handle_click
    self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
    self.quit.pack()

  def handle_click (self, xy):
    self.state = self.get_state_after_action(self.state, xy)
    self.state = self.black_player.play_one_step(self.state)
    self.tictactoe_board.draw_stones(self.state)
  
  def get_state_after_action (self, state, action):
    ret = np.array(state)
    ret[action[1]][action[0]] = WHITE_PLAYER_CODE
    return ret

root = tk.Tk()
app = Application(master=root)
app.mainloop()
