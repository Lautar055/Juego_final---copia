import pygame, sys
from nivel import * 
from pygame.locals import *
from configuraciones import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_enemigo import Enemigo
from class_frutas import Fruta
from class_end import Fin

class Nivel_dos(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        
        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo = pygame.image.load("recursos/Imagenes/Niveles/fondo/4.png")
        fondo = pygame.transform.scale(fondo, (W,H))

        #                                     Personaje
        posicion_inicial = (50, 230)
        tamaño = (65,75)

        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = pj_idle
        diccionario_animaciones["salta_derecha"] = pj_salta
        diccionario_animaciones["salta_izquierda"] = pj_salta_izquierda
        diccionario_animaciones["camina_derecha"] = pj_camina
        diccionario_animaciones["camina_izquierda"] = pj_camina_izquierda

        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial)
        #                                    Enemigos


        #                    ##############    Slime    ##############
        animaciones_slime = {}
        animaciones_slime["izquierda"] = slime_idle
        animaciones_slime["muerto"] = slime_muerte
        animaciones_slime["derecha"] = slime_idle_derecha

        slime_uno = Enemigo((65,75), animaciones_slime, (180, 745), 5, (10, 1880))
        slime_dos = Enemigo((65,75), animaciones_slime, (1500, 230), 5, (30, 1500))
        slime_tres = Enemigo((65,75), animaciones_slime, (700, 530), 5, (350, 1850))


        #                    ##############    murcielago    ##############
        animaciones_bat = {}
        animaciones_bat["izquierda"] = bat_idle
        animaciones_bat["muerto"] = bat_muerte
        animaciones_bat["derecha"] = bat_idle_derecha

        bat_uno = Enemigo((35,35), animaciones_bat, (1850, 350), 5, (1600, 1850))
        bat_dos = Enemigo((35,35), animaciones_bat, (200, 650), 5, (20, 340))

        lista_enemigos = [slime_uno, slime_dos, slime_tres, bat_uno, bat_dos]

        #                                     PISO
        piso = pygame.Rect(0,0,W,20)
        piso.top = 820
        piso_img = pygame.image.load("recursos/Imagenes/Niveles/platafomas/2/1.png")
        piso_img = pygame.transform.scale(piso_img, (W, 80))

        lados_piso = obtener_rectangulos(piso)

        #                                        Fin

        bandera_fin = Fin("recursos/Imagenes/miselaneos/Checkpoint/1.png", (50, 100), (1800, 725))

        #                                     Plataforma

        plataforma_uno = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (1600, 30), (-1, 300))
        plataforma_dos = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (1600, 30), (300, 600))

        lista_plataformas_agregadas = [plataforma_uno, plataforma_dos, bandera_fin]

        #                                       Frutas
        animaciones_banana = {}
        animaciones_banana["idle"] = banana

        animaciones_manzana = {}
        animaciones_manzana["idle"] = manzana

        animaciones_naranja = {}
        animaciones_naranja["idle"] = naranja

        fruta_uno = Fruta((20,20), animaciones_banana, (150, 50))

        lista_frutas = [fruta_uno]


        #                         Lista de Diccionarios Necesaria

        lista_dibujar_rectangulos = {}
        lista_dibujar_rectangulos["plataformas"] = lista_plataformas_agregadas
        lista_dibujar_rectangulos["enemigos"] = lista_enemigos
        lista_dibujar_rectangulos["frutas"] = lista_frutas
        lista_dibujar_rectangulos["fin"] = bandera_fin

        
        super().__init__(pantalla, mi_personaje, lista_dibujar_rectangulos, fondo, lados_piso, piso_img, "nivel_tres")

# mi_personaje.lados["main"].bottom