from turtle import back
import pygame 
from player import Player
from enemy import Enemy
from bullet import Bullet 
from explosion import Explosion
from welcome import Welcome

# Define values to be used in this program
FPS = 60
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Initialize pygame, and set the useful variables
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock() 

# Create a background image
background_image = pygame.image.load("images/road.png")

# Create different sprite groups for objects
all_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
enemy_sprite = pygame.sprite.Group()
bullet_sprite = pygame.sprite.Group()

# Create player object and add it in the player sprite group
player = Player()
all_sprite.add(player)
player_sprite.add(player)

# Loop enemy 2 times and load enemy images
for i in range(2):
    enemy1 = Enemy("images/enemy1.png")
    enemy2 = Enemy("images/enemy2.png")
    enemy3 = Enemy("images/enemy3.png")
    enemy4 = Enemy("images/enemy4.png")
    enemy5 = Enemy("images/enemy5.png")
    enemy6 = Enemy("images/enemy6.png")
    all_sprite.add(enemy1)
    enemy_sprite.add(enemy1)
    all_sprite.add(enemy2)
    enemy_sprite.add(enemy2)
    all_sprite.add(enemy3)
    enemy_sprite.add(enemy3)
    all_sprite.add(enemy4)
    enemy_sprite.add(enemy4)
    all_sprite.add(enemy5)
    enemy_sprite.add(enemy5)
    all_sprite.add(enemy6)
    enemy_sprite.add(enemy6)

# Dispay the welcome page
# welcome = True
# waiting = True
# while waiting:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         elif event.type == pygame.KEYUP:
#             waiting = False
# welcome = Welcome()


running = True

# Game loop
while running:
    # if welcome:
    #     welcome.show_welcome(screen)
    #     welcome = False

    clock.tick(FPS)

    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Make the backgrond auto move
    i = 0
    screen.blit(background_image, (i, 0))
    screen.blit(background_image, (SCREEN_WIDTH+i, 0))
    if (i == -SCREEN_WIDTH):
        screen.blit(background_image, (SCREEN_WIDTH+i, 0))
        i = 0
    i -=1

    # Receive events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                all_sprite.add(player.shoot())
                bullet_sprite.add(player.shoot())
                player.shoot()

    # Update game
    all_sprite.update()
    
    # If player hits enemy
    hits = pygame.sprite.groupcollide(enemy_sprite, player_sprite, True, True, collided = pygame.sprite.collide_mask)
    for hit in hits:
        explosionImage = Explosion(hit.rect.center)
        all_sprite.add(explosionImage)
            

    # Window display
    screen.fill((0,0,0)) # Reload the screen background
    screen.blit(background_image, (0,0))
    all_sprite.draw(screen)
    pygame.display.update()

pygame.quit()
