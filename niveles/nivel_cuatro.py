import pygame, sys
from pygame.locals import *
from configuraciones import *

class Nivel_cuatro():
    def __init__(self, pantalla: pygame.Surface):
        self._slave = pantalla
        W = pantalla.get_width()
        H = pantalla.get_height()

        self.next_lvl = "nivel_cuatro"

        self.img_fondo = pygame.image.load("recursos/Imagenes/Niveles/fondo/Fin.jpg")
        self.img_fondo = pygame.transform.scale(self.img_fondo, (W,H))

    def update(self, lista_eventos):
        self.acutualizar_pantalla()


    def acutualizar_pantalla(self):
        self._slave.blit(self.img_fondo,(0,0))
    
    def prox_lvl(self):
        if False:
            return ("Cambio", self.next_lvl)
        else:
            return ("no_cambio", self.next_lvl)