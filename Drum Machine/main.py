# Build your own beat maker
import pygame
from pygame import mixer

pygame.init()

# Screen
WIDTH = 1400
HEIGHT = 800

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('Drum Machine\Roboto-Bold.ttf', 32)

fps = 60
timer = pygame.time.Clock()

# Loop
run = True

while run:
    timer.tick(fps)
    screen.fill(black) # background
    
    for event in pygame.event.get():    # Any event
        if event.type == pygame.QUIT:
            run = False                    # Finish
    
    pygame.display.flip()
    
pygame.quit()