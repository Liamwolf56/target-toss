import pygame
import random
import math
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Asset paths
ASSET_DIR = os.path.join(os.path.dirname(__file__), '../assets')
BACKGROUND_PATH = os.path.join(ASSET_DIR, 'background.jpg')
BALL_PATH = os.path.join(ASSET_DIR, 'ball.png')
TARGET_PATH = os.path.join(ASSET_DIR, 'target.jpg')

# Game settings
BALL_RADIUS = 15
TARGET_RADIUS = 30
GRAVITY = 0.4
POWER_MULTIPLIER = 0.5
MAX_POWER = 100
ROUND_TIME = 60  # seconds

# Load assets
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Toss")
background_img = pygame.image.load(BACKGROUND_PATH).convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
ball_img = pygame.image.load(BALL_PATH).convert_alpha()
ball_img = pygame.transform.scale(ball_img, (BALL_RADIUS * 2, BALL_RADIUS * 2))
target_img = pygame.image.load(TARGET_PATH).convert()
target_img = pygame.transform.scale(target_img, (TARGET_RADIUS * 2, TARGET_RADIUS * 2))

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

# Game objects
class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.vx = 0
        self.vy = 0
        self.active = False

    def update(self):
        if self.active:
            self.vy += GRAVITY
            self.x += self.vx
            self.y += self.vy
            if self.y > HEIGHT or self.x < 0 or self.x > WIDTH:
                self.reset()

    def draw(self):
        screen.blit(ball_img, (self.x - BALL_RADIUS, self.y - BALL_RADIUS))

class Target:
    def __init__(self):
        self.reposition()

    def reposition(self):
        self.x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
        self.y = random.randint(TARGET_RADIUS, HEIGHT // 2)

    def draw(self):
        screen.blit(target_img, (self.x - TARGET_RADIUS, self.y - TARGET_RADIUS))

# Game functions
def draw_power_bar(power):
    pygame.draw.rect(screen, BLACK, (20, HEIGHT - 40, MAX_POWER * 2, 20), 2)
    pygame.draw.rect(screen, RED, (20, HEIGHT - 40, power * 2, 20))

def draw_trajectory(ball, mouse_pos):
    dx = mouse_pos[0] - ball.x
    dy = mouse_pos[1] - ball.y
    angle = math.atan2(dy, dx)
    power = min(int(math.hypot(dx, dy) * POWER_MULTIPLIER), MAX_POWER)
    vx = math.cos(angle) * power
    vy = math.sin(angle) * power
    
    points = []
    x, y = ball.x, ball.y
    for _ in range(30):
        vy += GRAVITY
        x += vx
        y += vy
        points.append((int(x), int(y)))
        if y > HEIGHT:
            break
    if len(points) > 1:
        pygame.draw.lines(screen, RED, False, points, 2)

def draw_text(text, x, y, center=True):
    img = font.render(text, True, BLACK)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(img, rect)

def main():
    ball = Ball()
    target = Target()
    score = 0
    high_score = 0
    power = 0
    charging = False
    start_time = pygame.time.get_ticks()
    game_over = False

    running = True
    while running:
        screen.blit(background_img, (0, 0))

        current_time = pygame.time.get_ticks()
        elapsed = (current_time - start_time) // 1000
        time_left = max(0, ROUND_TIME - elapsed)

        if time_left <= 0:
            game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not ball.active and not game_over:
                charging = True
                power = 0

            if event.type == pygame.MOUSEBUTTONUP and charging:
                charging = False
                dx = pygame.mouse.get_pos()[0] - ball.x
                dy = pygame.mouse.get_pos()[1] - ball.y
                angle = math.atan2(dy, dx)
                ball.vx = math.cos(angle) * power
                ball.vy = math.sin(angle) * power
                ball.active = True

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    ball.reset()
                    target.reposition()
                    score = 0
                    start_time = pygame.time.get_ticks()
                    game_over = False

        if charging:
            power = min(power + 1, MAX_POWER)

        ball.update()

        # Check hit
        if not game_over and ball.active:
            dist = math.hypot(ball.x - target.x, ball.y - target.y)
            if dist <= BALL_RADIUS + TARGET_RADIUS:
                score += 1
                if score > high_score:
                    high_score = score
                target.reposition()
                ball.reset()

        # Draw
        target.draw()
        ball.draw()
        draw_text(f"Score: {score}", 10, 10, center=False)
        draw_text(f"High Score: {high_score}", WIDTH - 180, 10, center=False)
        draw_text(f"Time Left: {time_left}", WIDTH // 2, 20)
        if charging:
            draw_power_bar(power)
            draw_trajectory(ball, pygame.mouse.get_pos())

        if game_over:
            draw_text("Game Over! Press R to Restart", WIDTH // 2, HEIGHT // 2 + 30)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
