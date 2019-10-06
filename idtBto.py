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
X e Y do mouse, Camada, Tela

Retorna:
Mudou, Tela, Botão
"""
###-------------###

def btMouse(x, y, c, tela):

    #--Botões da camada Menu--#  
    if c == 0:
        if x >= 730 and x <= 910 and y >= 190 and y <= 238:
            return True, crgImg.menu1, 1
    
        elif x >= 730 and x <= 910 and y >= 274 and y <= 318:
            return True, crgImg.menu2, 2

        elif x >= 730 and x <= 910 and y >= 352 and y <= 400:
            return True, crgImg.menu3, 3

        elif x >= 730 and x <= 910 and y >= 432 and y <= 482:
            return True, crgImg.menu4, 4
    
        elif x >= 730 and x <= 910 and y >= 512 and y <= 560:
            return True, crgImg.menu5, 5
        
        elif x >= 81 and x <= 161 and y >= 487 and y <= 568:
            return True, crgImg.menu, 6

        else:
            return True, crgImg.menu, 0

    #--Botões da camada Jogo--#
    if c == 1:
        if x >= 936 and x <= 994 and y >= 310 and y <= 342:
            return True, crgImg.jogo1, 1

        else:    
            return True, crgImg.jogo, 0

    #--Botões da camada Instruções--#
    if c == 2:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instrucoes, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instrucoes, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instrucoes, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instrucoes, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instrucoes, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instrucoes, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruVolt, 7

        else:
            return True, crgImg.instrucoes, 0

    #--Botões da camada Créditos--#
    if c == 3:
        if x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.creditosVolt, 1
        else:
            return True, crgImg.creditos, 0

    #--Botões da camada Opções--#
    if c == 4:
        if x >= 129 and x <= 206 and y >= 236 and y <= 316:
            return True, crgImg.opcoes, 1
        
        elif x >= 129 and x <= 206 and y >= 335 and y <= 412:
            return True, crgImg.opcoes, 2

        elif x >= 129 and x <= 206 and y >= 433 and y <= 510:
            return True, crgImg.opcoes, 3

        elif x >= 129 and x <= 206 and y >= 530 and y <= 606:
            return True, crgImg.opcoes, 4
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.opcoesVoltar, 5

        else:
            return True, crgImg.opcoes, 0

    """------------"""
    #--Instruções.2--#
    """------------"""
    if c == 20:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instruPeao, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instruPeao, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instruPeao, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instruPeao, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instruPeao, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instruPeao, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruPeaoVolt, 7

        else:
            return True, crgImg.instruPeao, 0

    if c == 21:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instruCava, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instruCava, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instruCava, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instruCava, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instruCava, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instruCava, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruCavaVolt, 7

        else:
            return True, crgImg.instruCava, 0

    if c == 22:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instruBisp, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instruBisp, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instruBisp, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instruBisp, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instruBisp, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instruBisp, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruBispVolt, 7

        else:
            return True, crgImg.instruBisp, 0

    if c == 23:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instruTorr, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instruTorr, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instruTorr, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instruTorr, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instruTorr, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instruTorr, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruTorrVolt, 7

        else:
            return True, crgImg.instruTorr, 0

    if c == 24:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instruDama, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instruDama, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instruDama, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instruDama, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instruDama, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instruDama, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruDamaVolt, 7

        else:
            return True, crgImg.instruDama, 0

    if c == 25:
        if x >= 38 and x <= 126 and y >= 202 and y <= 294:
            return True, crgImg.instruRei, 1
        
        elif x >= 206 and x <= 295 and y >= 202 and y <= 294:
            return True, crgImg.instruRei, 2

        elif x >= 374 and x <= 464 and y >= 202 and y <= 294:
            return True, crgImg.instruRei, 3

        elif x >= 540 and x <= 630 and y >= 202 and y <= 294:
            return True, crgImg.instruRei, 4

        elif x >= 708 and x <= 798 and y >= 202 and y <= 294:
            return True, crgImg.instruRei, 5

        elif x >= 878 and x <= 966 and y >= 202 and y <= 294:
            return True, crgImg.instruRei, 6
        
        elif x >= 861 and x <= 986 and y >= 591 and y <= 621:
            return True, crgImg.instruReiVolt, 7

        else:
            return True, crgImg.instruRei, 0

    #--eE--#
    if c == 100:
        return True, crgImg.eE, 0
