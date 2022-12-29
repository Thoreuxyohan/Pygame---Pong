import pygame, sys

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up the main screen
screen_width = 1280
screen_height = 900
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == event.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.flip()
    clock.tick(60)
