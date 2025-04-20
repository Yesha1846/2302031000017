import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Enemy")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 7

# Enemy
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("comicsans", 30)

def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos

    if (ex < px < ex + enemy_size or ex < px + player_size < ex + enemy_size) and \
       (ey < py < ey + enemy_size or ey < py + player_size < ey + enemy_size):
        return True
    return False

# Game loop
game_over = False
while not game_over:
    clock.tick(30)
    win.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Enemy movement
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

    # Check collision
    if detect_collision(player_pos, enemy_pos):
        text = font.render("Game Over!", True, (0, 0, 0))
        win.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        game_over = True
        break

    # Draw player and enemy
    pygame.draw.rect(win, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(win, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    pygame.display.update()
