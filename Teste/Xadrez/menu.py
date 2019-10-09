import sys, pygame
import crgImg, idtBto, tcrTela

###-----------------------------------------------------------###
"""
crgImg  ===== Carrega as imagens do jogo
idtBto  ===== Identifica as posições dos botões
tcrTela ===== Troca as imagens da tela
"""
###-----------------------------------------------------------###
def updateScreen(tela):
    screen.blit(tela, (0, 0))
    pygame.display.update()

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
crgImg.mdrTema(tema)
tela = crgImg.menu
updateScreen(tela)

#--Jogo em execução--#
while executando == True:
    x, y = pygame.mouse.get_pos()

    #--Controlar os eventos--#
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            executando = False

        if event.type == pygame.MOUSEBUTTONUP:
            if camada == 4:                
                if botao == 0 or botao == 5:
                    mudou, tela, camada = tcrTela.prxTela(camada, botao, tema)
                
                else:
                    mudou, tela, camada, tema = tcrTela.prxTela(camada, botao, tema)
                    crgImg.mdrTema(tema)
                    updateScreen(tela)

            elif camada == 0 and botao == 5:
                executando = tcrTela.prxTela(camada, botao, tema)

            else:
                mudou, tela_r, camada_r = tcrTela.prxTela(camada, botao, tema)    
                if(mudou):
                    tela = tela_r
                    camada = camada_r
                    updateScreen(tela)

    print(f'x:{x} y:{y} b:{botao} t:{tema} c:{camada}')

    mudou, tela_r, botao_r = idtBto.btMouse(x, y, camada, tela)
    
    if(mudou):
        tela = tela_r
        botao = botao_r
        updateScreen(tela)

pygame.quit()
sys.exit()
