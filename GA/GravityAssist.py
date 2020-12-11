import pygame
import math
import sys



def sign(a):
    return (a > 0) - (a < 0)



black = 0, 0, 0
white = 255, 255, 255

k = 1e7
m = 5.9742e24
M = 1898.7e27
G = 6.67259e-17
t = 1e5

pos_x = 20
pos_y = 500
earth = pos_x, pos_y
vel_x = 200
vel_y = 0.1
jupiter = 0, 150
v_j = 0.1


pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("arial",30)
text = font.render("Jupiter Gravity Slingshot ", 1, white)
pygame.display.set_caption("Gravitational slingshot simulation")

e = pygame.image.load("earth.jpg").convert_alpha()
j = pygame.image.load("jupiter.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()

    screen.fill(black)

    jupiter =  jupiter[0] - v_j, jupiter[1]
    screen.blit(j, jupiter)


    delta_x = (jupiter[0] - earth[0]) * k
    delta_y = (jupiter[1] - earth[1]) * k

    r2 = delta_x ** 2 + delta_y ** 2

    F = G * m * M / r2

    theta = math.acos(delta_x / r2 ** 0.5)

    fx = abs(F * math.cos(theta)) * sign(delta_x)
    fy = abs(F * math.sin(theta)) * sign(delta_y)

    ax = fx / m
    ay = fy / m

    vel_x += ax * t
    vel_y += ay * t

    pos_x += vel_x * t / k
    pos_y += vel_y * t / k
    earth = int(pos_x), int(pos_y)
    screen.blit(e, earth)

    v = 'Earth speed %.2f km/s' % ((vel_x ** 2 + vel_y ** 2) ** 0.5)
    speed = font.render(v, 1, white)
    screen.blit(text, (150, 100))
    screen.blit(speed, (200, 50))
    pygame.display.update()

