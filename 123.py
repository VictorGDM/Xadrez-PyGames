import time

import pygame

# definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))
# carregando fonte
font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('Olá mundo')

# preenchendo o fundo com preto
screen.fill(BLACK)

# desenhando na superfície 
pygame.draw.rect(screen, BLUE, [100, 100, 40, 40])

# atualizando a tela
pygame.display.flip()

time.sleep(5)

# preenchendo o fundo com preto
screen.fill(RED)

# definindo o texto
text = font.render('pygame', True, WHITE)
# copiando o texto para a superfície
screen.blit(text, [250, 200])

# atualizando a tela
pygame.display.flip()

time.sleep(5)