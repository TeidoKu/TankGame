import pygame
import sys
import pygame.locals 
from tank_game import Game

# I want a start screen that has a button that when clicked

class StartScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 960))
        self.background = pygame.image.load("img/background.jpg")
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.button = pygame.image.load("img/start.png")
        self.button = pygame.transform.scale(self.button, (300, 300))
        self.button_rect = self.button.get_rect()
        self.button_rect.center = (640, 800)
        self.running = True

    def start_screen(self):
        pygame.init()
        pygame.mixer.music.load("sound/title.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        while self.running:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()
            self.screen.blit(self.background, (0, 150))
            self.screen.blit(self.button, self.button_rect)
            pygame.display.update()
            self.key_event_listener()
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    self.running = False
                    game = Game()
                    game.game_loop(pygame.time.get_ticks())
                    
            



    def key_event_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.running = False
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.running = False

# if __name__ == "__main__":
#     pygame.init()
#     start_screen = StartScreen()
#     start_screen.start_screen()
    #when button is clicked, start tank_game.py
    


