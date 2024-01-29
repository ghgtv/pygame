import pygame
from entities.constants import WIDTH, HEIGHT


def move_player(keys, player):
    if keys[pygame.K_a]:
        player.directions[2] = True
    else:
        player.directions[2] = False
    if keys[pygame.K_d]:
        player.directions[3] = True
    else:
        player.directions[3] = False
    if keys[pygame.K_w]:
        player.directions[0] = True
    else:
        player.directions[0] = False
    if keys[pygame.K_s]:
        player.directions[1] = True
    else:
        player.directions[1] = False
    player.move()
