import pygame
import random

def draw_flames(ball_list, screen, palette):
    for ball in ball_list:
            randbig = random.randrange(ball.size*2, ball.size*3)
            randsmall = random.randrange(ball.size, ball.size*2)
            if ball.moveup and ball.moveright:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randbig/1.5),
                   round(ball.y + randbig/1.5)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randsmall/1.5),
                   round(ball.y + randsmall/1.5)]])
            elif ball.moveup and ball.moveleft:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randbig/1.5),
                   round(ball.y + randbig/1.5)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randsmall/1.5),
                   round(ball.y + randsmall/1.5)]])
            elif ball.movedown and ball.moveright:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randbig/1.5),
                   round(ball.y - randbig/1.5)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x - randsmall/1.5),
                   round(ball.y - randsmall/1.5)]])
            elif ball.movedown and ball.moveleft:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randbig/1.5),
                   round(ball.y - randbig/1.5)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x + randsmall/1.5),
                   round(ball.y - randsmall/1.5)]])
            elif ball.moveup:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y + randbig)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y + randsmall)]])
            elif ball.movedown:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y - randbig)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x - ball.size), round(ball.y)],
                   [round(ball.x + ball.size), round(ball.y)],
                   [round(ball.x),
                   round(ball.y - randsmall)]])
            elif ball.moveleft:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + randbig),
                   round(ball.y)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x + randsmall),
                   round(ball.y)]])
            elif ball.moveright:
                # This draws a triangle using the polygon command
                pygame.draw.polygon(screen, palette.yellow,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - randbig),
                   round(ball.y)]])
                pygame.draw.polygon(screen, palette.orange,
                   [[round(ball.x), round(ball.y - ball.size)],
                   [round(ball.x), round(ball.y + ball.size)],
                   [round(ball.x - randsmall),
                   round(ball.y)]])
            pygame.draw.circle(screen, ball.color, [round(ball.x), round(ball.y)], round(ball.size))
    return screen

def draw_arena(screen, arena, SCREEN_HEIGHT, palette):
    #Draw the rectangle around the ring
    pygame.draw.rect(screen, palette.brown, [round(arena.x - arena.size*1.1), 0, round(arena.size*2.3), SCREEN_HEIGHT])
    #Draw the starting lines in the ring
    pygame.draw.rect(screen, palette.white, [arena.x - round(arena.size/4),arena.y - round(arena.size/4), 5, round(arena.size/2)])
    pygame.draw.rect(screen, palette.white, [arena.x + round(arena.size/4 -5),arena.y - round(arena.size/4), 5, round(arena.size/2)])
    #Draw the Ring
    pygame.draw.circle(screen, arena.color, [round(arena.x), round(arena.y)], round(arena.size), 15)
    return screen

def main():
    print("draw has been imported")

if __name__ == "__main__":
    main()
