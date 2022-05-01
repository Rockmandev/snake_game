from typing import Tuple

class Grid_Point:
    def __init__(self, grid_x, grid_y, scale_factor=20):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.scale_factor = scale_factor
    
    @property
    def grid_pos(self):
        return (self.grid_x, self.grid_y)

    @grid_pos.setter
    def set_grid(self, grid_pos:Tuple[int]):
        self.grid_x = grid_pos[0]
        self.grid_y = grid_pos[1]

    @property
    def window_pos(self):
        return (self.grid_x*self.scale_factor,
                self.grid_y*self.scale_factor)
    
    @window_pos.setter
    def set_window(self, window_pos:Tuple[int]):
        self.window_x = window_pos[0]
        self.window_y = window_pos[1]

    @property
    def window_x(self):
        return self.grid_x * self.scale_factor

    @window_x.setter
    def set_window_x(self, window_x):
        self.grid_x = window_x // self.scale_factor

    @property
    def window_y(self):
        return self.grid_y * self.scale_factor

    @window_y.setter
    def set_window_y(self, window_y):
        self.grid_y = window_y // self.scale_factor

    @classmethod
    def from_window(cls, window_x, window_y, scale_factor=20):
        return Grid_Point(window_x // scale_factor, 
                          window_y // scale_factor,
                          scale_factor)
    
    def __add__(self, other):
        return Grid_Point(
            self.grid_x + other.grid_x,
            self.grid_y + other.grid_y,
            self.scale_factor
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Grid_Point(
                self.grid_x * other, self.grid_y * other, self.scale_factor
            )
        else:
            raise NotImplementedError

    def __eq__(self, other):
        return self.grid_pos == other.grid_pos