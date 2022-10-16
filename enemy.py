import pygame 
import os
import random 

class Enemy(pygame.sprite.Sprite):
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500

    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect() # Get the enemy rect
        # self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = random.randrange(0, Enemy.SCREEN_HEIGHT - self.rect.height) # Have the enemy start at a random location from left
        self.rect.x = 0 # Set the enemy all start at the very right
        self.speed = random.randrange(1, 4) # Give the enemy a random speed

    def update(self):
        self.rect.x += self.speed 
        
        # Reset the enemy when it reaches the right side of the screen
        if self.rect.left > Enemy.SCREEN_WIDTH:
            self.rect.y = random.randrange(50, Enemy.SCREEN_HEIGHT - self.rect.height) # Have the enemy start at a random location from left
            self.rect.x = 0 # Set the enemy all start at the very right
            self.speed = random.randrange(1, 4) # Give the enemy a random speed


