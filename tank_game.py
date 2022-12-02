import pygame
import pygame.locals
from entity import Tank, Tank2 ,Wall ,Pojectile ,Dwall
from helper import TextSurface
from endscreen import EndScreen
#Wall undistructiable wall
#Dwall distructiable wall

window = pygame.display.set_mode((1280, 960))
wall_group = pygame.sprite.Group()
dwall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
projectil_groupe = pygame.sprite.Group()



"""Main game class"""
class Game():
    
    def __init__(self):

        """
        Initialize all game variables
        Player cordination is generated from map generator
        assign player cordiats using unpacking

        Initialize player position and direction
        """
        self.proj = Pojectile() 
        player_cord = self.map_gen() # get player cordinats from map generator
        x,y = player_cord[0] # assign player cordinats to x and y using unpacking
        x1,y2 = player_cord[1] 
        self.tank = Tank(x,y,'up') 
        self.tank2 = Tank2(x1,y2,'down')
        self.roundstart = True #game first start flag
        self.start = 0
        
        self.end1 = 0 #p1 shot time reference
        self.end2 = 0 #p2 shot time reference
        self.running = True #running state

    def tick_to_sec (self, tick):
        """
        This function convert tick to second
        """
        return tick/1000

    def game_loop(self,Start_tick):
        """
        main game loop
        recive start tick from start screen
        plays music when game starts
        initialize game time using current_tick - start_tick
        """
        pygame.init()
        # This is required to use pygame's font system
        # pygame.font.init()
        # Event loop

        pygame.mixer.music.load("sound/bgm.ogg")
        
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

        # pygame.key.set_repeat(1,100)
        player_group.add(self.tank)
        player2_group.add(self.tank2)  
        
        while self.running:
            window = pygame.display.set_mode((1280, 960))
            window.fill((255, 255, 255)) 
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

            #start time tick
            
            #display time in seconds
            if self.roundstart:
                self.roundstart = False
                load = pygame.mixer.Sound("sound/T34reloadonly.ogg")
                pygame.mixer.Sound.set_volume(load,0.1)
                pygame.mixer.Sound.play(load)
                

            self.start = pygame.time.get_ticks() - Start_tick
            projectil_groupe.draw(window)
            player_group.draw(window)
            player2_group.draw(window)
            dwall_group.draw(window)
            wall_group.draw(window)
            #blit time text on posistion
            timetext = TextSurface().create_text_surface( f"{str(self.tick_to_sec(self.start))} sec")
            timetext.get_rect().center = (1000, -20)
            window.blit(timetext, (1110, 30))
            

            
            #record self.tank original cordinats 
            xpos = self.tank.rect.x
            ypos = self.tank.rect.y 

            xpos2 = self.tank2.rect.x
            ypos2 = self.tank2.rect.y
            

            self.key_event_listener(Start_tick)

            
            #end game 
            if pygame.sprite.spritecollide(self.proj, player_group, dokill=True):
                self.tank.live_status = False
                EndScreen('P2',self.tick_to_sec(self.start))
                self.running = False

            if pygame.sprite.spritecollide(self.proj, player2_group, dokill=True):
                self.tank2.live_status = False
                EndScreen('P1',self.tick_to_sec(self.start))
                
                self.running = False
            
            # projectil collision with with wall
            if pygame.sprite.spritecollide(self.proj, wall_group, dokill=False):
                pygame.sprite.Sprite.kill(self.proj)
                self.proj.rect.x = 0
                self.proj.rect.y = 20
            if pygame.sprite.spritecollide(self.proj, dwall_group, dokill=True):
                pygame.sprite.Sprite.kill(self.proj)
                self.proj.rect.x = 0
                self.proj.rect.y = 20
            
            # wall collision detection

            if pygame.sprite.spritecollide(self.tank2, dwall_group, dokill=False):
                self.tank2.rect.x = xpos2
                self.tank2.rect.y = ypos2
                
            if pygame.sprite.spritecollide(self.tank2, wall_group, dokill=False):
                self.tank2.rect.x = xpos2
                self.tank2.rect.y = ypos2   
                

            if pygame.sprite.spritecollide(self.tank, dwall_group, dokill=False):
                self.tank.rect.x = xpos
                self.tank.rect.y = ypos
            
            if pygame.sprite.spritecollide(self.tank, wall_group, dokill=False):
                self.tank.rect.x = xpos
                self.tank.rect.y = ypos
            projectil_groupe.update()
            pygame.display.update()    

    def map_gen(self):
        """
        Map generator function
        This function generate map and return player cordinats
        This function also generate wall and distructiable wall
        it devide the map as 16*12 grid each grid is 64*64
        x for non distructable wall
        d for distructable wall
        p2 for player 2 tank
        p1 for player 1 tank
        """
        tilesize = 64
        w_map = [
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ','p2',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x','d',' ',' ',' ',' ',' ','d','d',' ','d','d',' ',' ',' ',' ',' ',' ','d','x'],
        ['x',' ','d',' ',' ',' ',' ',' ','d',' ','d',' ',' ',' ',' ',' ',' ','d',' ','x'],
        ['x',' ',' ','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ',' ','x'],
        ['x',' ',' ',' ','d','d','d','d','d','d','d','d','d','d','d','d',' ',' ',' ','x'],
        ['x','x','d','x','d','d','d','d','x','x','x','d','d','d','d','d','x','d','x','x'],
        ['x',' ',' ',' ','d','d','d','d','d','d','d','d','d','d','d','d',' ',' ',' ','x'],
        ['x',' ',' ','d',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','d',' ',' ','x'],
        ['x',' ','d',' ',' ',' ',' ',' ','d',' ','d',' ',' ',' ',' ',' ',' ','d',' ','x'],
        ['x','d',' ',' ',' ',' ',' ','d','d',' ','d','d',' ',' ',' ',' ',' ',' ','d','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x',' ',' ',' ',' ',' ',' ',' ',' ','p1',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
        ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
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
                if col == 'p1':
                    p1 = (x,y)
                if col =='p2':
                    p2 = (x,y)
        
        return [p1, p2]

    def key_event_listener(self,Start_tick):
        
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()  #checking pressed keys
        if self.tank2.live_status == True: 
            if keys[pygame.K_w]:
                self.tank.rect.y -= 2
                self.tank.set_direction("up")
            elif keys[pygame.K_s]:
                self.tank.rect.y += 2
                self.tank.set_direction("down")
            elif keys[pygame.K_a]:
                self.tank.rect.x -= 2
                self.tank.set_direction("left")
            elif keys[pygame.K_d]:
                self.tank.rect.x += 2
                self.tank.set_direction("right")
            elif keys[pygame.K_f] and self.start-self.end1 > 2800:
                fire = pygame.mixer.Sound("sound/ATgun.ogg")
                pygame.mixer.Sound.set_volume(fire,0.1)
                pygame.mixer.Sound.play(fire)
                self.end1 = pygame.time.get_ticks() - Start_tick
                self.proj = self.tank.shoot_bullet()
                projectil_groupe.add(self.proj)

        if self.tank.live_status == True:
            if keys[pygame.K_UP]:
                self.tank2.rect.y -= 2
                self.tank2.set_direction("up")
            elif keys[pygame.K_DOWN]:
                self.tank2.rect.y += 2
                self.tank2.set_direction("down")
            elif keys[pygame.K_LEFT]:
                self.tank2.rect.x -= 2
                self.tank2.set_direction("left")
            elif keys[pygame.K_RIGHT]:
                self.tank2.rect.x += 2
                self.tank2.set_direction("right")
            elif keys[pygame.K_RCTRL] and self.start-self.end2 > 2800:
                fire = pygame.mixer.Sound("sound/ATgun.ogg")
                pygame.mixer.Sound.set_volume(fire,0.1)
                pygame.mixer.Sound.play(fire)
                self.end2 = pygame.time.get_ticks() - Start_tick
            
                self.proj = self.tank2.shoot_bullet()
                projectil_groupe.add(self.proj)       

