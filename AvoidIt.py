import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0,0,0)
PLAYER_COLOR = (255,0,0)
PLAYER_SIZE = 50
PLAYER_POS = [((WIDTH-PLAYER_SIZE)/2),HEIGHT-2*PLAYER_SIZE]

ENEMY_COLOR = (0,0,255)
ENEMY_SIZE = 50
ENEMY_POS = [random.randint(0, WIDTH-ENEMY_SIZE), 0]
ENEMY_SPEED = 5

ENEMY_LIST = [ENEMY_POS]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_over = False

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-ENEMY_SIZE)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))

def update_enemies_positions(enemy_list):
    for enemy_pos in enemy_list:
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += ENEMY_SPEED
        else:
            enemy_pos[0] = random.randint(0, WIDTH-ENEMY_SIZE)
            enemy_pos[1] = 0

def detect_collision(player_pos, enemy_list):
    for enemy_pos in enemy_list:
        px = player_pos[0]
        py = player_pos[1]
        ps = PLAYER_SIZE
        
        ex = enemy_pos[0]
        ey = enemy_pos[1]
        es = ENEMY_SIZE

        if (px <= ex+es and ex < px+ps) and (py <= ey+es and ey < py+ps):
            return True
        
    return False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(None)

        if event.type == pygame.KEYDOWN:
            x = PLAYER_POS[0]
            y = PLAYER_POS[1]

            if event.key == pygame.K_LEFT:
                x -= PLAYER_SIZE
            elif event.key == pygame.K_RIGHT:
                x += PLAYER_SIZE

            PLAYER_POS = [x,y]

    screen.fill(BACKGROUND_COLOR)

    # Updating the position of the enemy
    # if ENEMY_POS[1] >= 0 and ENEMY_POS[1] < HEIGHT:
    #     ENEMY_POS[1] += ENEMY_SPEED
    # else:
    #     ENEMY_POS[0] = random.randint(0, WIDTH-ENEMY_SIZE)
    #     ENEMY_POS[1] = 0

    drop_enemies(ENEMY_LIST)
    draw_enemies(ENEMY_LIST)
    update_enemies_positions(ENEMY_LIST)
    # pygame.draw.rect(screen, ENEMY_COLOR, (ENEMY_POS[0], ENEMY_POS[1], ENEMY_SIZE, ENEMY_SIZE))
    pygame.draw.rect(screen, PLAYER_COLOR, (PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE))

    if detect_collision(PLAYER_POS, ENEMY_LIST):
        print("Bum! Collided!!")
        game_over = True

    clock.tick(30)
    pygame.display.update()