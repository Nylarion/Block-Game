import random
import pygame


clock = pygame.time.Clock()
Y_limit = 720
X1_limit = 580 #Original value: 650
X2_limit = 790 #Original value: 880
stop_game = False
player_image = pygame.image.load("Snake/Assets/Textures/car.png")
auto_appearance = random.choice(["left", "right"])
vel_auto = 5
autos = []
autos_delete = []


def generate_pos():

    global auto_appearance
    
    if auto_appearance == "left":

        position = X1_limit

    elif auto_appearance == "right":

        position = X2_limit

    return position



def generate_autos(pantalla, player, game_fps):

    global x, y, stop_game

    if len(autos) == 0:

        x = generate_pos()
        y = 0 #Original value: -50

        autos.append([x, y, vel_auto])

    if len(autos) == 1:

        x1, y1, vel1 = autos[0]

        if y1 >= 450: #Original value: 350

            while True:
                
                x2 = generate_pos()

                if abs(x2 - x1) >= 0:

                    break
            autos.append([x2, 0, vel_auto])

    for i in range(len(autos)):

        x, y , vel = autos[i]

        
        if stop_game == False:
            
            y += vel

        elif stop_game == True:

            y = y

        if y > Y_limit:

            autos_delete.append(i)

        else:
            
            auto_enemy = pygame.Rect(x, y, 150, 200)
            pantalla.blit(player_image, auto_enemy)
            autos[i][1] = y

            if auto_enemy.colliderect(player): #LOSE COLIDER, IF PLAYER TOUCH A ENEMY, LOSE THE GAME

                #print("YOU LOSE!")
                stop_game = True


    for i in reversed(autos_delete):

        del autos[i]

    autos_delete.clear()
    return