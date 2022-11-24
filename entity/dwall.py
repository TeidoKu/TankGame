import pygame


class Dwall(pygame.sprite.Sprite):
    base_image = pygame.image.load("img/dwall.png")
    def __init__(self,x = 0,y = 0):
        super().__init__()
        # self.hp = 100
        self.image = pygame.transform.scale(self.base_image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
       
    
