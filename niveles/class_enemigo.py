import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulos


class Enemigo:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, coordenadas, color_rect=(255,0,0)):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        self.estado_vida = "vivo"
        
        self.contador_pasos = 0
        self.que_hace = "izquierda" # izq/dere - muerto
        self.animaciones = animaciones
        self.reescalar_animaciones()

        rectangulo = self.animaciones["derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        self.velocidad = velocidad

        self.min_x = coordenadas[0]
        self.max_x = coordenadas[1]

        self.color_dev = color_rect

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, q_animacion:str, valor_vida):
        animacion = self.animaciones[q_animacion]
        largo = len(animacion)
        
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        if valor_vida == "vivo":
            pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
            self.contador_pasos += 1
        elif valor_vida == "muerto":
            if self.contador_pasos == 0:
                self.mover(self.velocidad)
            else:
                pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
                self.contador_pasos += 1

    def mover(self, velocidad):
        if self.estado_vida == "vivo":
            for lado in self.lados:
                self.lados[lado].x += velocidad
        elif self.estado_vida == "muerto":
            if self.contador_pasos == 0:
                for lado in self.lados:
                    self.lados[lado].x = 100000000

    def update(self, pantalla, lados_personaje):
        match self.que_hace:
            case "derecha":
                self.animar(pantalla, "derecha", "vivo")
                self.mover(self.velocidad)
            case "izquierda":
                self.animar(pantalla, "izquierda", "vivo")
                self.mover(self.velocidad*-1)
            case "muerto":
                self.animar(pantalla, "muerto", "muerto")
                #self.mover(self.velocidad)
        self.detectar_x()
        self.detectar_muerte(lados_personaje)

    def detectar_x(self):
        if self.lados["main"].x == self.max_x:
            self.que_hace = "izquierda"
        if self.lados["main"].x == self.min_x:
            self.que_hace = "derecha"
    
    def detectar_muerte(self, lados_personaje):
        if self.lados["top"].colliderect(lados_personaje["bottom"]):
            self.que_hace = "muerto"
            self.estado_vida = "muerto"
    
    def dibujar_rectangulo(self, pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, self.color_dev, self.lados[lado], 2)