import random
import sys
import pygame
from pygame.locals import *

fps = 32 
screenwidth = 285
screenheight = 511
screen = pygame.display.set_mode((screenwidth, screenheight))
ground = screenheight * 0.8
game_sprite ={}
game_sound ={}
player ='flappy-bird-assets\sprites/bird.png'
pipe ='flappy-bird-assets\sprites/pipe-red.png' 
ground = 'flappy-bird-assets\sprites/ base.png'

if __name__ == '__main__':
    pygame.init()
    fps = pygame.time.Clock()
    pygame.display.set_caption ('flappy')
    game_sprite['numbers'] = (
        pygame.image.load('flappy-bird-assets\sprites/1.png') .convet_alpha()
        
        
    
    )

game_sprite['base'] = pygame.image.load('flappy-bird-assets\sprites/ base.png') .convet_alpha()
game_sprite['pipe'] =(Pygame.transform.rotate(pipe).convet_alpha() ,180)
pygame.image.load(pipe).convet_alpha()

