import matplotlib.pyplot as plt
import random
import math
scale = 0.87
initialLineGen = 3


def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1]-p2[1])


class Triangle:

    def __init__(self, p1, p2, p3, plt, gen):
        self.gen = gen
        self.colorhex = ''.join(
            ['#', self.redShift(), '00', self.blueShift()])
        self.points = [p1, p2, p3]
        self.plt = plt

    def redShift(self):
        redHex = str(hex(int(64*(initialLineGen-self.gen)/initialLineGen)))
        redHex = redHex[2:]
        if(len(redHex) == 1):
            redHex = '0' + redHex
        return redHex

    def blueShift(self):
        blueHex = str(hex(int(math.sqrt(255*(self.gen)/initialLineGen)*16)))
        blueHex = blueHex[2:]
        if(len(blueHex) == 1):
            blueHex = '0' + blueHex
        return blueHex

    def draw(self):
        xs = [self.points[0][0], self.points[1][0],
              self.points[2][0], self.points[0][0]]
        ys = [self.points[0][1], self.points[1][1],
              self.points[2][1], self.points[0][1]]
        plt.plot(xs, ys, color=self.colorhex, linewidth=self.gen,
                 solid_capstyle='round')

    def acceptablePoint(self):
        dist = [distance(self.points[0], self.points[1]), distance(
            self.points[0], self.points[1]), distance(self.points[1], self.points[2])]
        total = sum(dist)
        if(4*dist[0] < total):
            return 0
        if(4*dist[1] < total):
            return 1
        if(4*dist[2] < total):
            return 2
        return random.randint(0, 2)

    def newRandTriangles(self):
        randIndex = self.acceptablePoint()
        randPoint = self.points[randIndex]
        otherPoint1, otherPoint2 = self.points[(
            randIndex + 1) % 3], self.points[(randIndex + 2) % 3]
        opX = (otherPoint1[0]+otherPoint2[0]) / 2
        opY = (otherPoint1[1]+otherPoint2[1]) / 2
        opCenter = [opX, opY]
        plt.plot([randPoint[0], opCenter[0]],
                 [randPoint[1], opCenter[1]], color=self.colorhex, linewidth=self.gen, solid_capstyle='round')
        return [Triangle(randPoint, opCenter, otherPoint1, plt, self.gen*scale), Triangle(randPoint, opCenter, otherPoint2, plt, self.gen*scale)]

    def runWild(self):
        triangleList = self.newRandTriangles()
        for t in range(4094):
            littleList = triangleList[t].newRandTriangles()
            for lT in littleList:
                triangleList.append(lT)


fig = plt.figure()
fig.patch.set_facecolor('white')
tri = Triangle((random.random(), random.random()),
               (random.random(), random.random()),
               (random.random(), random.random()), plt, initialLineGen)
plt.axis('off')
tri.draw()
tri.runWild()
plt.show()
