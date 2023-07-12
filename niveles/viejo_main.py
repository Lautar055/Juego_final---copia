import pygame
import sys
from pygame.locals import *
from configuraciones import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_enemigo import Enemigo
from modo_progrmador import *


########################POSIBLES COSAS PARA ANIMACIONES.py########################################

def acutualizar_pantalla(pantalla, un_personaje: Personaje, fondo, que_hace, plataformas, lados_plataformas, enemigos):
    pantalla.blit(fondo,(0,0))
    # Plataformas
    pantalla.blit(piso_img, plataformas[0]["main"])

    for i in range(len(plataformas)):
        if i >= 1:
            pantalla.blit(plataformas[i].platform, (plataformas[i].lados_platadormas["main"].x, plataformas[i].lados_platadormas["main"].y))

    un_personaje.update(pantalla, que_hace, lados_plataformas, enemigos)
    for enemigo in enemigos:
        enemigo.update(pantalla, un_personaje.lados)

##################################################################################################

W,H = 1900, 900
TAMAÑO_PANTALLA = (W,H)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))
pygame.display.set_caption("Juego")

fondo = pygame.image.load("recursos/Imagenes/Niveles/fondo/4.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

#Salto
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0

###############################################
posicion_inicial = (H/2 - 300, 745)
tamaño = (65,75)

diccionario_animaciones = {}
diccionario_animaciones["quieto"] = pj_idle
diccionario_animaciones["salta_derecha"] = pj_salta
diccionario_animaciones["salta_izquierda"] = pj_salta_izquierda
diccionario_animaciones["camina_derecha"] = pj_camina
diccionario_animaciones["camina_izquierda"] = pj_camina_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial)
###############################################
animaciones_slime = {}
animaciones_slime["izquierda"] = slime_idle
animaciones_slime["muerto"] = slime_muerte
animaciones_slime["derecha"] = slime_idle_derecha

slime_uno = Enemigo((65,75), animaciones_slime, (1900, 750), 5, (1000, 1900))

lista_enemigos = [slime_uno]
###############################################
#PISO
piso = pygame.Rect(0,0,W,20)
piso.top = mi_personaje.lados["main"].bottom
piso_img = pygame.image.load("recursos/Imagenes/Niveles/platafomas/2/1.png")
piso_img = pygame.transform.scale(piso_img, (W, 80))

lados_piso = obtener_rectangulos(piso)

###############################################
#Plataforma
plataforma_uno = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (400, 20), (700, 700))
plataforma_dos = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (400, 20), (1200, 575))
plataforma_tres = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (400, 20), (200, 575))

lista_plataformas_agregadas = [plataforma_uno, plataforma_dos, plataforma_tres]
###############################################
lista_dibujar_rectangulos = {}
lista_dibujar_rectangulos["plataformas"] = lista_plataformas_agregadas
lista_dibujar_rectangulos["enemigos"] = lista_enemigos
###############################################
lista_plataformas = [lados_piso, plataforma_uno, plataforma_dos, plataforma_tres]
lados_plataformas = [lados_piso, plataforma_uno.lados_platadormas, plataforma_dos.lados_platadormas, plataforma_tres.lados_platadormas]

que_hace = "quieto"

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    acutualizar_pantalla(PANTALLA, mi_personaje, fondo, que_hace, lista_plataformas, lados_plataformas, lista_enemigos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if keys[pygame.K_UP]:
            que_hace = "salta_derecha"
        else:
            que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        if keys[pygame.K_UP]:
            que_hace = "salta_izquierda"
        else:
            que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        que_hace = "salta"
    else:
        que_hace = "quieto"

    if get_mode():

        for clave in lista_dibujar_rectangulos:
            for entrada in lista_dibujar_rectangulos[clave]:
                entrada.dibujar_rectangulo(PANTALLA)

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, (0, 255, 0), lados_piso[lado], 2)

        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, (255, 128, 0), mi_personaje.lados[lado], 2)

    pygame.display.update()

#pygame.draw.rect(PANTALLA, (0, 255, 0), lados_plataforma[lado], 2)