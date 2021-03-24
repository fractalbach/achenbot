"""
Generates Randomized Fractal Images
"""
import itertools

def makeFractal(sizeX, sizeY): 
    for (px, py) in itertools.product(range(sizeX), range(sizeY)):
        x0 = 3.5*(px / sizeX) - 2.5
        y0 = 2*(py / sizeY) - 1
        x = 0.0
        y = 0.0
        maxIter = 1000
        curIter = 0
        while (x*x + y*y <= 2*2 and curIter < maxIter):
            xtemp = x*x - y*y + x0
            y = 2*x*y + y0
            x = xtemp 
            curIter += 1
        color = getColorFromIteration(curIter, maxIter)




def getColorFromIteration(iteration, MaximumIteration):
    pass
