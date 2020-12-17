import pygame as pg
import random
import math

pg.init()

HEIGHT = 220*2
WIDTH = 390*2
PIXEL_DIM = 2
MAP_DIM_X = WIDTH/PIXEL_DIM
MAP_DIM_Y = HEIGHT/PIXEL_DIM

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

playing = True

screen.fill((255,255,255))
pg.display.flip()

def draw_pixel (x, y, color) :
    pg.draw.rect(screen, color, (x, y, PIXEL_DIM, PIXEL_DIM))

def get_pixel (x, y) :
    if x > 0 and x < WIDTH and y > 0 and y < HEIGHT :
        return screen.get_at((x, y))
    else :
        return BLACK

def bake_lighting (x, y, material):
    c = 1
    if material == "water":
        for i in range(y-PIXEL_DIM, y+PIXEL_DIM , PIXEL_DIM) :
            for j in range(x-PIXEL_DIM, x+PIXEL_DIM, PIXEL_DIM) :
                if get_pixel(i, j) != WHITE :
                    c += 1
        print(c)
        return (0, 0, (255/9)*c)

nb = int(input("> nombre de particules : "))

part_x = []
part_y = []


r = 0
offset = 10
for a in range(offset, offset + int(math.sqrt(nb)) + 1) :
    for b in range(offset, offset + int(math.sqrt(nb)) + 1) :

        r += 1
        part_y.append(a*PIXEL_DIM)
        part_x.append(b*PIXEL_DIM)


while playing :

    clock.tick(60)
    
    for i in range(0, len(part_x)) :
        draw_pixel(part_x[i], part_y[i], WHITE)
        if get_pixel(part_x[i], part_y[i] + PIXEL_DIM + 1) == WHITE and part_y[i] < HEIGHT :
            part_y[i] += PIXEL_DIM
        elif get_pixel(part_x[i] + PIXEL_DIM, part_y[i]) == WHITE and get_pixel(part_x[i] - PIXEL_DIM, part_y[i]) != WHITE and part_x[i] > 0 :
            part_x[i] += PIXEL_DIM
        elif get_pixel(part_x[i] + PIXEL_DIM, part_y[i]) != WHITE and get_pixel(part_x[i] - PIXEL_DIM, part_y[i]) == WHITE and part_x[i] < WIDTH :
            part_x[i] -= PIXEL_DIM
        elif get_pixel(part_x[i] + PIXEL_DIM, part_y[i]) == WHITE and get_pixel(part_x[i] - PIXEL_DIM, part_y[i]) == WHITE:
            if random.randint(0,1) == 0 :
                part_x[i] += PIXEL_DIM
            else :
                part_x[i] -= PIXEL_DIM

        draw_pixel(part_x[i], part_y[i], BLUE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
    
    pg.display.flip()

    
