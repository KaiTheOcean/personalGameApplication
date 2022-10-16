import pygame 
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png")# Get the player image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect() # Get the player's rect
        self.rect.centery = Player.SCREEN_HEIGHT/2  # Center the player's y coordinate
        self.rect.right = Player.SCREEN_WIDTH - 15 # Set the right position of the player
        self.speed = 4 # Set the player's movement speed
        self.boost = 5 # Boost the player speed

    def update(self):
        '''update method, allows player to move'''
        key_pressed = pygame.key.get_pressed() # Catch the key pressed event (if pressed return True, else False)

        # Control the player
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if key_pressed[pygame.K_SPACE]:
                self.rect.x += self.boost
        elif key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if key_pressed[pygame.K_SPACE]:
                self.rect.x -= self.boost
        elif key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
            if key_pressed[pygame.K_SPACE]:
                self.rect.y -= self.boost
        elif key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
            if key_pressed[pygame.K_SPACE]:
                self.rect.y += self.boost
        
        # Limit the player in the window screen
        if self.rect.right > Player.SCREEN_WIDTH:
            self.rect.right = Player.SCREEN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.top < 50:
            self.rect.top = 50
        elif self.rect.bottom > Player.SCREEN_HEIGHT - 50:
            self.rect.bottom = Player.SCREEN_HEIGHT - 50
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        return bullet