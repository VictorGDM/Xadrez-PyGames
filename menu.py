import sys, pygame
import crgImg, idtBto, tcrTela
import desenharTabuleiro, xadrez

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


def sonMenu():
    pygame.mixer.music.load('sons/menu/menu.mp3')
    pygame.mixer.music.play()


def sonMenuCancel():
    pygame.mixer.music.stop()

#--Variaveis de alteração--#
pygame.init()
size = width, height = 1000, 650
screen = pygame.display.set_mode(size)
executando = True
menuJogo = 1
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
    if (menuJogo == 1):
        sonMenu()

    while menuJogo == 1:
        x, y = pygame.mouse.get_pos()

        #--Controlar os eventos--#
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                executando = False
                menuJogo = 0

            if event.type == pygame.MOUSEBUTTONUP:
                if camada == 4:                
                    if botao == 0 or botao == 5:
                        mudou, tela, camada = tcrTela.prxTela(camada, botao, tema)
                    
                    else:
                        mudou, tela, camada, tema = tcrTela.prxTela(camada, botao, tema)
                        crgImg.mdrTema(tema)
                        updateScreen(tela)

                elif camada == 0 and botao == 5:
                    menuJogo = 0
                    executando = tcrTela.prxTela(camada, botao, tema)

                elif camada == 1:
                    sonMenuCancel()
                    menuJogo = 2

                else:
                    mudou, tela_r, camada_r = tcrTela.prxTela(camada, botao, tema)    
                    if(mudou):
                        tela = tela_r
                        camada = camada_r
                        updateScreen(tela)

        # print(f'x:{x} y:{y} b:{botao} t:{tema} c:{camada}')

        mudou, tela_r, botao_r = idtBto.btMouse(x, y, camada, tela)
        
        if(mudou):
            tela = tela_r
            botao = botao_r
            updateScreen(tela)

    tabuleiro = xadrez.pegarTabuleiro()

    while menuJogo == 2:
        desenharTabuleiro.pintarTelaGrafica(tabuleiro, tema, tela)
        meuJogo = desenharTabuleiro.capturarEvento()

        tabuleiro = xadrez.pegarTabuleiro()

pygame.quit()
sys.exit()
