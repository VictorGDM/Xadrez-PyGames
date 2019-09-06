import sys, pygame
import crgImg, idtBto, tcrTela, crgSons

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
# relogio = pygame.time.Clock()
executando = True
tSom = 0
som = crgSons.mdrSom(tSom)
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
    crgSons.mdrSom(tSom)
    tela, botao, tSom = idtBto.btMouse(x, y, camada, tela)

    #--Controlar os eventos--#
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            executando = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            if camada == 4:
                tela, camada, tema = tcrTela.prxTela(camada, botao, tema, tSom)

            elif camada == 0 and botao == 5:
                executando = tcrTela.prxTela(camada, botao, tema, tSom)

            else:
                tela, camada = tcrTela.prxTela(camada, botao, tema, tSom)                
                
    # pygame.time.delay(1000)
    # relogio.tick(10)
    print(f'x:{x} y:{y} b:{botao} t:{tema} c:{camada} tS:{tSom}')

    # redim = pygame.transform.smoothscale(tela, size)
    screen.blit(tela, (0,0))
    pygame.display.update()

pygame.quit()
sys.exit()
