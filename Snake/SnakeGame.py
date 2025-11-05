import pygame
import random
import sys
import Spawn_Cars
import PointsPlayer
pygame.init()


#---Variables---#
Ancho = 980
Alto = 720
game_fps = 26
color_fondo = (126, 143, 131)
font = pygame.font.Font('Snake/Assets/Font/slkscr.ttf', 30)
font_bigger = pygame.font.Font('Snake/Assets/Font/slkscr.ttf', 70)
clock = pygame.time.Clock()
level = 0
paused = False
show_texture = False
running = True
lvl_flag = False
maxlvl_flag = False
flag_frame = False
current_frame = 0
frame_time = 350
counter_time = 0
movimiento = False
update = pygame.time.get_ticks()
#----------------#

#---Textures---#
icon_image = pygame.image.load("Snake/Assets/Textures/icon.png")
player_image = pygame.image.load("Snake/Assets/Textures/car.png")
player = pygame.Rect(0, 720, 150, 200) #POS X, Y / Ancho y Alto
paused_image = pygame.image.load("Snake/Assets/Textures/paused.png")
paused_in_game = pygame.Rect(585,300, 100, 350)
stopPaused_image = pygame.image.load("Snake/Assets/Textures/stop-paused.png")
options_image = pygame.image.load("Snake/Assets/Textures/options.png")
options_in_game = pygame.Rect(0, 520, 200, 350)
points_image = pygame.image.load("Snake/Assets/Textures/point-level.png")
points_in_game = pygame.Rect(0, 0, 400, 150)
newLevel_image = pygame.image.load("Snake/Assets/Textures/new-level.png")
newLevel_ingame = pygame.Rect(585,300, 100, 350)
border_image = pygame.image.load("Snake/Assets/Textures/border.png")
border_in_game = pygame.Rect(550, 0, 417, 720)
explosionC1 = pygame.image.load("Snake/Assets/Textures/explosion1.png")
explosionC2 = pygame.image.load("Snake/Assets/Textures/explosion2.png")
frame = [explosionC1, explosionC2]
#--------------#

mainWindow = pygame.display.set_mode((Ancho, Alto))
pygame.display.set_caption("RaceCars PORT PC")
pygame.display.set_icon(icon_image)

#def explosion():

    #global update, frame_time, current_frame, frame
    #if Spawn_Cars.stop_game == True:
    
        #now = pygame.time.get_ticks()
        #if now - update > frame_time:

            #current_frame = (current_frame + 1) % len(frame)
            #update = now


        #mainWindow.blit(frame[current_frame], player)
    #return


def paused_game():

    global show_texture, paused

    if show_texture == True:
        mainWindow.blit(paused_image, paused_in_game)
        mainWindow.blit(stopPaused_image, options_in_game)
        paused = True
    return


def level_texture():

    global lvl_flag, maxlvl_flag, font_bigger, level

    text_newLvl = font_bigger.render(f'{int(level)}', True, (2, 31, 11))
    text_maxLvl = font.render(f'MAX', True, (2, 31, 11))

    if lvl_flag == True:

        mainWindow.blit(newLevel_image, newLevel_ingame)
        mainWindow.blit(text_newLvl, (855,320))

    if maxlvl_flag == True:

        mainWindow.blit(newLevel_image, newLevel_ingame)
        mainWindow.blit(text_newLvl, (855,305))
        mainWindow.blit(text_maxLvl, (845,360))


    if PointsPlayer.puntos_player in [550, 1550, 2550, 3550, 4550, 5550, 6550, 7550, 8550, 9550]:

        lvl_flag = True

    elif PointsPlayer.puntos_player == 10550:

        maxlvl_flag = True

    elif PointsPlayer.puntos_player in [650, 1700, 2750, 3800, 4850, 5900, 6950, 8000, 8850, 9900, 10950]:

        lvl_flag = False
        maxlvl_flag = False

    return


def movimiento_arriba():

    global counter_time

    counter_time += 1

    if counter_time == 10:

        player.y -= 20
        counter_time = 0


#def level_enemyPOS():

    #global level

    #Spawn_Cars.generate_autos(mainWindow, player, game_fps)

    #if PointsPlayer.puntos_player <= 350:

        #Spawn_Cars.auto_appearance = random.choice(["left", "right"])

    #elif PointsPlayer.puntos_player in [400, 450, 550, 1400, 1450, 1550, 2400, 2450, 2550, 3400, 3450, 3550, 4400, 4450, 4550,
        #5400, 5450, 5550, 6400, 6450, 6550, 7400, 7450, 7550, 8400, 8450, 8550, 9400, 9450, 9550, 10400, 10450, 10550]:

        #Spawn_Cars.auto_appearance = "right"

    
    #elif PointsPlayer.puntos_player in [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500, 1500]:

        #Spawn_Cars.auto_appearance = "right"
        #Spawn_Cars.vel_auto += 3
        #print(Spawn_Cars.vel_auto)
        #level += 1
        #print(level)
        #PointsPlayer.puntos_player += 50

    #elif PointsPlayer.puntos_player > (650 or 1750 or 2750 or 3750 or 4750 or 5750 or 6750 or 7750 or 8750 or 9750 or 10750):

        #Spawn_Cars.auto_appearance = random.choice(["left", "right"])

    #return
            

while running:

    fps = clock.get_fps()
    text_fps = font.render(f'FPS: {int(fps)}', True, (2, 31, 11))
    text_level = font.render(f'Nivel: {level}', True, (2, 31, 11))
    teclas_pressed = pygame.key.get_pressed()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            running = False

        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_v:

                game_fps = 26


        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_v:

                game_fps = 100
            

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_p:

                show_texture = not show_texture

                if show_texture == False:

                    paused = False
                    #print("Working!")

    if teclas_pressed[pygame.K_RIGHT]:

        if player.x + player.width < Ancho:

            if Spawn_Cars.stop_game == False:
                
                player.x += 250
                #print(player.x)

            else:

                player.x = player.x
                #print("WORK!")


    if teclas_pressed[pygame.K_LEFT]:

        if player.x > 0:

            if Spawn_Cars.stop_game == False:
                
                player.x -= 250
                print(player.x)

            else:

                player.x = player.x
                #print("WORK!")

    if teclas_pressed[pygame.K_UP]:

        if Spawn_Cars.stop_game == False:

            movimiento = not movimiento

            if counter_time == 100:

                player.y -= 10

        else:

            player.y = player.y

    if teclas_pressed[pygame.K_DOWN]:

        if Spawn_Cars.stop_game == False:

            player.y += 10

        else:

            player.y = player.y 

    if teclas_pressed[pygame.K_q]:

        pygame.quit()


    if paused == True:
        continue
    #---------------------

    if movimiento:
 
        movimiento_arriba()


    #---Limites de la pantalla---
    if player.left > 790: 

        player.left = 790 #AJUSTA LOS LIMITES DE LA PANTALLA DESDE ADENTRO


    if player.right < 730:

        player.right = 730 #AJUSTA LOS LIMITES DE LA PANTALLA DESDE ADENTRO


    if player.bottom > Alto:

        player.bottom = 680


    if player.top < 0:

        player.top = 0
    #----------------------------


    #---Controlador de "PERDER"---
    #if Spawn_Cars.stop_game == True:
        
        #RELLENAR CON UN BOTON DE CONTINUAR PARA PODER JUGAR EL JUEGO DE NUEVO
        #DEJAR ESTATICO AL JUGADOR Y QUE NO SE PUEDAN USAR LOS CONTROLES
    #-----------------------------

    mainWindow.fill(color_fondo)
    mainWindow.blit(points_image, points_in_game)
    PointsPlayer.points_player(mainWindow)
    #level_enemyPOS()
    mainWindow.blit(border_image, border_in_game)
    mainWindow.blit(options_image, options_in_game)
    mainWindow.blit(player_image, player)
    paused_game()
    level_texture()
    #explosion()
    mainWindow.blit(text_fps,(20, 20))
    mainWindow.blit(text_level,(20,80))
    pygame.display.flip()
    clock.tick(game_fps)

pygame.quit()
sys.exit()