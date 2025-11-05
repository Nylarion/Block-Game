import pygame
import Spawn_Cars
from Spawn_Cars import autos, Y_limit

puntos_player = 0

def points_player(pantalla):

    global puntos_player

    for i in range(len(autos)):

        No_use, give_points , vel = autos[i]

        give_points += vel

        if give_points > Y_limit:

            puntos_player += 50
            print("Give 50 points to player!")


    if puntos_player > 999999:

        puntos_player = 0


    font = pygame.font.Font('Assets/Font/slkscr.ttf', 30)
    inGame_points = font.render(f'Puntuacion: {puntos_player}', True, (2, 31, 11))
    pantalla.blit(inGame_points,(20, 50))
    return

    
        
    
