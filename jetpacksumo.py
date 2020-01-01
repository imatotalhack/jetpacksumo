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
from graphics.draw import draw_arena
from data.vardata import *

def reset(ball_list, arena, score):
    for ball in ball_list:
        if ball.color == palette.white:
            theta = math.radians(random.randrange(140,200))
        if ball.color == palette.red:
            theta = math.radians(random.randrange(320,380))
        hypotenuse = random.randrange(0.1*gamevar.screen_width,0.25*gamevar.screen_width)
        ball.x = (math.cos(theta)*hypotenuse) + (gamevar.screen_width/2)
        ball.y = (math.sin(theta)*hypotenuse) + (gamevar.screen_height/2)

        print(ball.x)
        print(ball.size)

        ball.speed_x = 0.0
        ball.speed_y = 0.0
        ball.moveup = False
        ball.moveleft = False
        ball.moveright = False
        ball.movedown = False
        ball.size = gamevar.ball_size
    arena.color = palette.grey
    font = pygame.font.Font('freesansbold.ttf', 32)
    font_big = pygame.font.Font('freesansbold.ttf', 80)
    message = str("ROUND # " + str(score[0]))
    text = font.render(message, True, palette.lightbrown)
    text2 = font_big.render(str(score[1]), True, palette.white)
    text3 = font_big.render(str(score[2]), True, palette.red)
    winner = False
    return ball_list, arena, text, text2, text3, winner

def make_ball(color):

    """
    Function to make a new, random ball.
    """

    ball = Ball(color, gamevar.ball_size, gamevar.gravity)
    if ball.color == palette.white:
        ball.x = gamevar.screen_width/2 - 80
        ball.y = gamevar.screen_height/2
    if ball.color == palette.red:
        ball.x = gamevar.screen_width/2 + 80
        ball.y = gamevar.screen_height/2

    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    # Speed and direction of rectangle
    ball.speed_x = 0.0
    ball.speed_y = 0.0

    return ball

def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [gamevar.screen_width, gamevar.screen_height]
    screen = pygame.display.set_mode(size)
    font = pygame.font.Font('freesansbold.ttf', 32)
    font_big = pygame.font.Font('freesansbold.ttf', 80)
    score = [1,0,0] #this keeps track of the round number, player 1's wins, and player 2's wins
    message = "ROUND # " + str(score[0])
    text = font.render(message, True, palette.lightbrown)
    text2 = font_big.render("0", True, palette.white)
    text3 = font_big.render("0", True, palette.red)
    textRect = text.get_rect()
    textRect.center = (round(gamevar.screen_width/2),round(gamevar.screen_height/1.5))

    pygame.display.set_caption("Bouncing Balls")

    # Loop until the user clicks the close button.
    done = False
    winner = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []
    player_list = []

    player_1 = make_ball(palette.white)
    player_list.append(player_1)
    ball_list.append(player_1)
    player_2 = make_ball(palette.red)
    player_list.append(player_2)
    ball_list.append(player_2)
    arena = make_ball(palette.white)
    arena.color = palette.grey

    arena.size = gamevar.screen_width*0.30
    arena.x = gamevar.screen_width/2
    arena.y = gamevar.screen_height/2

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing / Keypresses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player_1.moveup = True
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
                    player_2.moveup = True
                if event.key == pygame.K_LEFT:
                    player_2.moveleft = True
                if event.key == pygame.K_RIGHT:
                    player_2.moveright = True
                if event.key == pygame.K_DOWN:
                    player_2.movedown = True
            #What happens when the key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                        player_1.moveup = False
                if event.key == pygame.K_a:
                        player_1.moveleft = False
                if event.key == pygame.K_d:
                        player_1.moveright = False
                if event.key == pygame.K_s:
                    player_1.movedown = False
                if event.key == pygame.K_UP:
                        player_2.moveup = False
                if event.key == pygame.K_LEFT:
                        player_2.moveleft = False
                if event.key == pygame.K_RIGHT:
                        player_2.moveright = False
                if event.key == pygame.K_DOWN:
                    player_2.movedown = False
                    #ball = make_ball()
                    #ball_list.append(ball)

        # --- Logic
        #basically switches the player 1 and player 2 speeds in a messy way. Recode later
        if player_1.collision_detect_alt(player_2):
            temp_speed_x = player_1.speed_x
            temp_speed_y = player_1.speed_y
            print("COLLISION!")
            player_1.speed_x = player_2.speed_x*1.5
            player_1.speed_y = player_2.speed_y*1.5
            player_2.speed_x = temp_speed_x*1.5
            player_2.speed_y = temp_speed_y*1.5
            player_1.size += 1
            player_2.size += 1

        #pauses the game for a second to show who won the round, then resets the round
        if winner == True:
            pygame.time.wait(1000)
            ball_list, arena, text, text2, text3, winner = reset(ball_list, arena, score)

        #declares player 1 the winner
        if winner == False and player_1.collision_detect_alt(arena) and not player_2.collision_detect_alt(arena):
            arena.color = palette.white
            print("Player 1 wins!")
            text = font.render('PLAYER 1 WINS!', True, palette.white)
            score[0] += 1
            score[1] += 1
            winner = True
        #declares player 2 the winner
        elif winner == False and player_2.collision_detect_alt(arena) and not player_1.collision_detect_alt(arena):
            arena.color = palette.red
            text = font.render('PLAYER 2 WINS!', True, palette.red)
            score[0] += 1
            score[2] += 1
            winner = True

        #calculates the ball/players's new positon
        for ball in ball_list:
            # Move the ball's center
            ball.speed_x = ball.friction(ball.speed_x, gamevar)
            ball.speed_y = ball.friction(ball.speed_y, gamevar)
            ball.x += ball.speed_x
            ball.y += ball.speed_y

            #This adjusts the speed based on the player input
            if ball.moveup:
                ball.speed_y = ball.speed_y - 0.5*abs(gamevar.gravity)
            if ball.moveleft:
                ball.speed_x = ball.speed_x - 0.5*abs(gamevar.gravity)
            if ball.moveright:
                ball.speed_x = ball.speed_x + 0.5*abs(gamevar.gravity)
            if ball.movedown:
                ball.speed_y = ball.speed_y + 0.5*abs(gamevar.gravity)

        # --- Drawing
        # Set the screen background
        screen.fill(palette.black)
        #sets up positons for the text objects
        textRect = text.get_rect()
        textRect.center = (round(gamevar.screen_width/2),round(gamevar.screen_height/1.5))
        textRect2 = text2.get_rect()
        textRect2.center = (50, round(gamevar.screen_height/2))
        textRect3 = text3.get_rect()
        textRect3.center = (round(gamevar.screen_width -50), round(gamevar.screen_height/2))
        screen = draw_arena(screen, arena, gamevar.screen_height, palette)
        #draws the text onto the screen
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        # Draw the balls
        screen = draw_flames(ball_list, screen, palette)

        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
