import pygame


class TextSurface():
    def __init__(self):
        """This function creates a surface and renders the text argument in it"""
        # Get the default font for the system
    def create_text_surface(self,text):
        self.text = text
        self.default_font = pygame.font.get_default_font()
        font = pygame.font.Font(self.default_font, 24)
        self.text_surface = font.render(self.text, True, (0, 0, 0))
        return self.text_surface