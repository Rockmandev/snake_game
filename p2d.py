class P2D:
    def __init__(self, x:int, y:int, cellsize:int = 40):
        self.__x = x
        self.__y = y
        self.__cellsize = cellsize

    @property
    def grid_x(self):
        return self.__x
    
    @grid_x.setter
    def grid_x(self, x:int):
        self.__x = x

    @property
    def grid_y(self):
        return self.__y

    @grid_y.setter
    def grid_y(self, y:int):
        self.__y = y

    @property
    def grid(self):
        return (self.grid_x, self.grid_y)

    @grid.setter
    def grid(self, pos:Tuple(int)):
        self.grid_x = pos[0]
        self.grid_y = pos[1]

    @property
    def pixel_x(self):
        return self.grid_x * self.__cellsize

    @pixel_x.setter
    def pixel_x(self, x:int):
        self.grid_x = x // self.__cellsize

    @property
    def pixel_y(self):
        return self.grid_y * self.__cellsize

    @pixel_y.setter
    def pixel_y(self, y:int):
        self.grid_y = y // self.__cellsize

    @property
    def pixel(self):
        return (self.pixel_x, self.pixel_y)

    @pixel.setter
    def pixel(self, point:Tuple(int)):
        self.pixel_x = point[0]
        self.pixel_y = point[1]

    def __eq__(self, other):
        return (self.grid_x == other.grid_x) and (self.grid_y == other.grid_y)
    
    def __add__(self, other:P2D):
        return P2D(self.grid_x + other.grid_x, self.grid_y + other.grid_y)
