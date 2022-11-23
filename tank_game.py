
import pygame
import pygame.locals
from tank import Tank
from tank2 import Tank2
from wall import Wall #undistructiable wall
from projectile import Pojectile
from dwall import Dwall #distructiable wall
# def create_text_surface(text):
#     """This function creates a surface and renders the text argument in it"""

#     # Get the default font for the system
#     default_font = pygame.font.get_default_font()
#     font = pygame.font.Font(default_font, 24)
#     text_surface = font.render(text, True, (0, 0, 0))

#     return text_surface

window = pygame.display.set_mode((1280, 1024))
wall_group = pygame.sprite.Group()
dwall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
projectil_groupe = pygame.sprite.Group()

dwall_arr=[]


class Game():
    """Main program"""
    def __init__(self):
        self.proj = Pojectile()
        player_cord = self.map_gen()
        x,y = player_cord[0]
        x1,y2 = player_cord[1]
        self.tank = Tank(x,y,'up')
        self.tank2 = Tank2(x1,y2,'down')
        self.roundstart = True #game first start flag
        self.start = 0 #start tick
        self.end = 0 #shot time reference
        self.running = True #running state 
    def game(self):
        pygame.init()
        # This is required to use pygame's font system
        # pygame.font.init()
        
        # Event loop
        
        pygame.key.set_repeat(1,100)
        player_group.add(self.tank)
        player2_group.add(self.tank2)
        while self.running:

            self.start = pygame.time.get_ticks()
            if self.start < 1000 and self.roundstart:
                self.roundstart = False
                load = pygame.mixer.Sound("sound/T34reloadonly.ogg")
                pygame.mixer.Sound.set_volume(load,0.1)
                pygame.mixer.Sound.play(load)
            window = pygame.display.set_mode((1280, 1024))
            window.fill((255, 255, 255))        
            projectil_groupe.draw(window)
            player_group.draw(window)
            player2_group.draw(window)
            dwall_group.draw(window)
            wall_group.draw(window)

            
            #record self.tank original cordinats 
            xpos = self.tank.rect.x
            ypos = self.tank.rect.y 

            xpos2 = self.tank2.rect.x
            ypos2 = self.tank2.rect.y
            
            
            self.key_event_listener()

            
            if pygame.sprite.spritecollide(self.tank2, dwall_group, dokill=False):
                self.tank2.rect.x = xpos2
                self.tank2.rect.y = ypos2
                print("col")
            if pygame.sprite.spritecollide(self.tank2, wall_group, dokill=False):
                self.tank2.rect.x = xpos2
                self.tank2.rect.y = ypos2   
                print("col")

            if pygame.sprite.spritecollide(self.proj, wall_group, dokill=False):
                projectil_groupe.remove(self.proj)
            
            if pygame.sprite.spritecollide(self.proj, dwall_group, dokill=True):
                projectil_groupe.remove(self.proj)
            
            if pygame.sprite.spritecollide(self.tank, dwall_group, dokill=False):
                self.tank.rect.x = xpos
                self.tank.rect.y = ypos
            
            if pygame.sprite.spritecollide(self.tank, wall_group, dokill=False):
                self.tank.rect.x = xpos
                self.tank.rect.y = ypos
            projectil_groupe.update()
            pygame.display.update()    
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     mx = pygame.mouse.get_pos()[0]
                #     my = pygame.mouse.get_pos()[1]
                #     c1=mx-x
                #     c2=my-y
                #     con = c1*c2
                #     if 90 < con < 900:
                #         running = False                    

    def map_gen(self):
        tilesize = 64
        w_map = [
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x','d',' ',' ',' ',' ',' ',' ','p2',' ',' ',' ',' ',' ',' ',' ',' ',' ','d','x'],
        ['x',' ','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ','x'],
        ['x',' ','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ',' ','x'],
        ['x',' ',' ','d','d','d','d','d','d','d','d','d','d','d','d','d',' ',' ',' ','x'],
        ['x',' ',' ','d','d','d','d','d','d','d','d','d','d','d','d','d',' ',' ',' ','x'],
        ['x',' ','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ',' ','x'],
        ['x',' ','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ','x'],
        ['x','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ','p1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
        ]
        for row_index,row in enumerate(w_map):
            for col_index, col in enumerate(row):
                x = col_index * tilesize
                y = row_index * tilesize
                if col == 'x':
                    new_wall = Wall(x,y)
                    wall_group.add(new_wall)
                if col == 'd':
                    new_dwall = Dwall(x,y)
                    dwall_group.add(new_dwall)
                    dwall_arr.append(new_dwall)
                if col == 'p1':
                    p1 = (x,y)
                if col =='p2':
                    p2 = (x,y)
        
        return [p1, p2]

    def key_event_listener(self):
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    keycode = event.key
                    keyname = pygame.key.name(keycode)
                    if keyname == '[8]': # up
                        self.tank2.rect.y -= 20
                        self.tank2.set_direction("up")
                    if keyname == '[5]': # down 
                        self.tank2.rect.y += 20
                        self.tank2.set_direction("down")
                    if keyname == '[4]': # left
                        self.tank2.rect.x -= 20
                        self.tank2.set_direction("left")
                    if keyname == '[6]': # right
                        self.tank2.rect.x += 20
                        self.tank2.set_direction("right")
                    if keyname == '[0]' and self.start-self.end > 2800:
                        fire = pygame.mixer.Sound("sound/ATgun.ogg")
                        pygame.mixer.Sound.set_volume(fire,0.1)
                        pygame.mixer.Sound.play(fire)
                        self.end = pygame.time.get_ticks()
                        self.proj = self.tank2.shoot_bullet()
                        projectil_groupe.add(self.proj)       

                    if keyname == "up":
                        self.tank.rect.y -= 10
                        self.tank.set_direction("up")
                    if keyname == "down":
                        self.tank.rect.y += 10
                        self.tank.set_direction("down")
                    if keyname == "left":
                        self.tank.rect.x -= 10
                        self.tank.set_direction("left")
                    if keyname == "right":
                        self.tank.rect.x += 10
                        self.tank.set_direction("right")
                    
                    if keyname == "space" and self.start-self.end > 2800:
                        fire = pygame.mixer.Sound("sound/ATgun.ogg")
                        pygame.mixer.Sound.set_volume(fire,0.1)
                        pygame.mixer.Sound.play(fire)
                        self.end = pygame.time.get_ticks()
                        self.proj = self.tank.shoot_bullet()
                        projectil_groupe.add(self.proj)       


        


if __name__ == "__main__":
    Game().game()
