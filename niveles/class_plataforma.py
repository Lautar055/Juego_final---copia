import pygame
from configuraciones import obtener_rectangulos

class Plataforma:
    def __init__(self, imagen, tamaño, posicion, color_rect=(255,255,255)):
        self.platform = pygame.image.load(imagen)
        self.platform = pygame.transform.scale(self.platform, tamaño)
        self.posicion = posicion

        self.color_dev = color_rect

        rectangulo = self.platform.get_rect()
        rectangulo.x = self.posicion[0]
        rectangulo.y = self.posicion[1]
        self.lados_platadormas = obtener_rectangulos(rectangulo)

    def dibujar_rectangulo(self, pantalla):
        for lado in self.lados_platadormas:
            pygame.draw.rect(pantalla, self.color_dev, self.lados_platadormas[lado], 2)
