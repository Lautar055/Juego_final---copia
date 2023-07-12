import pygame, sys
from configuraciones import reescalar_imagenes, obtener_rectangulos


class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial):
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #X e Y iniciales
        self.rectangulo_x = posicion_inicial[0]
        self.rectangulo_y = posicion_inicial[1]
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -20
        self.limite_velocidad_caida = 20
        self.esta_saltando = False
        
        self.velocidad = 10
        self.desplazamiento_y = 0

        self.vidas = 3

    #quiete - salta_derecha - salta_izquierda - camina_derecha - camina_izquierda
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

    def mover(self, velocidad, tp=False):
        if not tp:
            for lado in self.lados:
                self.lados[lado].x += velocidad
        elif tp:
            for lado in self.lados:
                self.lados[lado].x = self.rectangulo_x
                self.lados[lado].y = self.rectangulo_y - 20

    def update(self, pantalla, que_hace, plataformas, enemigos):
        self.que_hace = que_hace

        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad*-1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "salta_derecha":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                self.mover(self.velocidad)
            case "salta_izquierda":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                self.mover(self.velocidad*-1)
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")

        if que_hace == "salta_izquierda" or self.esta_saltando == True and que_hace == "izquierda":
            self.aplicar_gravedad(pantalla, "salta_izquierda", plataformas)
        else:
            self.aplicar_gravedad(pantalla, "salta_derecha", plataformas)
        
        self.detectar_clolision_enemigo(enemigos)

    def aplicar_gravedad(self, pantalla, animacion, plataformas):
        #SALTO
        if self.esta_saltando:
            self.animar(pantalla, animacion)

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        #CAIDA
        for piso in plataformas:
            if self.lados["bottom"].colliderect(piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = piso["top"].top + 5
                break
            else:
                self.esta_saltando = True

        #AJUSTAR RECTANGULOS
        self.lados["bottom"].bottom = self.lados["main"].bottom
        self.lados["top"].top = self.lados["main"].top
        self.lados["right"].top = self.lados["main"].top
        self.lados["left"].top = self.lados["main"].top
        self.lados["right"].right = self.lados["main"].right
        self.lados["left"].left = self.lados["main"].left
    
    def detectar_clolision_enemigo(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.lados["right"].colliderect(enemigo.lados["right"]):
                pygame.quit()
                sys.exit(0)
            elif self.lados["right"].colliderect(enemigo.lados["left"]):
                pygame.quit()
                sys.exit(0)
            
            elif self.lados["left"].colliderect(enemigo.lados["right"]):
                pygame.quit()
                sys.exit(0)
            elif self.lados["left"].colliderect(enemigo.lados["left"]):
                pygame.quit()
                sys.exit(0)
            
            elif self.lados["top"].colliderect(enemigo.lados["bottom"]):
                pygame.quit()
                sys.exit(0)
            elif self.lados["bottom"].colliderect(enemigo.lados["top"]):
                self.desplazamiento_y = -15
