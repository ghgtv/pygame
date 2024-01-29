import pygame
import math

from entities.constants import CORRECTION_ANGLE


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/bullets/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0])) - CORRECTION_ANGLE

        self.image = pygame.transform.rotate(self.image, angle)
        self.speed = 10
        self.shoot_sound = pygame.mixer.Sound('game_sounds/shooting/shoot.mp3')
        self.shoot_sound.set_volume(0.4)
        self.shoot_sound.play()

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed,
                    self.pos[1] + self.dir[1] * self.speed)

        self.rect = self.image.get_rect(center=self.pos)
        if self.rect.top <= 1:
            self.kill()


