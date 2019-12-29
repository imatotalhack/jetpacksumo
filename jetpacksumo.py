"""
This is a game where you try and knock your opponent out of the ring.
Player 1 uses UP, DOWN, LEFT, RIGHT,
Player 2 uses W,S,A,D,

This game was written by: Ben Lee, David Lee, and Patrick Lee
"""

import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTBROWN = (203,85,73)
GREY = (140,140,140)
RED = (255,0,0)
BROWN = (153,35,23)
GREEN = (172, 255,102)
BLUE = (112, 121, 255)
YELLOW = (255,229,51)
ORANGE = (255,89,44)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 15.0
GRAVITY = -0.25
MIN_SPEED = abs(GRAVITY) * 1.5
MAX_Y_SPEED = abs(GRAVITY) * 3
MAX_X_SPEED = abs(GRAVITY) * 1

class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self, color):
        self.x = 0.0
        self.y = 0.0
        self.change_x = 0.0
        self.change_y = 0.0
        self.booster = False
        self.moveleft = False
        self.moveright = False
        self.movedown = False
        self.color = color
        self.size = BALL_SIZE

    def collision_detect(self, otherplayer):
        """ Assumes rectangles are same size or that this rectangle is smaller than the other rectangle"""
        if self.x + self.change_x > (otherplayer.x + otherplayer.size):
            # Is to the right of the other rectangle
            return False
        elif (self.x + self.change_x + self.size) < otherplayer.x - otherplayer.size:
            # is to the left of the other rectangle
            return False
        elif (self.y + self.change_y + self.size) < otherplayer.y - otherplayer.size:
            # is above the other rectangle
            return False
        elif self.y + self.change_y > (otherplayer.y + self.size + otherplayer.size):
            # is below the other rectangle
            return False
        else:
            return True
    def collision_detect_alt(self, othercircle):
         if(math.sqrt((self.x-othercircle.x)**2+(self.y-othercircle.y)**2)<=self.size+othercircle.size):
             return True
         else:
             return False
    def friction(self, x):
        if x != 0:
            x = (x/abs(x))*(abs(x) - abs(GRAVITY/5))
            if abs(x) < abs(GRAVITY/10):
                x = 0
        return x

def reset(ball_list, arena, score):
    for ball in ball_list:
        if ball.color == WHITE:
            theta = math.radians(random.randrange(140,200))
        if ball.color == RED:
            theta = math.radians(random.randrange(320,380))
        hypotenuse = random.randrange(0.1*SCREEN_WIDTH,0.25*SCREEN_WIDTH)
        ball.x = (math.cos(theta)*hypotenuse) + (SCREEN_WIDTH/2)
        ball.y = (math.sin(theta)*hypotenuse) + (SCREEN_HEIGHT/2)
        #if ball.color == WHITE:
            #ball.x = random.randrange(SCREEN_WIDTH*0.2, SCREEN_WIDTH/2)
        #if ball.color == RED:
            #ball.x = random.randrange(SCREEN_WIDTH/2, SCREEN_WIDTH*0.8)
        print(ball.x)
        print(ball.size)
        #ball.y = SCREEN_HEIGHT/2 + ((math.sqrt((SCREEN_WIDTH*0.30)**2 - ((SCREEN_WIDTH/2 - ball.x)**2))))
        ball.change_x = 0.0
        ball.change_y = 0.0
        ball.booster = False
        ball.moveleft = False
        ball.moveright = False
        ball.movedown = False
        ball.size = BALL_SIZE
    arena.color = GREY
    font = pygame.font.Font('freesansbold.ttf', 32)
    font_big = pygame.font.Font('freesansbold.ttf', 80)
    message = str("ROUND # " + str(score[0]))
    text = font.render(message, True, LIGHTBROWN)
    text2 = font_big.render(str(score[1]), True, WHITE)
    text3 = font_big.render(str(score[2]), True, RED)
    winner = False
    return ball_list, arena, text, text2, text3, winner

def make_ball(color):

    """
    Function to make a new, random ball.
    """

    ball = Ball(color)
    if ball.color == WHITE:
        ball.x = SCREEN_WIDTH/2 - 80
        ball.y = SCREEN_HEIGHT/2
    if ball.color == RED:
        ball.x = SCREEN_WIDTH/2 + 80
        ball.y = SCREEN_HEIGHT/2

    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    # Speed and direction of rectangle
    ball.change_x = 0.0
    ball.change_y = 0.0

    return ball

def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font('freesansbold.ttf', 32)
    font_big = pygame.font.Font('freesansbold.ttf', 80)
    score = [1,0,0] #this keeps track of the round number, player 1's wins, and player 2's wins
    message = str("ROUND # " + str(score[0]))
    text = font.render(message, True, LIGHTBROWN)
    text2 = font_big.render("0", True, WHITE)
    text3 = font_big.render("0", True, RED)
    textRect = text.get_rect()
    textRect.center = (round(SCREEN_WIDTH/2),round(SCREEN_HEIGHT/1.5))

    pygame.display.set_caption("Bouncing Balls")

    # Loop until the user clicks the close button.
    done = False
    winner = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []
    player_list = []

    player_1 = make_ball(WHITE)
    player_list.append(player_1)
    ball_list.append(player_1)
    player_2 = make_ball(RED)
    player_list.append(player_2)
    ball_list.append(player_2)
    arena = make_ball(WHITE)
    arena.color = GREY

    arena.size = SCREEN_WIDTH*0.30
    arena.x = SCREEN_WIDTH/2
    arena.y = SCREEN_HEIGHT/2

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_1.booster = True
                if event.key == pygame.K_a:
                    player_1.moveleft = True
                if event.key == pygame.K_d:
                    player_1.moveright = True
                if event.key == pygame.K_s:
                    player_1.movedown = True
                if event.key == pygame.K_r:
                    for player in player_list:
                        ball_list, arena, text, text2, text3, winner= reset(ball_list, arena, score)
                #Player 2 controls
                if event.key == pygame.K_UP:
                    player_2.booster = True
                if event.key == pygame.K_LEFT:
                    player_2.moveleft = True
                if event.key == pygame.K_RIGHT:
                    player_2.moveright = True
                if event.key == pygame.K_DOWN:
                    player_2.movedown = True
            #What happens when the key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                        player_1.booster = False
                if event.key == pygame.K_a:
                        player_1.moveleft = False
                if event.key == pygame.K_d:
                        player_1.moveright = False
                if event.key == pygame.K_s:
                    player_1.movedown = False
                if event.key == pygame.K_UP:
                        player_2.booster = False
                if event.key == pygame.K_LEFT:
                        player_2.moveleft = False
                if event.key == pygame.K_RIGHT:
                        player_2.moveright = False
                if event.key == pygame.K_DOWN:
                    player_2.movedown = False
                    #ball = make_ball()
                    #ball_list.append(ball)

        # --- Logic
        #basically switches the player 1 and player 2 speeds in a messy way. Recode layer
        if player_1.collision_detect_alt(player_2):
            temp_change_x_1 = player_1.change_x
            temp_change_x_2 = player_2.change_x
            temp_change_y_1 = player_1.change_y
            temp_change_y_2 = player_2.change_y
            print("COLLISION!")
            player_1.change_x = temp_change_x_2*1.5
            player_2.change_x = temp_change_x_1*1.5
            player_1.change_y = temp_change_y_2*1.5
            player_2.change_y = temp_change_y_1*1.5
            player_1.size += 1
            player_2.size += 1

        if winner == True:
            pygame.time.wait(1000)
            ball_list, arena, text, text2, text3, winner = reset(ball_list, arena, score)

        if winner == False and player_1.collision_detect_alt(arena) and not player_2.collision_detect_alt(arena):
            arena.color = WHITE
            print("Player 1 wins!")
            text = font.render('PLAYER 1 WINS!', True, WHITE)
            score[0] += 1
            score[1] += 1
            winner = True
        elif winner == False and player_2.collision_detect_alt(arena) and not player_1.collision_detect_alt(arena):
            arena.color = RED
            text = font.render('PLAYER 2 WINS!', True, RED)
            score[0] += 1
            score[2] += 1
            winner = True

        for ball in ball_list:
            # Move the ball's center
            ball_index = ball_list.index(ball)
            ball.change_x = ball.friction(ball.change_x)
            ball.change_y = ball.friction(ball.change_y)
            ball.x += ball.change_x
            #ball.change_y = ball.change_y - GRAVITY
            if ball.booster:
                ball.change_y = ball.change_y - 0.5*abs(GRAVITY)
            if ball.moveleft:
                ball.change_x = ball.change_x - 0.5*abs(GRAVITY)
            if ball.moveright:
                ball.change_x = ball.change_x + 0.5*abs(GRAVITY)
            if ball.movedown:
                ball.change_y = ball.change_y + 0.5*abs(GRAVITY)

            #if the ball will go through the ceiling of the floor next refresh
            # if (ball.y + ball.change_y > SCREEN_HEIGHT - ball.size):
            #     ball.change_y *= (-1*abs(GRAVITY*0.5))
            #     if abs(ball.change_y) < MIN_SPEED:
            #         ball.change_y = 0.0
            #         ball.change_x = 0.0
            # if ball.x + ball.change_x > SCREEN_WIDTH - ball.size or ((ball.x + ball.change_x) < ball.size):
            #     ball.change_x *= (-1*abs(GRAVITY*0.7))
            ball.y += ball.change_y
            # Bounce the ball if needed

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        textRect = text.get_rect()
        textRect.center = (round(SCREEN_WIDTH/2),round(SCREEN_HEIGHT/1.5))
        textRect2 = text2.get_rect()
        textRect2.center = (50, round(SCREEN_HEIGHT/2))
        textRect3 = text3.get_rect()
        textRect3.center = (round(SCREEN_WIDTH -50), round(SCREEN_HEIGHT/2))

        #Draw the rectangle around the ring
        pygame.draw.rect(screen, BROWN, [round(arena.x - arena.size*1.1), 0, round(arena.size*2.3), SCREEN_HEIGHT])
        #Draw the starting lines in the ring
        pygame.draw.rect(screen, WHITE, [arena.x - round(arena.size/4),arena.y - round(arena.size/4), 5, round(arena.size/2)])
        pygame.draw.rect(screen, WHITE, [arena.x + round(arena.size/4 -5),arena.y - round(arena.size/4), 5, round(arena.size/2)])
        #Draw the Ring
        pygame.draw.circle(screen, arena.color, [round(arena.x), round(arena.y)], round(arena.size), 15)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        # Draw the balls
        for ball in ball_list:
            randbig = random.randrange(ball.size*2, ball.size*3)
            randsmall = random.randrange(ball.size, ball.size*2)
            if ball.booster and ball.moveright:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randbig/1.5),
                   round(ball.y + randbig/1.5)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randsmall/1.5),
                   round(ball.y + randsmall/1.5)]])
            elif ball.booster and ball.moveleft:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randbig/1.5),
                   round(ball.y + randbig/1.5)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randsmall/1.5),
                   round(ball.y + randsmall/1.5)]])
            elif ball.movedown and ball.moveright:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randbig/1.5),
                   round(ball.y - randbig/1.5)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randsmall/1.5),
                   round(ball.y - randsmall/1.5)]])
            elif ball.movedown and ball.moveleft:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randbig/1.5),
                   round(ball.y - randbig/1.5)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randsmall/1.5),
                   round(ball.y - randsmall/1.5)]])
            elif ball.booster:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y + randbig)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y + randsmall)]])
            elif ball.movedown:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y - randbig)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y - randsmall)]])
            elif ball.moveleft:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + randbig),
                   round(ball.y)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + randsmall),
                   round(ball.y)]])
            elif ball.moveright:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, YELLOW,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - randbig),
                   round(ball.y)]])
                pygame.draw.polygon(screen, ORANGE,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - randsmall),
                   round(ball.y)]])
            pygame.draw.circle(screen, ball.color, [round(ball.x), round(ball.y)], round(ball.size))
            #pygame.draw.circle(screen, ball.color, [int(ball.x + ball.change_x*10), int(ball.y + ball.change_y*10)], int(ball.size))
            #pygame.draw.circle(screen, ball.color, [int(ball.x+ ball.change_x*20), int(ball.y + ball.change_y*20)], int(ball.size))

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
