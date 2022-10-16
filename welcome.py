import pygame 

class Welcome():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 500
    font_name = pygame.font.match_font("arial")
    def __init__(self):
        pass

    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(Welcome.font_name, size)
        text_surface = font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surface, text_rect)

    def show_welcome(surf):
        Welcome.draw_text(surf, "Racing Car", 64, Welcome.SCREEN_WIDTH/2, Welcome.SCREEN_HEIGHT/4)
        Welcome.draw_text(surf, "up, down, left, and right arrow to move. Space to boost speed", 30, Welcome.SCREEN_WIDTH/2, Welcome.SCREEN_HEIGHT/2)
        Welcome.draw_text(surf, "Press any key to start the game", 18, Welcome.SCREEN_WIDTH/2, Welcome.SCREEN_HEIGHT/6)
        pygame.display.update()

            
