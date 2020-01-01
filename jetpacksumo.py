"""
This is a game where you try and knock your opponent out of the ring.
Player 1 uses UP, DOWN, LEFT, RIGHT,
Player 2 uses W,S,A,D,

This game was written by: Ben Lee, David Lee, and Patrick Lee
"""

import pygame
import random
import math
from customclasses.ball import Ball
from graphics.draw import draw_flames
from data.vardata import *

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

    ball = Ball(color, BALL_SIZE, GRAVITY)
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

def draw_arena(screen, arena):
    #Draw the rectangle around the ring
    pygame.draw.rect(screen, BROWN, [round(arena.x - arena.size*1.1), 0, round(arena.size*2.3), SCREEN_HEIGHT])
    #Draw the starting lines in the ring
    pygame.draw.rect(screen, WHITE, [arena.x - round(arena.size/4),arena.y - round(arena.size/4), 5, round(arena.size/2)])
    pygame.draw.rect(screen, WHITE, [arena.x + round(arena.size/4 -5),arena.y - round(arena.size/4), 5, round(arena.size/2)])
    #Draw the Ring
    pygame.draw.circle(screen, arena.color, [round(arena.x), round(arena.y)], round(arena.size), 15)
    return screen


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
        # --- Event Processing / Keypresses
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
            ball.change_x = ball.friction(ball.change_x, GRAVITY)
            ball.change_y = ball.friction(ball.change_y, GRAVITY)
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

            ball.y += ball.change_y

        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)
        textRect = text.get_rect()
        textRect.center = (round(SCREEN_WIDTH/2),round(SCREEN_HEIGHT/1.5))
        textRect2 = text2.get_rect()
        textRect2.center = (50, round(SCREEN_HEIGHT/2))
        textRect3 = text3.get_rect()
        textRect3.center = (round(SCREEN_WIDTH -50), round(SCREEN_HEIGHT/2))
        screen = draw_arena(screen, arena)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        # Draw the balls
        screen = draw_flames(ball_list, screen, YELLOW, ORANGE)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
