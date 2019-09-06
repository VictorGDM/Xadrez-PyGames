import pygame
pygame.init()

###-----------------------------------------------------------###
"""
Carrega os sons utilizados pelo jogo.
"""
###-----------------------------------------------------------###

def mdrSom(tipo):

    if tipo == 0:
        som = 'sons/click/releaseClick.mp3'
        return pygame.mixer.music.load(som)
    
    if tipo == 1:
        som = 'sons/pecas/torre/ajudaTorre.mp3'
        return pygame.mixer.music.load(som)


