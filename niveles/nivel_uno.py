import pygame, sys
from nivel import * 
from pygame.locals import *
from configuraciones import *
from class_personaje import Personaje
from class_plataforma import Plataforma
from class_enemigo import Enemigo
from class_frutas import Fruta
from class_end import Fin

class Nivel_uno(Nivel):
    def __init__(self, pantalla: pygame.Surface):
        
        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo = pygame.image.load("recursos/Imagenes/Niveles/fondo/4.png")
        fondo = pygame.transform.scale(fondo, (W,H))

        #                                     Personaje
        posicion_inicial = (H/2 - 300, 745)
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

        slime_uno = Enemigo((65,75), animaciones_slime, (700, 275), 5, (610, 1120))
        slime_dos = Enemigo((65,75), animaciones_slime, (1500, 475), 5, (1210, 1520))

        lista_enemigos = [slime_uno, slime_dos]

        #                                     PISO
        piso = pygame.Rect(0,0,W,20)
        piso.top = mi_personaje.lados["main"].bottom
        piso_img = pygame.image.load("recursos/Imagenes/Niveles/platafomas/2/1.png")
        piso_img = pygame.transform.scale(piso_img, (W, 80))

        lados_piso = obtener_rectangulos(piso)

        #                                        Fin

        bandera_fin = Fin("recursos/Imagenes/miselaneos/Checkpoint/1.png", (50, 100), (1540, 150))

        #                                   Plataforma

        plataforma_uno = Plataforma("recursos/Imagenes/Niveles/platafomas/1/0.png", (100, 50), (700, 700))
        plataforma_dos = Plataforma("recursos/Imagenes/Niveles/platafomas/1/0.png", (100, 50), (1000, 700))
        plataforma_tres = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (400, 20), (1200, 550))
        plataforma_cuatro = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (400, 20), (200, 550))
        plataforma_cinco = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (600, 30), (600, 350))
        plataforma_seis = Plataforma("recursos/Imagenes/Niveles/platafomas/1/0.png", (100, 50), (1810, 250))
        plataforma_siete = Plataforma("recursos/Imagenes/Niveles/platafomas/1/0.png", (100, 50), (1500, 250))
        plataforma_ocho = Plataforma("recursos/Imagenes/Niveles/platafomas/2/0.png", (230, 50), (1590, 250))

        lista_plataformas_agregadas = [plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro, plataforma_cinco, plataforma_seis, plataforma_siete, plataforma_ocho, bandera_fin]

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

        
        super().__init__(pantalla, mi_personaje, lista_dibujar_rectangulos, fondo, lados_piso, piso_img, "nivel_dos")