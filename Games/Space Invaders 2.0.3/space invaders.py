import pygame
import random
import math
from pygame import mixer
# Website for Icons ----- Flaticon.com
# Website for Backgrounds ---- Freepik.com
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders 2.0.3")
# player
playerImage = pygame.image.load("spaceship.png")
# Background
background = pygame.image.load("background.png")
#background music
mixer.music.load("background.wav")
mixer.music.play(-1)
playerx = 370
playery = 480
player_x_change = 30
# Enemy
enemyImage = []
enemyX = []
enemyY = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load("monster (1).png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemy_x_change.append(15)
    enemy_y_change.append(40)
# Bullet
# Ready - We cannot see the bullet on the screen
# Fire - The bullet is currently moving
bulletImage = pygame.image.load("bullets.png")
bulletX = 0
bulletY = 480
bullet_x_change = 0
bullet_y_change = 25
bullet_state = "ready"

#Score
score = 0
Text = pygame.font.Font('freesansbold.ttf' ,32)

textX = 10
testY = 10
def show_Score(x,y):
    score_1 = Text.render("SCORE : "+str(score),True,(255,0,0))
    screen.blit(score_1, (x, y))
def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y,i):
    screen.blit(enemyImage[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:
    screen.fill((0, 0, 255))
    # Background Image
    background = pygame.image.load("background.png")
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -7
            if event.key == pygame.K_RIGHT:
                player_x_change = 7
            if event.key == pygame.K_SPACE:
                bulletX = playerx
                bullet_sound = mixer.Sound("laser.wav")
                bullet_sound.play()
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    # Player Movement
    playerx += player_x_change
    # Player Boundaries
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    # Enemy Boundaries
    for i in range(num_of_enemies):
        enemyX[i] += enemy_x_change[i]
        if enemyX[i] <= 0:
            enemy_x_change[i] = 20
            enemyY[i] += enemy_y_change[i]
        elif enemyX[i] >= 736:
            enemy_x_change[i] = -20
            enemyY[i] += enemy_y_change[i]

        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            enemy_sound = mixer.Sound("explosion.wav")
            enemy_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_y_change
    player(playerx, playery)
    show_Score(textX,testY)
    pygame.display.update()
