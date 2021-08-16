import tkinter as tk

class GridCanvas (tk.Canvas):
  GRID_DIV = [3, 3]
  ONE_SPACE_SIZE = 50

  def __init__ (self, master):
    super().__init__(master)
    self.master = master
    self.create_grids()
    self.pack()
    self.bind('<Button-1>', lambda event: self.handle_grid_click(self.convert_canvas_pos_to_grid_pos((event.x, event.y))))

  def create_grids (self):
    for y in range(self.GRID_DIV[0]):
      for x in range(self.GRID_DIV[1]):
        self.create_grid((x, y))

  def create_grid (self, xy):
    self.create_rectangle(
      *self.convert_grid_pos_to_canvas_start_pos(xy),
      *self.convert_grid_pos_to_canvas_end_pos(xy)
    )
  
  def handle_grid_click (self, xy):
    pass

  def convert_grid_pos_to_canvas_start_pos (self, xy):
    return (
      xy[0] * self.ONE_SPACE_SIZE,
      xy[1] * self.ONE_SPACE_SIZE
    )
  
  def convert_grid_pos_to_canvas_end_pos (self, xy):
    return (
      (xy[0] + 1) * self.ONE_SPACE_SIZE,
      (xy[1] + 1) * self.ONE_SPACE_SIZE
    )
  
  def convert_canvas_pos_to_grid_pos (self, xy):
    return (
      xy[0] // self.ONE_SPACE_SIZE,
      xy[1] // self.ONE_SPACE_SIZE
    )
