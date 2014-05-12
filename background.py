import pygame

class Background(object):
    
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
    def update(self):
        pass
        