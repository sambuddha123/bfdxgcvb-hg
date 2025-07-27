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
    e_img.append(pygame.image.load("enemy.png"))
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
    score= font.render("Score: " + str(score), True, (255, 255, 255))
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

