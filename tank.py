import pygame
import pygame.locals
import math



class Wall(pygame.sprite.Sprite):
    """This is the class for a falling mushroom"""

    base_image = pygame.image.load("img/wall-icon.png")

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(self.base_image, (50, 50))
        self.rect = self.image.get_rect()



class Tank(pygame.sprite.Sprite):
    """This is the main player Class"""

    def __init__(self):
        super().__init__()
        self.original_image_up = pygame.image.load("img/t34up.png")
        self.original_image_down = pygame.image.load("img/t34down.png")
        self.original_image_left = pygame.image.load("img/t34left.png")
        self.original_image_right = pygame.image.load("img/t34right.png")
        
        self.imageup = pygame.transform.scale(self.original_image_up, (25,50)) 
        self.imagedown = pygame.transform.scale(self.original_image_down, (25,50))
        self.imageleft = pygame.transform.scale(self.original_image_left, (50,25))
        self.imageright = pygame.transform.scale(self.original_image_right, (50,25))

        self.image = self.imageup # default oriantation for p1 

        self.rect = self.image.get_rect()

        # Starting position = middle of the screen, bottom
        self.rect.x = 500
        self.rect.y = 668







def create_text_surface(text):
    """This function creates a surface and renders the text argument in it"""

    # Get the default font for the system
    default_font = pygame.font.get_default_font()
    font = pygame.font.Font(default_font, 24)
    text_surface = font.render(text, True, (0, 0, 0))

    return text_surface



def main():
    """Main program"""
    
    tank = Tank()

    wall = Wall()


    pygame.init()
    # This is required to use pygame's font system
    pygame.font.init()
    window = pygame.display.set_mode((1024, 768))
    clock = pygame.time.Clock()
    # Event loop
    running = True
    x = tank.rect.x
    y = tank.rect.y
    
    pygame.font.init()
    # arial = pygame.font.SysFont('arial', 18)
    # text_surface = arial.render("quit", True, (0, 0, 0))
    pygame.key.set_repeat(1,100)
    

  
    while running:
        window.fill((255, 255, 255))
        clock.tick(60)

        surf = pygame.Surface((40,40))
        surf.fill((0, 0, 255))
        #surf.set_colorkey((0, 0, 255))
        #pygame.draw.circle(surf,(0, 255, 0), (20, 20), 15)
        # surf.blit(text_surface, (6, 6))
        window.blit(tank.image, (x, y))

        for event in pygame.event.get():
            pygame.display.update()
            if event.type == pygame.locals.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keycode = event.key
                keyname = pygame.key.name(keycode)
                if keyname == "up":
                    y -= 10
                    tank.image = tank.imageup
                if keyname == "down":
                    y +=10
                    tank.image = tank.imagedown
                if keyname == "left":
                    x -=10
                    tank.image = tank.imageleft
                if keyname == "right":
                    tank.image = tank.imageright
                    x +=10
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx = pygame.mouse.get_pos()[0]
                my = pygame.mouse.get_pos()[1]
                c1=mx-x
                c2=my-y
                con = c1*c2
                if 90 < con < 900:
                    running = False                    
               
        


        


if __name__ == "__main__":
    main()
