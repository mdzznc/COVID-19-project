import pyglet
from infectv2 import LifeGame
from math import floor
#version 2.0 build for infectv2

cells = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         ]

ROW = 100
COL = 100




def displayMtrix(mrt):
    for i in mrt:
        print("c(", end = '')
        for j in range(len(i)):
            if j == len(i)-1:
                print("%i),"% i[j])
            else:
                print("%i," % i[j], end='')

def displaylist(lst):
    print("c(", end='')
    for i in range(len(lst)):
        if i == len(lst) - 1:
            print("%i)" % lst[i])
        else:
            print("%i," % lst[i], end='')

hot_map = []

total_count = []
health_count = []
sick_count = []
rehealth_count = []

for i in range(ROW):
    hot_map.append([])
    for j in range(COL):
        hot_map[i].append(0)
class MainWindow(pyglet.window.Window):
    def __init__(self,*args,**Kwargs):

        self.RunState = True
        super().__init__(*args,**Kwargs)
        pyglet.clock.schedule_interval(self.update, 0.2)
        self.size = floor(args[0]/ROW)
        #####
        self.LifeGame = LifeGame(ROW,COL,alive=0.2,move_mode=2,infect_rate=0.1,sick_percent=0.01,self_healing_rate=0.01,move_pro=1)
        ###
        self.times = 0

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.show()

    def on_key_press(self, symbol, modifiers):
        displayMtrix(hot_map)
        displaylist(total_count)
        displaylist(health_count)
        displaylist(sick_count)
        displaylist(rehealth_count)
        if(self.RunState):
            pyglet.clock.unschedule(self.update)
            self.RunState = False
        else:
            pyglet.clock.schedule_interval(self.update, 0.2)
            self.RunState = True

    def show(self):
        display = self.LifeGame.display()
        total_count.append(0)
        health_count.append(0)
        sick_count.append(0)
        rehealth_count.append(0)
        for i in range(0, self.LifeGame.rows):
            for j in range(0, self.LifeGame.cols):
                green = 0
                red = 0
                blue = 0
                if display[i][j][0] > 0:
                    green = min(125+20* display[i][j][0],255)
                if display[i][j][1] > 0:
                    red = min(125 + 20 * display[i][j][1], 255)
                if display[i][j][2] > 0:
                    bule = min(125 + 20 * display[i][j][2], 255)
                color = (red, green, blue, 255)
                hot_map[i][j] = hot_map[i][j] + display[i][j][0]+display[i][j][1]+display[i][j][2]
                total_count[self.times] = total_count[self.times]+display[i][j][0]+display[i][j][1]+display[i][j][2]
                health_count[self.times] = health_count[self.times] + display[i][j][0]+ display[i][j][2]
                sick_count[self.times] = sick_count[self.times] + display[i][j][1]
                rehealth_count[self.times] = rehealth_count[self.times] + display[i][j][2]
                self.rect((i * self.size, j * self.size), self.size, self.size, color)

    def rect(self, pos, width, height, color):
        pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLE_STRIP,
                             ("v2f", (pos[0], pos[1], pos[0], pos[1] + height, pos[0] + width, pos[1], pos[0] + width,
                                      pos[1] + height)),
                             ("c4B", tuple(color[i] for i in range(0, 4)) * 4))

    def update(self, dt):
        self.times = self.times +1
        print("itera : %i" % self.times)
        if (self.times != 1):
            self.LifeGame.move()
        # if(self.times %100 ==0):
        #     displayMtrix(hot_map)
        #     displaylist(total_count)
        #     displaylist(health_count)
        #     displaylist(sick_count)
        #     displaylist(rehealth_count)
        if(sick_count[len(sick_count)-1] == 0 or health_count[len(sick_count)-1] -rehealth_count[len(sick_count)-1] == 0):
              displaylist(total_count)
              displaylist(health_count)
              displaylist(sick_count)
              displaylist(rehealth_count)
        print("FPS : % f" % pyglet.clock.get_fps())


window = MainWindow(800, 800,"Henrys Cellular automaton")
pyglet.app.run()
