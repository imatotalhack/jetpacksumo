#This is setting up all the static variables

class Gamevar:
    """
    class to hold game variables
    """
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 500
        self.ball_size = 15.0
        self.gravity = -0.25
        self.min_speed = abs(self.gravity) * 1.5

class Palette:
    """
    class to standardize colours
    """
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.lightbrown = (203,85,73)
        self.grey = (140,140,140)
        self.red = (255,0,0)
        self.brown = (153,35,23)
        self.green = (172, 255,102)
        self.blue = (112, 121, 255)
        self.yellow = (255,229,51)
        self.orange = (255,89,44)

palette = Palette()
gamevar = Gamevar()

def main():
    print("vardata has been imported")

if __name__ == "__main__":
    main()
