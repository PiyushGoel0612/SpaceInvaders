import pygame

class Spaceship:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,20,20)

    def move(self,screen_width):
        speed = 5
        dx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -speed
        elif key[pygame.K_RIGHT]:
            dx = speed
        
        if (self.rect.x +dx < 40):
            dx = self.rect.x - 40
        elif (self.rect.x + dx > screen_width-40):
            dx = screen_width - 40 - self.rect.x

        self.rect.x += dx
    
class Bullet:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,10,10)

    def move(self,screen_height):
        dy = -7
        self.rect.y += dy

class Alien:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,30,30)

    def move(self,direction):
        if direction == "LEFT":
            self.rect.x -= 2
        else:
            self.rect.x += 2

class Rocks:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,15,15)

class Bullet_alien:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,10,30)

    def move(self,screen_height):
        dy = +5
        self.rect.y += dy