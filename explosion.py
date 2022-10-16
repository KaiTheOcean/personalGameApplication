import pygame 

class Explosion(pygame.sprite.Sprite):
    # Create explosion images
    explosion = {}
    explosion['explosion'] = []
    for i in range(9):
        explosion_image = pygame.image.load(f"images/explosions/regularExplosion0{i}.png")
        explosion['explosion'].append(pygame.transform.scale(explosion_image, (75, 75)))

    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = Explosion.explosion['explosion'][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks() # The time from the begining till now
        self.frame_rate = 20 # Set the time from the picture to the next picture

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame ==len(Explosion.explosion['explosion']):
                self.kill()
            else:
                self.image = Explosion.explosion['explosion'][self.frame]
                center = self.rect.center
                self.center = self.image.get_rect()
                self.rect.center = center