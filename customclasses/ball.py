import pygame
import math

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self, color, BALL_SIZE, gamevar):
        self.x = 0.0
        self.y = 0.0
        self.change_x = 0.0
        self.change_y = 0.0
        self.moveup = False
        self.moveleft = False
        self.moveright = False
        self.movedown = False
        self.color = color
        self.size = BALL_SIZE

    def collision_detect_alt(self, othercircle):
         if(math.sqrt((self.x-othercircle.x)**2+(self.y-othercircle.y)**2)<=self.size+othercircle.size):
             return True
         else:
             return False

    def friction(self, x, gamevar):
        if x != 0:
            x = (x/abs(x))*(abs(x) - abs(gamevar.gravity/5))
            if abs(x) < abs(gamevar.gravity/10):
                x = 0
        return x

def main():
    print("ball has been imported")

if __name__ == "__main__":
    main()
