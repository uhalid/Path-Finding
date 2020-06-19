#button for pygame
import pygame
from  costanti import *
from labels import *

class Button():
    def __init__(self, x, y, height, width, surface, textColor, backgroundColor, text,  function = None, fontSize= 20, font='freesansbold.ttf'):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.surface = surface
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.text = text
        self.function = function
        self.fontSize = fontSize
        self.font = font
        self.border = None  
    
        
    def create(self):
        
        #draw border
        if self.border:
            pygame.draw.rect(self.surface, border, (self.x-2, self.y -
                                            2, self.width+4, self.height+4), 0)

        #draw  the button
        pygame.draw.rect(self.surface, self.backgroundColor, (self.x, self.y,
                                           self.width, self.height), 0)


        
        font = pygame.font.SysFont(self.font, self.fontSize)
        text = font.render(self.text, 1, self.textColor)
        self.surface.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                        self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #check  if the mouse is over the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
