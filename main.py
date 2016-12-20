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
crashed = False


def collision(a, b, size):
    """returns true if the two values are within a certain range of each other"""
    if math.fabs(a - b) <= size:
        return True
    else:
        return False


def render(x, y, sprite):
    """just blit rewritten for convenience"""
    gameDisplay.blit(sprite, (x, y))


def move(x, y, angle, speed):
    """move something at an angle and speed"""
    x += math.cos(math.radians(angle)) * speed
    y += math.sin(math.radians(angle)) * speed
    return x, y


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


class paddle:
    x = 400
    y = 500
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("paddle.png")


class ball:
    x = 400
    y = 300
    angle = 90
    side = 0
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("ball.png")

"""block format = [x,y,set to be destroyed]"""
blocks = []
block = pygame.sprite.Sprite()
block.image = pygame.image.load("block.png")

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        paddle.x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        paddle.x += 5
    ball.x, ball.y = move(ball.x, ball.y, ball.angle, 8)
    if collision(paddle.x, ball.x, 32) & collision(paddle.y, ball.y, 16):
        if (ball.x - paddle.x) == 0:
            ball.angle = -90
        else:
            ball.angle = -90 + ((ball.x - paddle.x) * 90 / 32)
    if ball.y < 0:
        ball.side = "ud"
    if ball.x < 0 or ball.x > 800:
        ball.side = "lr"
    render(paddle.x - 32, paddle.y - 8, paddle.sprite.image)
    render(ball.x - 8, ball.y - 8, ball.sprite.image)
    for b in range(len(blocks)):
        if collision(ball.x, blocks[b][0], 16) & collision(ball.y, blocks[b][1], 16):
            if math.fabs(ball.y-blocks[b][1]) > math.fabs(ball.x-blocks[b][0]):
                ball.side = "ud"
                blocks[b][2] = True
                break
            else:
                ball.side = "lr"
                blocks[b][2] = True
                break
    for b in blocks:
        render(b[0] - 16, b[1] - 16, block.image)
    for b in blocks:
        if b[2] == True:
            blocks.remove(b)
    if ball.side == "lr":
        ball.angle = math.copysign(180 - math.fabs(ball.angle), ball.angle)
        ball.side = 0
    if ball.side == "ud":
        ball.angle *= -1
        ball.side = 0
    pygame.display.update()
    clock.tick(50)
    gameDisplay.fill(black)
pygame.quit()
quit()
