import pygame
from costanti import *

class Label:
    def __init__(self, x, y, surface, colorText, colorBackground, text, fontSize, font='freesansbold.ttf'):
        self.x = x
        self.y = y
        self.surface = surface
        self.colorText = colorText
        self.colorBackground = colorBackground
        self.text = text
        self.fontSize = fontSize
        self.font = font
        
    def create_label(self):
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.colorText, self.colorBackground)
        textRect = text.get_rect()
        return text, textRect
