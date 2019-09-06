import sys, pygame, crgImg, idtBto
pygame.init()

###-----------------------------------------------------------###
"""
Troca a tela do jogo de acordo com o clique do mouse.
Troca a camada de tela que o jogo se encontra.
"""
###-----------------------------------------------------------###

###-------------###
"""
Recebe:
Camada, Botão, Tema

Retorna:
Tela, Camada, Tema
"""
###-------------###

def prxTela(c, b, t):

    #--Telas do menu--#
    if c == 0:
        if b == 1:
            return crgImg.jogo, 1
            
        elif b == 2:
            return crgImg.instrucoes, 2

        elif b == 3:
            return crgImg.creditos, 3

        elif b == 4:
            return crgImg.opcoes, 4

        elif b == 5:
            return False

        elif b == 6:
            return crgImg.eE, 100

        else:
            return crgImg.menu, 0
    
    #--Telas do jogo--#
    if c == 1:
        if b == 1:
            return crgImg.menu, 0

        else:
            return crgImg.jogo, 1

    #--Telas das Instruções--#
    if c == 2:
        if b == 1:
            return crgImg.instruPeao, 20

        if b == 2:
            return crgImg.instruCava, 21

        if b == 3:
            return crgImg.instruBisp, 22

        if b == 4:
            return crgImg.instruTorr, 23

        if b == 5:
            return crgImg.instruDama, 24

        if b == 6:
            return crgImg.instruRei, 25

        if b == 7:
            return crgImg.menu, 0

        else:
            return crgImg.instrucoes, 2

    #--Telas dos Créditos--#
    if c == 3:
        if b == 1:
            return crgImg.menu, 0
        
        else:
            return crgImg.creditos, 3
        
    #--Telas das opções--#
    if c == 4:
        if b == 1:
            return crgImg.opcoes, 4, 0
        
        if b == 2:
            return crgImg.opcoes, 4, 1

        if b == 3:
            return crgImg.opcoes, 4, 2

        if b == 4:
            return crgImg.opcoes, 4, 3

        if b == 5:
            return crgImg.menu, 0, t

        else:
            return crgImg.opcoes, 4, t

    """------------"""
    #--Instruções.2--#
    """------------"""
    if c == 20:
        if b == 1:
            return crgImg.instrucoes, 2
        
        if b == 2:
            return crgImg.instruCava, 21
        
        if b == 3:
            return crgImg.instruBisp, 22
        
        if b == 4:
            return crgImg.instruTorr, 23
        
        if b == 5:
            return crgImg.instruDama, 24

        if b == 6:
            return crgImg.instruRei, 25

        if b == 7:
            return crgImg.menu, 0
        
        else:
            return crgImg.instruPeao, 20

    if c == 21:
        if b == 1:
            return crgImg.instruPeao, 20
        
        if b == 2:
            return crgImg.instrucoes, 2
        
        if b == 3:
            return crgImg.instruBisp, 22
        
        if b == 4:
            return crgImg.instruTorr, 23
        
        if b == 5:
            return crgImg.instruDama, 24

        if b == 6:
            return crgImg.instruRei, 25

        if b == 7:
            return crgImg.menu, 0
        
        else:
            return crgImg.instruCava, 21

    if c == 22:
        if b == 1:
            return crgImg.instruPeao, 20
        
        if b == 2:
            return crgImg.instruCava, 21
        
        if b == 3:
            return crgImg.instrucoes, 2
        
        if b == 4:
            return crgImg.instruTorr, 23
        
        if b == 5:
            return crgImg.instruDama, 24

        if b == 6:
            return crgImg.instruRei, 25

        if b == 7:
            return crgImg.menu, 0
        
        else:
            return crgImg.instruBisp, 22

    if c == 23:
        if b == 1:
            return crgImg.instruPeao, 20
        
        if b == 2:
            return crgImg.instruCava, 21
        
        if b == 3:
            return crgImg.instruBisp, 22
        
        if b == 4:
            return crgImg.instrucoes, 2
        
        if b == 5:
            return crgImg.instruDama, 24

        if b == 6:
            return crgImg.instruRei, 25

        if b == 7:
            return crgImg.menu, 0
        
        else:
            return crgImg.instruTorr, 23

    if c == 24:
        if b == 1:
            return crgImg.instruPeao, 20
        
        if b == 2:
            return crgImg.instruCava, 21
        
        if b == 3:
            return crgImg.instruBisp, 22
        
        if b == 4:
            return crgImg.instruTorr, 23
        
        if b == 5:
            return crgImg.instrucoes, 2

        if b == 6:
            return crgImg.instruRei, 25

        if b == 7:
            return crgImg.menu, 0
        
        else:
            return crgImg.instruDama, 24

    if c == 25:
        if b == 1:
            return crgImg.instruPeao, 20
        
        if b == 2:
            return crgImg.instruCava, 21
        
        if b == 3:
            return crgImg.instruBisp, 22
        
        if b == 4:
            return crgImg.instruTorr, 23
        
        if b == 5:
            return crgImg.instruDama, 24

        if b == 6:
            return crgImg.instrucoes, 2

        if b == 7:
            return crgImg.menu, 0
        
        else:
            return crgImg.instruRei, 25

    #--eE--#
    if c == 100:
        if b == 0:
            return crgImg.menu, 0
