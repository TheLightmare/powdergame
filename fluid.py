import pygame as pg
import random
import math

pg.init()

HEIGHT = 220*2
WIDTH = 390*2
PIXEL_DIM = 2
MAP_DIM_X = WIDTH/PIXEL_DIM
MAP_DIM_Y = HEIGHT/PIXEL_DIM
FPS = 60

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (100, 50, 50)
BLACK = (0, 0, 0)
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

playing = True

pg.key.set_repeat(300, 300)
screen.fill((255,255,255))
pg.display.flip()

def draw_pixel (x, y, color) :
    pg.draw.rect(screen, color, (x, y, PIXEL_DIM, PIXEL_DIM))

def get_pixel (x, y) :
    if x > 0 and x < WIDTH and y > 0 and y < HEIGHT :
        return screen.get_at((x, y))
    else :
        return BLACK

def bake_lighting (x, y, material): #not effective right now. should permit to have fancier materials
    c = 1
    if material == "water":
        for i in range(y-PIXEL_DIM, y+PIXEL_DIM , PIXEL_DIM) :
            for j in range(x-PIXEL_DIM, x+PIXEL_DIM, PIXEL_DIM) :
                if get_pixel(i, j) != WHITE :
                    c += 1
        print(c)
        return (0, 0, (255/9)*c)

def summon_particles (x, y, material) :
    for i in range(y-(5*PIXEL_DIM), y+(5*PIXEL_DIM), PIXEL_DIM) :
        for j in range(x-(5*PIXEL_DIM), x+(5*PIXEL_DIM), PIXEL_DIM) :
            if material == "water" and get_pixel(x, y) == WHITE:
                part_w_x.append(j)
                part_w_y.append(i)
            elif material == "dirt" and get_pixel(x, y) == WHITE:
                part_d_x.append(j)
                part_d_y.append(i)
                
def update():
    for i in range(0, len(part_w_x)) :
        draw_pixel(part_w_x[i], part_w_y[i], WHITE)
        if get_pixel(part_w_x[i], part_w_y[i] + PIXEL_DIM + 1) == WHITE and part_w_y[i] < HEIGHT :
            part_w_y[i] += PIXEL_DIM
        elif get_pixel(part_w_x[i] + PIXEL_DIM, part_w_y[i]) == WHITE and get_pixel(part_w_x[i] - PIXEL_DIM, part_w_y[i]) != WHITE and part_w_x[i] > 0 :
            part_w_x[i] += PIXEL_DIM
        elif get_pixel(part_w_x[i] + PIXEL_DIM, part_w_y[i]) != WHITE and get_pixel(part_w_x[i] - PIXEL_DIM, part_w_y[i]) == WHITE and part_w_x[i] < WIDTH :
            part_w_x[i] -= PIXEL_DIM
        elif get_pixel(part_w_x[i] + PIXEL_DIM, part_w_y[i]) == WHITE and get_pixel(part_w_x[i] - PIXEL_DIM, part_w_y[i]) == WHITE:
            if random.randint(0,1) == 0 :
                part_w_x[i] += PIXEL_DIM
            else :
                part_w_x[i] -= PIXEL_DIM

        draw_pixel(part_w_x[i], part_w_y[i], BLUE)

    for i in range(0, len(part_d_x)) :
        draw_pixel(part_d_x[i], part_d_y[i], WHITE)
        if get_pixel(part_d_x[i], part_d_y[i] + PIXEL_DIM + 1) == WHITE and part_d_y[i] < HEIGHT :
            part_d_y[i] += PIXEL_DIM
        

        draw_pixel(part_d_x[i], part_d_y[i], BROWN)

part_w_x = []
part_w_y = []

part_d_x = []
part_d_y = []

r = 0


while playing :

    clock.tick(FPS)
    pg.display.set_caption("{:.2f}".format(clock.get_fps()) + "    water : " + str(len(part_w_x)) + "    dirt : " + str(len(part_d_x)))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        if event.type == pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                playing = False
                
            if event.key == pg.K_RIGHT :
                summon_particles(50, 10, "water")

            if event.key == pg.K_LEFT :
                summon_particles(500, 10, "dirt")

    update()
    
    pg.display.flip()

pg.quit()

    
