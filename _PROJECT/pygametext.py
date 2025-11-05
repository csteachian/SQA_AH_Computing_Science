import pygame, time

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(pygame.font.get_default_font(), 36)

# now print the text
text_surface = font.render('Hello world', True, (255, 255, 255))
screen.blit(text_surface, dest=(0,0))

pygame.display.flip()
time.sleep(3)
pygame.quit()
