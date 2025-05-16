import pygame
import random

def check_collision(ball_rect, target_rect):
    return ball_rect.colliderect(target_rect)

def get_new_target_position(screen_width, screen_height, target_size):
    x = random.randint(0, screen_width - target_size)
    y = random.randint(0, screen_height - target_size)
    return x, y

