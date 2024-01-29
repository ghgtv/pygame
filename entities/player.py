import math

import pygame

from .constants import WIDTH, HEIGHT, CORRECTION_ANGLE


class Player:

    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 100, 100)
        self.speed = 10
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.original_image = self.image.copy()
        self.directions = [False, False, False, False]

    def move(self):
        if self.directions[0]:
            self.rect.y -= self.speed
        if self.directions[1]:
            self.rect.y += self.speed
        if self.directions[2]:
            self.rect.x -= self.speed
        if self.directions[3]:
            self.rect.x += self.speed

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - CORRECTION_ANGLE
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)
