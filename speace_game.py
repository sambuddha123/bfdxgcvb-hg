import math
import random
import pygame

s_w=800
s_h=500
p_s_x=370
p_s_y=300
e_s_x_min=50
e_s_y_max=150
e_s_x=4
e_s_y=40
b_s_y=10
c_d=27

pygame.init()
screen = pygame.display.set_mode((s_w, s_h))

bg=pygame.image.load("image.png")
p_img=pygame.image.load("download (4).png")
p_x=p_s_x
p_y=p_s_y
p_x_change=0
e_img=[]
en_x=[]
en_y=[]
en_x_change=[]
en_y_change=[]
num_en=6

for i in range(num_en):
    e_img.append(pygame.image.load("download (3).png"))
    en_x.append(random.randint(0,s_w-64))
    en_y.append(random.randint(e_s_y_max, s_h - e_s_y_max))
    en_x_change.append(e_s_x)
    en_y_change.append(e_s_y)

b_img=pygame.image.load("download (2).png")
b_x=0
b_y=p_s_y
b_x_change=0
b_y_change=b_s_y
b_state="ready"

score=0
font=pygame.font.Font("freesansbold.ttf", 32)
text_x=10
text_y=10
over=pygame.font.Font("freesansbold.ttf", 64)
def show_score(x, y):
    score_display = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_display, (x, y))

def game_over_text():
    over_text = over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(p_img, (x, y))

def enemy(x, y, i):
    screen.blit(e_img[i], (x, y))

def fire_bullet(x, y):
    global b_state
    b_state = "fire"
    screen.blit(b_img, (x + 16, y + 10))

def is_collision(en_x, en_y, b_x, b_y):
    distance = math.sqrt((en_x - b_x) ** 2 + (en_y - b_y) ** 2)
    return distance < c_d

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_x_change = -5
            if event.key == pygame.K_RIGHT:
                p_x_change = 5
            if event.key == pygame.K_SPACE and b_state == "ready":
                b_x= p_x
                b_y= p_y
                b_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p_x_change = 0 

    p_x += p_x_change
    p_x = max(0, min(p_x, s_w - 64))

    for i in range(num_en):
        if en_y[i]>340:
            for j in range(num_en):
                en_y[j] = 2000
            game_over_text()
            break
        en_x[i]+= en_x_change[i]
        if en_x[i]<= 0 or en_x[i] >= s_w - 64:
            en_x_change[i] *= -1
            en_y[i] += en_y_change[i]
        
        if is_collision(en_x[i], en_y[i], b_x, b_y):
            b_y = p_s_y
            b_state = "ready"
            score += 1
            en_x[i] = random.randint(0, s_w - 64)
            en_y[i] = random.randint(e_s_y_max, s_h - e_s_y_max)

        enemy(en_x[i], en_y[i], i)

    if b_state == "fire":
        fire_bullet(b_x, b_y)
        b_y -= b_y_change
        if b_y <= 0:
            b_y = p_s_y
            b_state = "ready"
    
    player(p_x, p_y)
    show_score(text_x, text_y)
    pygame.display.update()
