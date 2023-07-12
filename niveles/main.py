import pygame
import sys
from pygame.locals import *
from configuraciones import *
from modo_progrmador import *
from nivel_uno import Nivel_uno
from nivel_dos import Nivel_dos
from nivel_tres import Nivel_tres
from nivel_cuatro import Nivel_cuatro

W,H = 1900, 900
TAMAÑO_PANTALLA = (W,H)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))
pygame.display.set_caption("Juego")

nivel_actual = Nivel_uno(PANTALLA)

niveles = {}
niveles["nivel_uno"] = Nivel_uno
niveles["nivel_dos"] = Nivel_dos
niveles["nivel_tres"] = Nivel_tres
niveles["nivel_cuatro"] = Nivel_cuatro

def get_nivel(nombre_nivel, pantalla):
    return niveles[nombre_nivel](pantalla)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)

    nivel_actual.update(eventos)
    partes_nivel = nivel_actual.prox_lvl()
    if partes_nivel[0] == "Cambio":
        nivel_actual = get_nivel(partes_nivel[1], PANTALLA)

    pygame.display.update()
