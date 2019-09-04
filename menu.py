import sys, pygame
import crgImg, idtBto, tcrTela

###-----------------------------------------------------------###
"""
crgImg  ===== Carrega as imagens do jogo
idtBto  ===== Identifica as posições dos botões
tcrTela ===== Troca as imagens da tela
"""
###-----------------------------------------------------------###

#--Variaveis de alteração--#
pygame.init()
size = width, height = 1000, 650
screen = pygame.display.set_mode(size)
executando = True
botao = 0
tema = 0

#--Telas do jogo--#
pygame.display.set_caption('Xadrez')
camada = 0
# crgImg.mdrTema(tema)
tela = crgImg.menu
# screen.blit(tela, (0,0))

#--Jogo em execução--#
while executando == True:
    x, y = pygame.mouse.get_pos()
    tela, botao = idtBto.btMouse(x, y, camada, tela)

    #--Controlar os eventos--#
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            executando = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if camada == 4:
                tela, camada, tema = tcrTela.prxTela(camada, botao, tema)

            elif camada == 0 and botao == 5:
                executando = tcrTela.prxTela(camada, botao, tema)

            else:
                tela, camada = tcrTela.prxTela(camada, botao, tema)                
                
    #pygame.time.delay(1000)
    print(f'{x} {y} {botao} {tema}')

    # redim = pygame.transform.smoothscale(tela, size)
    screen.blit(tela, (0,0))
    pygame.display.update()

pygame.quit()
sys.exit()
