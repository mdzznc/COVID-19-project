from random import gauss
from math import floor


def gauss_2d(mu_x, sigma_x, *args):
    # general random a points which is in a normal distribution
    if len(args) == 2:
        mu_y = args[0]
        sigma_y = args[1]
    else:
        mu_y = mu_x
        sigma_y = sigma_x

    y = floor(gauss(mu_y, sigma_y))
    x = floor(gauss(mu_x, sigma_x))
    return y, x


# a basic vision of Conway's Game of Life

#vision 1.10 imporve the algorithm

class Cell:
    def __init__(self, state=0):
        # class, the class of the cell
        # == 0, the empty space
        # == 1, the living cell
        self.state = state
        self.neighbor = 0

    def run_rules(self):
        # neighbor_1 the number of neighbor which is state 1
        b = [2]
        s = [2,3]
        if (self.state == 1) and not (self.neighbor  in s):
            self.state = 0
        if (self.state == 0) and (self.neighbor  in b):
            self.state = 1
       #signal model
        self.neighbor = 0


    def reciver(self):
        self.neighbor = self.neighbor+1


class LifeGame:
    def __init__(self, rows, cols, alive=0, neighborranges=1, cells=[],cells_x=0, cells_y=0):
        #rows, cols, the rows and cols of the cells
        #alives percentage of the alive in first time

        self.rows = rows
        self.cols = cols
        self.alive = alive
        self.cells = []
## set the neighbor range
        self.neighborRange = neighborranges
        self.row_config = []
        self.col_config = []
        self.RangeConfigSet()
## generate the map
        self.generate(cells,cells_x, cells_y)

    def inArea(self, y, x):
        if y < 0 or x < 0 or y > self.rows-1 or x > self.cols-1:
            return False
        return True

    def generate(self,cells,cells_x, cells_y):
        for i in range(0, self.rows):
            self.cells.append([])
            for j in range(0, self.cols):
                self.cells[i].append(0)
        total = floor(self.alive*self.rows*self.cols)

        if (len(cells) == 0):
            while total > 0:
                pos = gauss_2d(self.cols/2,self.cols/4,self.rows/2,self.rows/4)
                if self.inArea(pos[0], pos[1]) and self.cells[pos[0]][pos[1]] == 0:
                    self.cells[pos[0]][pos[1]] = 1
                    total = total-1
        else:
            for i in range(0,len(cells)):
                for j in range(0,len(cells[0])):
                    if self.inArea(i+cells_y,j+cells_x):
                        self.cells[i+cells_y][j+cells_x] = cells[i][j]

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.cells[i][j] == 1:
                    self.cells[i][j] = Cell(1)
                else :
                    self.cells[i][j] = Cell(0)

    def display(self):
        s = []
        for i in range(0,self.rows):
            s.append([])
            for j in range(0,self.cols):
                s[i].append(self.cells[i][j].state)

        return s

    def RangeConfigSet(self):
        if self.neighborRange == 0:
            self.row_config = [-1, 0, 0, 1]
            self.col_config = [0, 1, -1, 0]
        else:
            for i in range(-self.neighborRange, self.neighborRange + 1):
                for j in range(-self.neighborRange, self.neighborRange + 1):
                    if i == 0 and j == 0:
                        pass
                    else:
                        self.row_config.append(i)
                        self.col_config.append(j)



    def SignalToNeighbers(self,y,x):
        if self.cells[y][x].state == 1:
            for i in range(0, len(self.row_config)):
                if self.inArea(y+self.row_config[i],x+self.col_config[i]):
                    self.cells[y + self.row_config[i]][x + self.col_config[i]].reciver()
        elif self.cells[y][x].state == 0:
            pass


    def move(self):
        count = 0
        for i in range(0,self.rows):
            for j in range(0, self.cols):
                self.SignalToNeighbers(i,j)
                if self.cells[i][j].state == 1:
                    count = count+1
        print("count : %i" % count)

        for i in range(0,self.rows):
            for j in range(0, self.cols):
                self.SignalToNeighbers(i,j)

        for i in range(0,self.rows):
            for j in range(0,self.cols):
                self.cells[i][j].run_rules()
