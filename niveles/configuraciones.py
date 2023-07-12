import pygame
#######################################################################
def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def reescalar_imagenes(lista_imagenes, tamaño):
#    for lista in lista_imagenes:
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def obtener_rectangulos(principal)-> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -7, principal.top, 7, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 7, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario


#######################################################################

pj_idle = [pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/0.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/1.png"), 
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/2.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/3.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/4.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/5.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/6.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/7.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/8.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/9.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/idle/10.png"),]

pj_camina = [pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/0.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/1.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/2.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/3.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/4.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/5.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/6.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/7.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/8.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/9.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/10.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/11.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/12.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/13.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/14.png"),
            pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/correr/15.png"),]

pj_camina_izquierda = girar_imagenes(pj_camina, True, False)

pj_salta = [pygame.image.load("recursos/Imagenes/personaje/Virtual_Guy/salto/0.png"),]

pj_salta_izquierda = girar_imagenes(pj_salta, True, False)

slime_idle = [pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/0.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/1.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/2.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/3.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/4.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/5.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/6.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/7.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/8.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/idle/9.png"),]

slime_idle_derecha = girar_imagenes(slime_idle, True, False)

slime_muerte = [pygame.image.load("recursos/Imagenes/enemigos/Slime/muerte/4.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/muerte/3.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/muerte/2.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/muerte/1.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Slime/muerte/0.png"),]

banana = [pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/0.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/1.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/2.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/3.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/4.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/5.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/6.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/7.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/8.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/9.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/10.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/11.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/12.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/13.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/14.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/15.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Banana/16.png")]

manzana = [pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/0.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/1.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/2.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/3.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/4.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/5.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/6.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/7.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/8.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/9.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/10.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/11.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/12.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/13.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/14.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/15.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/16.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Manzana/17.png")]

naranja = [pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/0.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/1.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/2.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/3.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/4.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/5.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/6.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/7.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/8.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/9.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/10.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/11.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/12.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/13.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/14.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/15.png"),
        pygame.image.load("recursos/Imagenes/miselaneos/Fruits/Naranja/16.png")]

fin = [pygame.image.load("recursos/Imagenes/miselaneos/Checkpoint/1.png")]

bat_idle = [pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/0.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/1.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/2.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/3.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/4.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/5.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/Idle_move/6.png")]

bat_idle_derecha = girar_imagenes(bat_idle, True, False)

bat_muerte = [pygame.image.load("recursos/Imagenes/enemigos/Bat/muerte/0.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/muerte/1.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/muerte/2.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/muerte/3.png"),
            pygame.image.load("recursos/Imagenes/enemigos/Bat/muerte/4.png"),]