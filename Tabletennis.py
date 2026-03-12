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
changexy1 = 5
#racket one
y_coordinate = 190
x_coordinate = 60
changexy = 5
#ball
y_coordinate2 = 330
x_coordinate2 = 385
changexy2 = 4
changexy3 = 4
#racket
racket_img = pygame.image.load("table-tennis-racket2.png")
racket2_img = pygame.image.load("table-tennis-racket2.png")
ball = pygame.image.load("ball2.png")
def racket(move_x,move_y):
    grid.blit(racket_img,(move_x,move_y))
def racket2(move_x,move_y):
    grid.blit(racket2_img,(move_x,move_y))
def table_tennis_ball(move_x,move_y):
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
background = pygame.image.load("table.png")
background = pygame.transform.scale(background,(800,600))
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.QUIT:
           var = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                changexy = 5
            if event.key == pygame.K_UP:
                changexy = -5
        grid.blit(background, (0, 0))
        pygame.display.update()
    y_coordinate += changexy
    if y_coordinate <=0:
        y_coordinate = 0
    elif y_coordinate >= 500:
        y_coordinate = 500
    if y_coordinate1 < y_coordinate2:
        y_coordinate1 += changexy1
    elif y_coordinate1 > y_coordinate2:
        y_coordinate1 -= changexy1
    if x_coordinate2 <= 0:
        x_coordinate2 = 1
        changexy2 = 5
        score += 1
        print("Enemy point:",score)
        if score == 6:
            print("Match point!")
            font = pygame.font.Font(None, 50)
            message = font.render("Match Point!", True, (255,0,0))
            grid.blit(message, (300,200))
            pygame.display.update()
        if score == 7:
            print("Done")
            font = pygame.font.Font(None, 50)
            message = font.render("Done!", True, (255,0,0))
            grid.blit(message, (300,200))
            pygame.display.update()
    elif x_coordinate2 >= 736:
        changexy2 = -5
        score += 1
        print("Your point:",score)
        if score == 6:
            print("Match point!")
            font = pygame.font.Font(None, 50)
            message = font.render("Match Point!", True, (255,0,0))
            grid.blit(message, (300,200))
            pygame.display.update()
        if score == 7:
            print("Done!")
            font = pygame.font.Font(None, 50)
            message = font.render("Done!", True, (255,0,0))
            grid.blit(message, (300,200))
            pygame.display.update()
    x_coordinate2 += changexy2
    if y_coordinate2 <= 0:
        y_coordinate2 = 1
        changexy3 = 5
        score += 1
    elif y_coordinate2 >= 570:
        changexy3 = -5
        score += 1
    y_coordinate2 += changexy3
    hit_ball = collide1(x_coordinate2,y_coordinate2,x_coordinate,y_coordinate)
    if hit_ball:
        changexy2 = 5
    hit_ball1 = collide2(x_coordinate2,y_coordinate2,x_coordinate1,y_coordinate1)
    if hit_ball1:
        changexy2 = -5
    x_coordinate2 += changexy2
    grid.blit(background,(0,0))
    racket(x_coordinate,y_coordinate)
    racket2(x_coordinate1,y_coordinate1)
    table_tennis_ball(x_coordinate2,y_coordinate2)
    pygame.display.update()
pygame.quit()
  
