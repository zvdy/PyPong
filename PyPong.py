# pong terminal game pygame

import pygame
import sys
import random

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# title 
pygame.display.set_caption("Pong")

# player
player = pygame.Rect(700, 250, 10, 100)

# enemy
enemy = pygame.Rect(50, 250, 10, 100)

# ball
ball = pygame.Rect(400, 300, 10, 10)

# player speed
player_speed = 0

# enemy speed
enemy_speed = 0

# ball speed
ball_speed_x = 5
ball_speed_y = 5

# background color
bg_color = pygame.Color("grey12")

# white color
white_color = pygame.Color("white")

# clock
clock = pygame.time.Clock()

# font
font = pygame.font.Font("freesansbold.ttf", 32)

# score
player_score = 0
enemy_score = 0

# text
player_text = font.render(str(player_score), True, white_color)
enemy_text = font.render(str(enemy_score), True, white_color)

# text rect
player_text_rect = player_text.get_rect(center = (700, 50))
enemy_text_rect = enemy_text.get_rect(center = (100, 50))

# game loop
while True :
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 7
                if event.key == pygame.K_UP:
                    player_speed -= 7
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7
    
        # ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y
    
        # enemy movement
        if ball.y > enemy.y + 50:
            enemy.y += 5
        if ball.y < enemy.y + 50:
            enemy.y -= 5
    
        # ball collision
        if ball.top <= 0 or ball.bottom >= 600:
            ball_speed_y *= -1
    
        # player collision
        if ball.colliderect(player) and ball_speed_x > 0:
            ball_speed_x *= -1
    
        # enemy collision
        if ball.colliderect(enemy) and ball_speed_x < 0:
            ball_speed_x *= -1
    
        # player score
        if ball.left <= 0:
            player_score += 1
            player_text = font.render(str(player_score), True, white_color)
            player_text_rect = player_text.get_rect(center = (700, 50))
            ball.center = (400, 300)
            ball_speed_x *= -1
    
        # enemy score
        if ball.right >= 800:
            enemy_score += 1
            enemy_text = font.render(str(enemy_score), True, white_color)
            enemy_text_rect = enemy_text.get_rect(center = (100, 50))
            ball.center = (400, 300)
            ball_speed_x *= -1
    
        # player movement
        player.y += player_speed
    
        # player boundary
        if player.top <= 0:
            player.top = 0
        if player.bottom >= 600:
            player.bottom = 600
    
        # enemy boundary
        if enemy.top <= 0:
            enemy.top = 0
        if enemy.bottom >= 600:
            enemy.bottom = 600
    
        # background color
        screen.fill(bg_color)
    
        # draw player
        pygame.draw.rect(screen, white_color, player)

        # draw enemy
        pygame.draw.rect(screen, white_color, enemy)

        # draw ball
        pygame.draw.rect(screen, white_color, ball)

        # draw score
        screen.blit(player_text, player_text_rect)
        screen.blit(enemy_text, enemy_text_rect)

        # update screen
        pygame.display.flip()

        # fps
        clock.tick(60)