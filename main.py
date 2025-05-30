import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

ball = pygame.Rect(400, 550, 20, 20)
target = pygame.Rect(random.randint(0, 780), random.randint(0, 200), 40, 40)

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
        if ball.colliderect(target):
            score += 1
            target.x = random.randint(0, 780)
            target.y = random.randint(0, 200)
            ball.y = 550
            throwing = False
        elif ball.y < 0:
            ball.y = 550
            throwing = False

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), target)
    pygame.draw.ellipse(screen, (0, 255, 0), ball)
    
    pygame.display.flip()
    clock.tick(60)
