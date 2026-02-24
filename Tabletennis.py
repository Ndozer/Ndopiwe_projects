import pygame
import random
import math
pygame.init()

grid = pygame.display.set_mode((800,600))
#Display
pygame.display.set_caption("Pixel|Table Tennis")
ico = pygame.image.load("table-tennis.png")
pygame.display.set_icon(ico)

#racket two
y_coordinate1 = 190
x_coordinate1 = 650
changexy1 = 0.8
#racket one
y_coordinate = 190
x_coordinate = 60
changexy = 0
#ball
y_coordinate2 = 330
x_coordinate2 = 385
changexy2 = 1
changexy3 = 1
#racket
def racket(move_x,move_y):
 racket = pygame.image.load("table-tennis-racket2.png")
 grid.blit(racket,(move_x,move_y))
def racket2(move_x,move_y):
 racket2 = pygame.image.load("table-tennis-racket2.png")
 grid.blit(racket2,(move_x,move_y))
def table_tennis_ball(move_x,move_y):
 ball = pygame.image.load("ball2.png")
 grid.blit(ball,(move_x,move_y))
def collide1(x_coordinate2,y_coordinate2,x_coordinate,y_coordinate):
 meet_point = math.sqrt((math.pow(x_coordinate2 - x_coordinate,2)) + (math.pow(y_coordinate2-y_coordinate,2)))
 if meet_point < 57:
     return True
 else:
     return False
def collide2(x_coordinate2,y_coordinate2,x_coordinate1,y_coordinate1):
 meet_point = math.sqrt((math.pow(x_coordinate2 - x_coordinate1,2)) + (math.pow(y_coordinate2-y_coordinate1,2)))
 if meet_point < 50:
     return True
 else:
     return False
#Tab control
score = 0
var = True
while var:
    for cancel in pygame.event.get():
        if cancel.type == pygame.QUIT:
           var = False
        if cancel.type == pygame.KEYDOWN:
            if cancel.key == pygame.K_DOWN:
                changexy = 1
            if cancel.key == pygame.K_UP:
                changexy = -1
    y_coordinate += changexy
    if y_coordinate <=0:
        y_coordinate = 0
    elif y_coordinate >= 500:
        y_coordinate = 500
    if y_coordinate1 <= 0:
        y_coordinate1 = 1
        changexy1 = 1
    elif y_coordinate1 >= 500:
        changexy1 = -1
    y_coordinate1 += changexy1
    if x_coordinate2 <= 0:
        x_coordinate2 = 1
        changexy2 = 1
        score += 1
        print("Enemy point:",score)
        if score == 6:
            print("Match point!")
        if score == 7:
            print("Done")
    elif x_coordinate2 >= 736:
        changexy2 = -1
        score += 1
        print("Your point:",score)
        if score == 6:
            print("Match point!")
        if score == 7:
            print("Done")
    x_coordinate2 += changexy2
    if y_coordinate2 <= 0:
        y_coordinate2 = 1
        changexy3 = 1
        score += 1
    elif y_coordinate2 >= 570:
        changexy3 = -1
        score += 1
    y_coordinate2 += changexy3
    hit_ball = collide1(x_coordinate2,y_coordinate2,x_coordinate,y_coordinate)
    if hit_ball:
        changexy2 = 1
    hit_ball1 = collide2(x_coordinate2,y_coordinate2,x_coordinate1,y_coordinate1)
    if hit_ball1:
        changexy2 = -1
    x_coordinate2 += changexy2
    grid.fill((255,255,255))
    racket(x_coordinate,y_coordinate)
    racket2(x_coordinate1,y_coordinate1)
    table_tennis_ball(x_coordinate2,y_coordinate2)
    pygame.display.update()
pygame.quit()
  
