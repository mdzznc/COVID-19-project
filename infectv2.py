from random import gauss
from random import random
from random import randrange
from math import floor
from math import ceil


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

# vision 2.0  changed the moving method

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
        self.lastroom = 1
        self.thisroom = 1
        self.dir =randrange(0,4)

        #for moving mode 1
        self.mode1stat = False

        if self.state in (1, 2):
            self.health_points = 24

    def run_rules(self, infect_rate=0, self_healing_rate=0):
        if self.state == 2:
            self.health_points = self.health_points - 1
            if self.health_points == 0:
                self.state = 0;
            if self_healing_rate > random():
                self.state = 3;
        elif self.state == 1 and self.sick_neighbor > 0:
            while self.state == 1 and self.sick_neighbor > 0:
                if infect_rate > random():
                    self.state = 2
                self.sick_neighbor = self.sick_neighbor - 1

    def reciver(self):
        self.sick_neighbor = self.sick_neighbor + 1

    def isNeedChange(self,mode):
        if mode ==2:
            return True
        return self.lastroom < self.thisroom

    def change_dir(self,mode = 0):
        if mode ==0:
            self.dir = (self.dir+1)%4
        elif mode ==1:
            if self.mode1stat:
                self.dir = (self.dir+2)%4
                self.mode1stat = False
            else:
                self.change_dir(mode=0)
                self.mode1stat = True
        elif mode ==2:
            self.dir = randrange(0, 4)
        elif mode ==3:
            self.dir = randrange(0, 4)


class LifeGame:
    def __init__(self, rows, cols, alive=0, spreadRange=1,moverate=1,cells=[], cells_x=0, cells_y=0, **Kwargs):
        # rows, cols, the rows and cols of the cells
        # alives percentage of the alive in first time


        ## running rate
        self.infect_rate = 0
        self.self_healing_rate = 0
        self.sick_percent = 0
        self.move_mode = 0
        self.move_pro=1
        if "infect_rate" in Kwargs:
            self.infect_rate = Kwargs['infect_rate']
        if "move_pro" in Kwargs:
            self.move_pro = Kwargs['move_pro']
        if "self_healing_rate" in Kwargs:
            self.self_healing_rate = Kwargs['self_healing_rate']
        if "sick_percent" in Kwargs:
            self.sick_percent = Kwargs['sick_percent']
        if "move_mode" in Kwargs:
            self.move_mode = Kwargs['move_mode']

        ## set the spread range
        self.spreadRange = spreadRange
        self.spread_row = []
        self.spread_col = []
        self.spreadrange()
        ## config of movement
        self.moverate = moverate
        self.x_move = [-1,0,1,0]
        self.y_move = [0,1,0,-1]
        ## generate the map
        self.rows = rows
        self.cols = cols
        self.alive = alive
        self.cells = []
        self.generate(cells, cells_x, cells_y)

    def inArea(self, y, x):
        if y < 0 or x < 0 or y > self.rows - 1 or x > self.cols - 1:
            return False
        return True

    def spreadrange(self):
        for ranges in range(0, 11):
            self.spread_row.append([])
            self.spread_col.append([])
            for i in range(-ranges, ranges + 1):
                for j in range(-ranges, ranges + 1):
                    if (i ** 2 + j ** 2) ** 0.5 <= ranges:
                        self.spread_row[ranges].append(i)
                        self.spread_col[ranges].append(j)

    def generate(self, cells, cells_x, cells_y):
        for i in range(0, self.rows):
            self.cells.append([])
            for j in range(0, self.cols):
                self.cells[i].append([])
        total = floor(self.alive * self.rows * self.cols)
        sick = ceil(total * self.sick_percent)

##working on generate map
        if (len(cells) == 0):
            ## no map input
            while total > 0:
                pos = gauss_2d(self.cols / 2, self.cols / 4, self.rows / 2, self.rows / 4)
                if self.inArea(pos[0], pos[1]):
                    if sick > 0 and random() * 4 < self.sick_percent:
                        self.cells[pos[0]][pos[1]].append(2)
                        sick = sick - 1
                    else:
                        self.cells[pos[0]][pos[1]].append(1)
                    total = total - 1
        else:
            #using a input map
            for i in range(0, len(cells)):
                for j in range(0, len(cells[0])):
                    if self.inArea(i + cells_y, j + cells_x) and cells[i][j] != 0:
                        if type(cells) == list:
                            self.cells[i + cells_y][j + cells_x] = self.cells[i + cells_y][j + cells_x] + cells[i][j]
                        if type(cells) == int:
                            self.cells[i + cells_y][j + cells_x].append(cells[i][j])

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                for k in range(len(self.cells[i][j])):
                     self.cells[i][j][k]= Cell(self.cells[i][j][k])

    def display(self):
        s = []
        total = 0
        total_sick = 0
        for i in range(0, self.rows):
            s.append([])
            for j in range(0, self.cols):
                sick = 0
                health = 0
                recovered = 0
                for k in range(len(self.cells[i][j])):
                    total = total+1
                    if(self.cells[i][j][k].state == 1):
                        health = health +1
                    elif(self.cells[i][j][k].state == 2):
                        sick = sick+1
                        total_sick = total_sick +1
                    elif (self.cells[i][j][k].state == 3):
                        recovered = recovered+1

                s[i].append([health,sick,recovered])
        print("total : %i" % total)
        print("total sick : %i" % total_sick)
        return s

    def roomreciver(self,y,x):
        for i in range(len(self.cells[y][x])):
            self.cells[y][x][i].reciver()

    def roommates(self,y,x):
        for i in range(len(self.cells[y][x])):
            self.cells[y][x][i].lastroom = len(self.cells[y][x])

    def roomstatecheck(self, y, x):
        for i in range(len(self.cells[y][x])):
            ## remove death people and send the inpormation
            if self.cells[y][x][i].state == 2:
                for i in range(0, len(self.spread_row[self.spreadRange])):
                    if self.inArea(y + self.spread_row[self.spreadRange][i], x + self.spread_col[self.spreadRange][i]):
                        self.roomreciver(y + self.spread_row[self.spreadRange][i],x + self.spread_col[self.spreadRange][i])
        for i in self.cells[y][x]:
            if i.state == 0:
                self.cells[y][x].remove(i)


    def move(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.roomstatecheck(i, j)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                for k in range(len(self.cells[i][j])):
                    self.cells[i][j][k].run_rules(self.infect_rate, self.self_healing_rate)


        for i in range(0, self.rows):
            for j in range(0, self.cols):
                for k in range(len(self.cells[i][j])):
                    self.cells[i][j][k].thisroom = len(self.cells[i][j])

        # move

        temp = []
        for i in range(0, self.rows):
            temp.append([])
            for j in range(0, self.cols):
                temp[i].append([])

        for i in range(0, self.rows):
            for j in range(0, self.cols):
                for k in range(len(self.cells[i][j])):
                    if(self.cells[i][j][k].isNeedChange(mode=self.move_mode)):
                        self.cells[i][j][k].change_dir(mode=self.move_mode)
                    dir = self.cells[i][j][k].dir
                    while( not self.inArea(i+self.y_move[dir],j+self.x_move[dir])):
                        self.cells[i][j][k].change_dir(mode=self.move_mode)
                        dir = self.cells[i][j][k].dir
                    if(self.move_pro>random()):
                        temp[i+self.y_move[dir]][j+self.x_move[dir]].append(self.cells[i][j][k])
                    else:
                        temp[i][j].append(self.cells[i][j][k])
                    self.cells[i][j][k].lastroom = self.cells[i][j][k].thisroom

        self.cells = temp
