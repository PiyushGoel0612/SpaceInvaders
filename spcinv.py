import pygame
from spcind2 import *
import random as rd

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
stop = 0

clock = pygame.time.Clock()
FPS = 60

current = pygame.time.get_ticks()

count = 0
count_alien = 3
alien_moved = 60
direction = "LEFT"

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

bg = pygame.image.load("space.png").convert_alpha()
scaled_bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

ship_img = pygame.image.load("ship.png").convert_alpha()
bullet_img = pygame.image.load("image.png").convert_alpha()
title_img = pygame.image.load("spaceinvaders.png").convert_alpha()
alien_img = pygame.image.load("alien.png").convert_alpha()
al_blt = pygame.image.load("bulletred.png").convert_alpha()
rock_img = pygame.image.load("red.png").convert_alpha()
game_over = pygame.image.load("gmovr.png").convert_alpha()
gm_over = pygame.transform.scale(game_over,(400,200))

ship = Spaceship(280,610)

x = [80,180,280,380,480]    # 100 ka gap between ships
y = [140,220,300]           # 80 along y direction
aliens = []
alien_bullet = []

x_r = [i for i in range(50,171,15)]
x_r.extend([i for i in range(235,356,15)])
x_r.extend([i for i in range(420,541,15)])
y_r = [450,435,465,420,480]
rocks = []
temp = 1
for j in y_r:
    for i in x_r:
        rocks.append(Rocks(i,j))
    if temp == 1 or temp == 3 or temp == 5:
        x_r.pop(0)
        x_r.pop(0)
        x_r.pop(len(x_r)-1)
        x_r.pop(len(x_r)-1)
    temp += 1

for j in y:
    for i in x:
        aliens.append(Alien(i,j))
    x.pop(0)
    if len(x)!=0:
        x.pop(len(x)-1)

run = True
Finished = 0
while run:

    clock.tick(FPS)
    spc = pygame.key.get_pressed()

    # temp_var = count_alien
    # for i in range(temp_var):
    #     sh = rd.choice(aliens)
    #     alien_bullet.append(Bullet_alien(sh.rect.x,sh.rect.y))
    #     alien_bullet[len(alien_bullet)-1].move(SCREEN_HEIGHT)
    #     count_alien-=1

    screen.blit(scaled_bg,(0,0))
    screen.blit(title_img,(225,0))

    if alien_moved <= 0:
        direction = "RIGHT"

    elif alien_moved >= 100:
        direction = "LEFT"

    if direction == "LEFT":
        alien_moved -= 2

    elif direction == "RIGHT":
        alien_moved += 2

    for i in rocks:
        screen.blit(rock_img,(i.rect.x,i.rect.y))
        shit = 0
        if count == 1:
            if blt.rect.colliderect(i.rect):
                rocks.remove(i)
                del i
                del blt
                count = 0
                shit = 1
        if len(alien_bullet)!=0 and shit == 0:
            for j in alien_bullet:
                if i.rect.colliderect(j.rect):
                    rocks.remove(i)
                    alien_bullet.remove(j)
                    del i
                    del j

    ship.move(SCREEN_WIDTH)
    screen.blit(ship_img,(ship.rect.x - 20,ship.rect.y - 25))
    
    if pygame.time.get_ticks() - current > 1000:
        if len(aliens) >= 2:
            for i in rd.sample(aliens,2):
                alien_bullet.append(Bullet_alien(i.rect.x + 15,i.rect.y + 30))
        elif len(aliens) == 1:
            for i in rd.sample(aliens,1):
                alien_bullet.append(Bullet_alien(i.rect.x + 15,i.rect.y + 30))
        else:
            pass
        current  =pygame.time.get_ticks()
    
    for i in alien_bullet:
        i.move(SCREEN_HEIGHT)
        if i.rect.colliderect(ship.rect):
            alien_bullet.remove(i)
            del i
            del ship
            stop = 1
            run = False
            Finished = 1
            break
        if i.rect.y > 600:
            alien_bullet.remove(i)
            del i
        else:
            screen.blit(al_blt,(i.rect.x-15,i.rect.y-15))

    for i in aliens:
        i.move(direction)
        screen.blit(alien_img,(i.rect.x,i.rect.y))
        if count == 1:
            if blt.rect.colliderect(i.rect):
                aliens.remove(i)
                del i
                del blt
                count = 0

    if (count == 0) and (spc[pygame.K_SPACE]):
        blt = Bullet(ship.rect.x, ship.rect.y-20)
        #blt.draw(screen)
        if blt.rect.y <= 500:
            screen.blit(bullet_img,(blt.rect.x - 10,blt.rect.y - 10))
        count = 1

    if count == 1:
        blt.move(SCREEN_HEIGHT)
        #blt.draw(screen)
        if blt.rect.y <= 550:
            screen.blit(bullet_img,(blt.rect.x - 10,blt.rect.y - 10))

    if (count==1) and (blt.rect.y <= 10):
        del blt
        count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

if Finished == 1:
    screen2 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    run = True

while run:

    screen.blit(scaled_bg,(0,0))
    screen.blit(title_img,(225,0))

    for i in rocks:
        screen.blit(rock_img,(i.rect.x,i.rect.y))

    for i in aliens:
        screen.blit(alien_img,(i.rect.x,i.rect.y))

    screen.blit(gm_over,(100,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()