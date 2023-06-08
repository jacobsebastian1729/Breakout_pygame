import pygame
from sys import exit

import random

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("My Game")

screen = pygame.display.set_mode((600,600))
screen.fill((20,20,20))

background = pygame.Surface((600,600))
background.fill((200,200,200))

test_surf1 = pygame.Surface((10,10))
test_surf1.fill((205,10,20))
test_surf1_rect = test_surf1.get_rect(center = (300,400))

test_surf2 = pygame.Surface((200,10))
test_surf2.fill((20,10,205))
test_surf2_rect = test_surf2.get_rect(center = (300,550))

##rect tiles:

rectangle_tiles = []

tup_array = []


for i in range(0,100):
    x_ = random.randint(0, ((300//25) -1))
    y_ = random.randint(0, ((200//25) -1))
    x = x_ * 25
    y = y_ * 25
    
    rect = pygame.Rect(x, y, 20,20)
    rectangle_tiles.append(rect)
    rect = pygame.Rect(600-x, y, 20,20)
    rectangle_tiles.append(rect)
step_y = 5
i = 0

step_x = 0
j = 0


collide12 = 1

move_left = False
move_right = False

red_rect_active = False

while True:

    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    ##click space to start the red rect move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                red_rect_active = True
    
    ##blue rect movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False
    
    if move_left:
        test_surf2_rect.x -= 4
        if test_surf2_rect.x <= 0:
            test_surf2_rect.x = 0
    if move_right:
        test_surf2_rect.x += 4
        if test_surf2_rect.x + 200 >= 600:
            test_surf2_rect.x = 400

    ##initeial set up background and two objects(blue and red rect)          
    screen.blit(background, (0,0))
    screen.blit(test_surf1, test_surf1_rect)
    screen.blit(test_surf2, test_surf2_rect)


    ## rectangle tiles
    for rect in rectangle_tiles:
        pygame.draw.rect(screen , (25, 150, 20), rect)

    


    if red_rect_active:

        ##rectangle tiles collision
        for index,rect in enumerate(rectangle_tiles):
            if rect.colliderect(test_surf1_rect):
                rectangle_tiles.pop(index)
                
        
        
        ## red rect y logic    
        test_surf1_rect.y += step_y

        if test_surf1_rect.y >= 590:
            step_y = -5
        elif test_surf1_rect.y <= 0:
            step_y = 5
        
        #test_surf1_rect.y = i

        ##red rect x logic
        test_surf1_rect.x += step_x

        if test_surf1_rect.x >= 590:
            step_x = step_x*(-1)
        elif test_surf1_rect.x <= 0:
            step_x = step_x*(-1)

            
        ##collidion between red and blue rect
        if test_surf1_rect.colliderect(test_surf2_rect):
            step_y = -5
            ts2_centroid = ((test_surf2_rect.x + (test_surf2_rect.width)/2))
            ts1_centroid = (test_surf1_rect.x + (10/2))
            step_x = 1 + ((ts1_centroid-ts2_centroid)//20)
            #print(step_x)

    
    
    

    
    #pygame.draw.rect(screen, (255, 0, 0), (i, i, 25,25))
    #if test_surf1.colliderect(test_surf2):
     #   print("collide")
    
    pygame.display.update()
    clock.tick(60)
