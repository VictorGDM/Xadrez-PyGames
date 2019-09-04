import pygame, crgImg
pygame.init()

###-----------------------------------------------------------###
"""
Identifica a posição de um botão em sua determinada camada
"""
###-----------------------------------------------------------###

###-------------###
"""
Recebe:
X e Y do mouse, Camada, Tema

Retorna:
Tela, Botão
"""
###-------------###

def btMouse(x, y, c, tela):

    #--Botões da camada Menu--#  
    if c == 0:
        if x >= 730 and x <= 910 and y >= 190 and y <= 238:
            return crgImg.menu1, 1
    
        elif x >= 730 and x <= 910 and y >= 274 and y <= 318:
            return crgImg.menu2, 2

        elif x >= 730 and x <= 910 and y >= 352 and y <= 400:
            return crgImg.menu3, 3

        elif x >= 730 and x <= 910 and y >= 432 and y <= 482:
            return crgImg.menu4, 4
    
        elif x >= 730 and x <= 910 and y >= 512 and y <= 560:
            return crgImg.menu5, 5
        
        elif x >= 81 and x <= 161 and y >= 487 and y <= 568:
            return crgImg.menu, 6

        else:
            return crgImg.menu, 0

    #--Botões da camada Jogo--#
    if c == 1:
        if x >= 936 and x <= 994 and y >= 310 and y <= 342:
            return crgImg.jogo1, 1

        else:    
            return crgImg.jogo, 0

    #--Botões da camada Instruções--#
    if c == 2:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return crgImg.instruPeao, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return crgImg.instruCava, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return crgImg.instruBisp, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return crgImg.instruTorr, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return crgImg.instruDama, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return crgImg.instruRei, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return crgImg.instruVolt, 7

        else:
            return crgImg.instrucoes, 0

    #--Botões da camada Créditos--#
    if c == 3:
        if x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return crgImg.creditosVolt, 1
        else:
            return crgImg.creditos, 0

    #--Botões da camada Opções--#
    if c == 4:
        if x >= 129 and x <= 206 and y >= 236 and y <= 316:
            return crgImg.opcoes, 1
        
        elif x >= 129 and x <= 206 and y >= 335 and y <= 412:
            return crgImg.opcoes, 2

        elif x >= 129 and x <= 206 and y >= 433 and y <= 510:
            return crgImg.opcoes, 3

        elif x >= 129 and x <= 206 and y >= 530 and y <= 606:
            return crgImg.opcoes, 4
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return crgImg.opcoesVoltar, 5

        else:
            return crgImg.opcoes, 0

    #--eE--#
    if c == 100:
        return crgImg.eE, 0
