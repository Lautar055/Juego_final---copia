import pygame, sys
from pygame.locals import *
from configuraciones import *
from modo_progrmador import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_general, imagen_fondo, lados_piso, piso_img, prox_lvl):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.jugador.que_hace = "quieto"
        self.general = lista_general
        self.plataformas = self.general["plataformas"]
        self.enemigos = self.general["enemigos"]
        self.frutas = self.general["frutas"]
        self.fin = self.general["fin"]
        self.img_fondo = imagen_fondo
        self.lados_piso = lados_piso
        self.piso_img = piso_img

        self.next_lvl = prox_lvl

        self.lados_plataformas = [self.lados_piso]
        for plataforma in self.plataformas:
            self.lados_plataformas.append(plataforma.lados_platadormas)

    def update(self, lista_eventos):
        self.eventos = lista_eventos
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        self.leer_inputs()
        self.acutualizar_pantalla()
        self.dibujar_rectangulos()


    def acutualizar_pantalla(self):
        self._slave.blit(self.img_fondo,(0,0))
        # Plataformas
        self._slave.blit(self.piso_img, self.lados_piso["main"])

        for i in range(len(self.plataformas)):
            self._slave.blit(self.plataformas[i].platform, (self.plataformas[i].lados_platadormas["main"].x, self.plataformas[i].lados_platadormas["main"].y))

        self.jugador.update(self._slave, self.jugador.que_hace, self.lados_plataformas, self.enemigos)
        for enemigo in self.enemigos:
            enemigo.update(self._slave, self.jugador.lados)
        for fruta in self.frutas:
            fruta.update(self._slave, self.jugador.lados)


    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                self.jugador.que_hace = "salta_derecha"
            else:
                self.jugador.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                self.jugador.que_hace = "salta_izquierda"
            else:
                self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto"
    
    def dibujar_rectangulos(self):
        if get_mode():

            for clave in self.general:
                if clave == "fin":
                    pass
                else:
                    for entrada in self.general[clave]:
                        entrada.dibujar_rectangulo(self._slave)

            for lado in self.lados_piso:
                pygame.draw.rect(self._slave, (0, 255, 0), self.lados_piso[lado], 2)

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, (255, 128, 0), self.jugador.lados[lado], 2)
    
    def prox_lvl(self):
        if self.fin.deteccion_end(self.jugador.lados):
            return ("Cambio", self.next_lvl)
        else:
            return ("no_cambio", self.next_lvl)
