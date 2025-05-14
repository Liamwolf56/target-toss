import pygame
from game.logic import check_collision
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball = pygame.Rect(400, 550, 20, 20)
target = pygame.Rect(random.randint(0, 760), random.randint(0, 200), 40, 40)
throwing = False
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not throwing:
            throwing = True

    if throwing:
        ball.y -= 10
        if check_collision(ball, target):
            score += 1
            target.x = random.randint(0, 760)
            target.y = random.randint(0, 200)
            ball.y = 550
            throwing = False
        elif ball.y < 0:
            ball.y = 550
            throwing = False

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), target)
    pygame.draw.ellipse(screen, (0, 255, 0), ball)
    pygame.display.set_caption(f"Target Toss | Score: {score}")
    pygame.display.flip()
    clock.tick(60)
