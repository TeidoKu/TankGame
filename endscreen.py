import pygame
import pygame.locals
import sys
from helper import TextSurface
from helper import Export_json

class EndScreen():
    def __init__(self,winerP,endtime) -> None:
        self.winer=winerP
        self.endtime=endtime
        self.end_screen()

    def end_screen(self):  
        pygame.init()
        statictext = TextSurface().create_text_surface(f"Game Over The Winner is {self.winer}: (enter name here)")
        statictext2 = TextSurface().create_text_surface(f"When you are done press enter")
        self.clock = pygame.time.Clock()
        # it will display on screen
        self.window = pygame.display.set_mode([1280, 960])
        # basic font for user typed
        self.base_font = pygame.font.Font(None, 32)
        self.user_name = ''
        # create rectangle
        input_rect = pygame.Rect(450,960/2, 140, 32)
        # color_active stores color(lightskyblue3) which
        # gets active when input box is clicked by user
        color_active = pygame.Color('lightskyblue3')     
        # color_passive store color(chartreuse4) which is
        # color of input box.
        color_passive = pygame.Color('chartreuse4')
        color = color_passive  
        active = False
        running = True
        pygame.key.set_repeat(500,100)
        while running:
            for event in pygame.event.get():
            # if user types QUIT then the screen will close
                if event.type == pygame.locals.QUIT:
                    running = False
        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    #checks if user has pressed enter
                    if event.key == pygame.K_RETURN:
                        self.user_name
                        Export_json({'name':self.user_name,'role':self.winer,'time':self.endtime})
                        running = False
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        self.user_name = self.user_name[:-1]
                    elif len(self.user_name) < 10 and event.key != pygame.K_SPACE:
                        self.user_name += event.unicode
                        # Unicode standard is used for string
                        # formation
            
            # it will set background color of screen
            self.window.fill((255, 255, 255))
        
            if active:
                color = color_active
            else:
                color = color_passive
                
            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(self.window, color, input_rect)
        
            text_surface = self.base_font.render(self.user_name, True, (255, 255, 255))
            
            # render at position stated in arguments
            self.window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            self.window.blit(statictext, (450, 960/2 -50))
            self.window.blit(statictext2, (450, 960/2 +50))
            
            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width()+10)
            
            # display.flip() will update only a portion of the
            # screen to updated, not full area
            pygame.display.flip()
            self.clock.tick(60)
