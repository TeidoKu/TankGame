import pygame
from .projectile import Pojectile


class Tank(pygame.sprite.Sprite):
    """This is the main player Class"""

    def __init__(self,x = 0,y = 0, direction = None):
        super().__init__()
        self.original_image_up = pygame.image.load("img/t34up.png")
        self.original_image_down = pygame.image.load("img/t34down.png")
        self.original_image_left = pygame.image.load("img/t34left.png")
        self.original_image_right = pygame.image.load("img/t34right.png")
        self.direction = direction
        self.live_status = True
        
        self.image = pygame.transform.scale(self.original_image_up, (50,100))  # default oriantation for p1 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = [self.rect.x,self.rect.y]


    def set_direction(self,direction):
        self.direction = direction

        if self.direction == "up":
            self.image = pygame.transform.scale(self.original_image_up, (50,100))
            self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
            # self.rect.w = 50
            # self.rect.h = 100
        if self.direction == "down":
            self.image = pygame.transform.scale(self.original_image_down, (50,100))
            self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
            # self.rect.w = 50
            # self.rect.h = 100
        if self.direction == "left":
            self.image = pygame.transform.scale(self.original_image_left, (100,50))
            self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
            # self.rect.w = 100
            # self.rect.h = 50
        if self.direction == "right":
            self.image = pygame.transform.scale(self.original_image_right, (100,50))
            self.rect = self.image.get_rect(topleft=(self.rect.x,self.rect.y))
            # self.rect.w = 100
            # self.rect.h = 50
    
    def shoot_bullet(self):
        if self.direction == "up":
            return Pojectile(self.rect.x + 25 , self.rect.y -10 ,self.direction)
        if self.direction == "down":
            return Pojectile(self.rect.x + 25 , self.rect.y +110 ,self.direction)
        if self.direction == "left":
            return Pojectile(self.rect.x -10 , self.rect.y +25 ,self.direction)
        if self.direction == "right":
            return Pojectile(self.rect.x +110, self.rect.y +25 ,self.direction)

    def died(self):
        self.live_status = False