import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulos

class Fruta:
    def __init__(self, tamaño, animaciones, posicion_inicial, color_rect=(255,255,255)):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.contador_pasos = 0
        self.animaciones = animaciones
        self.reescalar_animaciones()

        rectangulo = self.animaciones["idle"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)

        self.color_dev = color_rect

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, q_animacion:str):
        animacion = self.animaciones[q_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
            pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
            self.contador_pasos += 1

    def mover(self):
        if self.contador_pasos == 0:
            for lado in self.lados:
                self.lados[lado].x = 100000000

    def update(self, pantalla, lados_personaje):
        self.animar(pantalla, "idle")
        if self.lados["main"].colliderect(lados_personaje["main"]):
            self.mover()

    def dibujar_rectangulo(self, pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, self.color_dev, self.lados[lado], 2)