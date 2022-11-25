import pygame

class Pojectile(pygame.sprite.Sprite):
    def __init__(self,x=0,y=20,direction="up"):
        super().__init__()
        if (x != None and y != None):
            self.x = x 
            self.y = y
            self.image = pygame.Surface((10,10))
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect(center = (self.x,self.y)) # default up 
            self.direction = direction
        else:
            pass
    def update(self):
        if self.direction == 'up':
            self.rect.y -= 15
        if self.direction == 'down':
            self.rect.y += 15
        if self.direction == 'left':
            self.rect.x -= 15
        if self.direction == 'right':
            self.rect.x += 15