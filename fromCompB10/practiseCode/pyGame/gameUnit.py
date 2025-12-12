import pygame
import random
import sys

pygame.init()

# Set the window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Basic 2D Game")

# Load the player image
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20)
player_speed = 5

# Load the enemy image
enemy_image = pygame.image.load("enemy.png")
enemies = []

# Enemy spawn timer
SPAWN_ENEMY_EVENT = pygame.USEREVENT
pygame.time.set_timer(SPAWN_ENEMY_EVENT, 1000)

# Game loop variables
FPS = 60
clock = pygame.time.Clock()

# Score
score = 0
SCORE_FONT = pygame.font.Font(None, 36)

def create_enemy():
    enemy_rect = enemy_image.get_rect()
    enemy_rect.topleft = (random.randint(0, WINDOW_WIDTH - enemy_rect.width), 0)
    enemies.append(enemy_rect)

def update_enemies():
    for enemy_rect in enemies[:]:
        enemy_rect.y += 5
        if enemy_rect.top > WINDOW_HEIGHT:
            enemies.remove(enemy_rect)

    for event in pygame.event.get():
        if event.type == SPAWN_ENEMY_EVENT:
            create_enemy()

def draw_player():
    screen.blit(player_image, player_rect)

def draw_score():
    score_surface = SCORE_FONT.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

def check_collision():
    for enemy_rect in enemies:
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def update_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_speed

def update_score():
    global score
    score += 1

def show_game_over():
    game_over_surface = SCORE_FONT.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_surface, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def update_game():
    update_player()
    update_enemies()
    update_score()
    if check_collision():
        show_game_over()

def draw_game():
    screen.fill((0, 0, 0))
    draw_player()

    for enemy_rect in enemies:
        screen.blit(enemy_image, enemy_rect)

    draw_score()

    pygame.display.flip()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    update_game()
    draw_game()
    clock.tick(FPS)