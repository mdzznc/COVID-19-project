from random import gauss
from random import random
from random import randrange
from math import floor
from math import  ceil

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


# infact vision

#vision 1.10 imporve the algorithm

class Cell:
    def __init__(self, state=0):
        # class, the class of the cell
        # == 0, the empty space
        # == 1, the health people
        # == 2, sick people
        # == 3, people who surive after sick
        self.state = state
        self.sick_neighbor = 0
        self.heath_points = 0


        if self.state in (1,2):
            self.health_points = 24

    def run_rules(self,infect_rate=0, self_healing_rate=0):
        if self.state==2:
            self.health_points = self.health_points-1
            if self.health_points==0:
                self.state=0;
            if self_healing_rate > random():
                self.state=3;
        elif self.state ==1 and self.sick_neighbor > 0 :
            while self.state==1 and self.sick_neighbor>0:
                if   infect_rate >random():
                    self.state =2
                self.sick_neighbor = self.sick_neighbor-1



    def reciver(self):
        self.sick_neighbor = self.sick_neighbor+1


class LifeGame:
    def __init__(self, rows, cols, alive=0, neighborranges=1, cells=[],cells_x=0, cells_y=0,**Kwargs):
        #rows, cols, the rows and cols of the cells
        #alives percentage of the alive in first time

        self.rows = rows
        self.cols = cols
        self.alive = alive
        self.cells = []
## running rate
        self.move_mean=0
        self.move_var=0
        self.infect_rate=0
        self.self_healing_rate=0
        self.sick_percent = 0
        if "move_mean" in Kwargs:
            self.move_mean = Kwargs['move_mean']
        if "move_var" in Kwargs:
            self.move_var = Kwargs['move_var']
        if "infect_rate" in Kwargs:
            self.infect_rate = Kwargs['infect_rate']
        if "self_healing_rate" in Kwargs:
            self.self_healing_rate = Kwargs['self_healing_rate']
        if "sick_percent" in Kwargs:
            self.sick_percent = Kwargs['sick_percent']
## set the neighbor range
        self.neighborRange = neighborranges
        self.row_config = []
        self.col_config = []
        self.RangeConfigSet()
## set the movement range
        if self.move_mean != 0 or self.move_var != 0:
            self.move_row = []
            self.move_col = []
            self.setmovement()


## generate the map
        self.generate(cells,cells_x, cells_y)

    def inArea(self, y, x):
        if y < 0 or x < 0 or y > self.rows-1 or x > self.cols-1:
            return False
        return True

    def setmovement(self):
        for ranges in range(0, 11):
            self.move_row.append([])
            self.move_col.append([])
            for i in range(-ranges, ranges + 1):
                for j in range(-ranges, ranges + 1):
                    if (i ** 2 + j ** 2) ** 0.5 <= ranges:
                        self.move_row[ranges].append(i)
                        self.move_col[ranges].append(j)

    def generate(self,cells,cells_x, cells_y):
        for i in range(0, self.rows):
            self.cells.append([])
            for j in range(0, self.cols):
                self.cells[i].append(0)
        total = floor(self.alive*self.rows*self.cols)
        sick =  ceil(total*self.sick_percent)

        if (len(cells) == 0):
            while total > 0:
                pos = gauss_2d(self.cols/2,self.cols/4,self.rows/2,self.rows/4)
                if self.inArea(pos[0], pos[1]) and self.cells[pos[0]][pos[1]] == 0:
                    if sick > 0 and random()*4 < self.sick_percent:
                        self.cells[pos[0]][pos[1]] = 2
                        sick = sick-1
                    else:
                        self.cells[pos[0]][pos[1]] = 1
                    total = total-1
        else:
            for i in range(0,len(cells)):
                for j in range(0,len(cells[0])):
                    if self.inArea(i+cells_y,j+cells_x):
                        self.cells[i+cells_y][j+cells_x] = cells[i][j]

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                    self.cells[i][j] = Cell(self.cells[i][j])


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
                for j in range (-self.neighborRange,self.neighborRange + 1):
                    if i==0 and j == 0:
                        pass
                    else:
                        self.row_config.append(i)
                        self.col_config.append(j)



    def SignalToNeighbers(self,y,x):
        if self.cells[y][x].state == 2:
            for i in range(0, len(self.row_config)):
                if self.inArea(y+self.row_config[i],x+self.col_config[i]):
                    self.cells[y + self.row_config[i]][x + self.col_config[i]].reciver()
        elif self.cells[y][x].state == 0:
            pass

    def roll_pos(self,y,x):
        move_ranges = abs(floor(gauss(self.move_mean, self.move_var)))
        # avoid a large movement which is over 10
        if (move_ranges > 10):
            move_ranges = 10
        pos = randrange(len(self.move_col[move_ranges]))
        return y+self.move_row[move_ranges][pos],x+self.move_col[move_ranges][pos]

    def move(self):
        health_count = 0
        sick_count = 0
        after_heal = 0
        people_count = 0
        for i in range(0,self.rows):
            for j in range(0, self.cols):
                self.SignalToNeighbers(i,j)
                if self.cells[i][j].state == 1:
                    health_count = health_count+1
                    people_count = people_count+1
                elif self.cells[i][j].state == 2:
                    sick_count =sick_count+2
                    people_count = people_count + 1
                elif self.cells[i][j].state == 3:
                    after_heal = after_heal+1
                    people_count = people_count + 1
        print("health_count : %i" % health_count)
        print("sick_count  :  %i" % sick_count)
        print("after_heal  :  %i" % after_heal)
        print("people_count : %i" % people_count)

        for i in range(0,self.rows):
            for j in range(0,self.cols):
                self.cells[i][j].run_rules(self.infect_rate,self.self_healing_rate)

        if self.move_var !=0 or self.move_mean != 0:
            temp = []
            for i in range(0, self.rows):
                temp.append([])
                for j in range(0, self.cols):
                    temp[i].append(Cell(0))
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    if self.cells[i][j].state != 0:
                        while True:
                            pos = self.roll_pos(i, j)
                            if self.inArea(pos[0],pos[1]):
                                 if temp[pos[0]][pos[1]].state == 0:
                                    temp[pos[0]][pos[1]] = self.cells[i][j]
                                    break

            self.cells = temp
