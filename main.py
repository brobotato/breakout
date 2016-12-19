__author__ = 'BrianUser'

import pygame
import math
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def render(x, y, sprite):
    gameDisplay.blit(sprite, (x, y))

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class paddle:
    x = 0
    y = 0

class ball:
    x = 0
    y = 0
    angle = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = True
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        paddle.x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        paddle.x += 5
    pygame.display.update()
    clock.tick(50)
    gameDisplay.fill()
pygame.quit()
quit()
