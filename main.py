__author__ = 'BrianUser'

import pygame
import math
import time

pygame.init()

display_width = 800
display_height = 600
pygame.display.set_caption('Breakout')
icon = pygame.sprite.Sprite()
icon.image = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon.image)

black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.Font("resources/vgaoem.fon", 15)
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
crashed = False
global playing
playing = False
level_name = "Level 1"

pygame.mixer.init()
bounce = pygame.mixer.Sound("resources/ball_bounce.wav")
destroy = pygame.mixer.Sound("resources/block_destroy.wav")

gameover = font.render("Game Over!", True, white)
gameover_rect = gameover.get_rect(center=(display_width / 2, display_height / 2))
victory = font.render("You Win!", True, white)
victory_rect = victory.get_rect(center=(display_width / 2, display_height / 2))
title = font.render("Breakout", True, white)
title_rect = title.get_rect(center=(display_width / 2, -10 + display_height / 2))
subtitle = font.render("Press Space to Start", True, white)
subtitle_rect = subtitle.get_rect(center=(display_width / 2, 10 + display_height / 2))
subtitle2 = font.render("Level Select", True, white)
subtitle2_rect = subtitle2.get_rect(center=(display_width / 2, 85 + display_height / 2))
level = font.render("{0}".format(level_name), True, white)
level_rect = level.get_rect(center=(display_width / 2, 100 + display_height / 2))


def collision(a, b, size):
    # returns true if the two values are within a certain range of each other
    if math.fabs(a - b) <= size:
        return True
    else:
        return False


def render(x, y, sprite):
    # just blit rewritten for convenience
    gameDisplay.blit(sprite, (x, y))


def move(x, y, angle, speed):
    # move something at an angle and speed
    x += math.cos(math.radians(angle)) * speed
    y += math.sin(math.radians(angle)) * speed
    return x, y


def rot_center(image, angle):
    # rotate an image while keeping its center and size
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def reset():
    # reset all game variables
    paddle.x = 400
    paddle.y = 500
    ball.x = 400
    ball.y = 400
    ball.angle = 90
    ball.side = 0
    ball.lives = 3
    playing = False
    return playing


def run():
    # execute game code
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        if paddle.x > 7:
            paddle.x -= 7
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        if paddle.x < 793:
            paddle.x += 7
    ball.x, ball.y = move(ball.x, ball.y, ball.angle, 8)
    if collision(paddle.x, ball.x, 32) & collision(paddle.y, ball.y, 16):
        if (ball.x - paddle.x) == 0:
            ball.angle = -90
        else:
            ball.angle = -90 + ((ball.x - paddle.x) * 90 / 32)
        bounce.play()
    if (ball.y <= 0) & (0 <= ball.x <= 800):
        ball.side = "ud"
    elif (ball.x <= 0 or ball.x >= 800) & (ball.y >= 0):
        ball.side = "lr"
    elif (ball.x <= 0) & (ball.y <= 0):
        ball.angle = 45
        bounce.play()
    elif (ball.x >= 800) & (ball.y <= 0):
        ball.angle = 135
        bounce.play()
    if ball.y > 600:
        if ball.lives > 0:
            ball.y = 400
            ball.x = 400
            paddle.x = 400
            ball.angle = 90
            ball.lives -= 1
            time.sleep(2)
        else:
            gameDisplay.blit(gameover, gameover_rect)
            pygame.display.update()
            playing = False
            return playing
    if blocks == []:
        gameDisplay.blit(victory, victory_rect)
        pygame.display.update()
        playing = False
        return playing
    for x in range(0, ball.lives, 1):
        render(x * 24 + 8, 576, ball.sprite.image)
    render(paddle.x - 32, paddle.y - 8, paddle.sprite.image)
    render(ball.x - 8, ball.y - 8, ball.sprite.image)
    for b in range(len(blocks)):
        if collision(ball.x, blocks[b][0], 16) & collision(ball.y, blocks[b][1], 16):
            if math.fabs(ball.y - blocks[b][1]) < math.fabs(ball.x - blocks[b][0]):
                ball.side = "lr"
                blocks[b][2] = True
                break
            else:
                ball.side = "ud"
                blocks[b][2] = True
                break
    for b in blocks:
        render(b[0] - 16, b[1] - 16, block.image)
    for b in blocks:
        if b[2] == True:
            destroy.play()
            blocks.remove(b)
    if ball.side != 0:
        if ball.side == "lr":
            ball.angle = math.copysign(180 - math.fabs(ball.angle), ball.angle)
        elif ball.side == "ud":
            ball.angle *= -1
        bounce.play()
        ball.side = 0


class paddle:
    x = 400
    y = 500
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("resources/paddle.png")


class ball:
    x = 400
    y = 400
    angle = 90
    side = 0
    lives = 3
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.image.load("resources/ball.png")


# block format = [x,y,set to be destroyed]
blocks = []
lvl1 = []
lvl2 = []
block = pygame.sprite.Sprite()
block.image = pygame.image.load("resources/block.png")
for x in range(64, 768, 32):
    for y in range(96, 256, 32):
        lvl1.append([x, y, False])
for y in range(96, 256, 32):
    lvl2.append([64, y, False])
for y in range(96, 256, 32):
    lvl2.append([128, y, False])
lvl2.append([96, 160, False])
for y in range(96, 256, 32):
    lvl2.append([192, y, False])
for x in range(224, 288, 32):
    lvl2.append([x, 96, False])
for x in range(224, 288, 32):
    lvl2.append([x, 160, False])
for x in range(224, 288, 32):
    lvl2.append([x, 224, False])
for y in range(96, 256, 32):
    lvl2.append([320, y, False])
for x in range(352, 416, 32):
    lvl2.append([x, 224, False])
for y in range(96, 256, 32):
    lvl2.append([448, y, False])
for x in range(480, 544, 32):
    lvl2.append([x, 224, False])
for y in range(96, 256, 32):
    lvl2.append([576, y, False])
for y in range(96, 256, 32):
    lvl2.append([640, y, False])
lvl2.append([608, 96, False])
lvl2.append([608, 224, False])
for y in range(96, 192, 32):
    lvl2.append([736, y, False])
lvl2.append([736, 224, False])
blocks = lvl1

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    if (pygame.key.get_pressed()[pygame.K_SPACE] != 0) & (playing == False):
        playing = True
    if (pygame.key.get_pressed()[pygame.K_1] != 0) & (playing == False):
        blocks = lvl1
        level_name = "Level 1"
    if (pygame.key.get_pressed()[pygame.K_2] != 0) & (playing == False):
        blocks = lvl2
        level_name = "Level 2"
    if playing == True:
        run()
    elif playing == False:
        level = font.render("{0}".format(level_name), True, white)
        level_rect = level.get_rect(center=(display_width / 2, 100 + display_height / 2))
        gameDisplay.blit(level, level_rect)
        gameDisplay.blit(title, title_rect)
        gameDisplay.blit(subtitle, subtitle_rect)
        gameDisplay.blit(subtitle2, subtitle2_rect)
    pygame.display.update()
    clock.tick(50)
    gameDisplay.fill(black)
pygame.quit()
quit()
