import pygame
import sys
import pygame.locals 
from tank_game import Game

# I want a start screen that has a button that when clicked

class StartScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load("img/startscreen.jpg")
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.button = pygame.image.load("img/dwall.png")
        self.button = pygame.transform.scale(self.button, (200, 100))
        self.button_rect = self.button.get_rect()
        self.button_rect.center = (400, 300)
        self.running = True

    def start_screen(self):
        while self.running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.button, self.button_rect)
            pygame.display.update()
            self.key_event_listener()
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.running = False
                    game = Game()
                    game.game_loop()
                    
            



    def key_event_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                self.running = False
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.running = False

if __name__ == "__main__":
    pygame.init()
    start_screen = StartScreen()
    start_screen.start_screen()
    #when button is clicked, start tank_game.py
    


