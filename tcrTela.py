import pygame
import crgImg, idtBto
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
Se a tela mudou, Tela, Camada
Se a tela mudou, Tela, Camada, Tema <<< No caso de configurações.
"""
###-------------###

def prxTela(c, b, t):

    #--Telas do menu--#
    if c == 0:
        if b == 1:
            return True, crgImg.jogo, 1
            
        if b == 2:
            return True, crgImg.instrucoes, 2

        if b == 3:
            return True, crgImg.creditos, 3

        if b == 4:
            return True, crgImg.opcoes, 4

        if b == 5:
            return False

        if b == 6:
            return True, crgImg.eE, 100

        else:
            return False, crgImg.menu, 0
    
    #--Telas do jogo--#
    if c == 1:
        if b == 1:
            return True, crgImg.menu, 0

        else:
            return False, crgImg.jogo, 1

    #--Telas das Instruções--#
    if c == 2:
        if b == 1:
            return True, crgImg.instruPeao, 20

        if b == 2:
            return True, crgImg.instruCava, 21

        if b == 3:
            return True, crgImg.instruBisp, 22

        if b == 4:
            return True, crgImg.instruTorr, 23

        if b == 5:
            return True, crgImg.instruDama, 24

        if b == 6:
            return True, crgImg.instruRei, 25

        if b == 7:
            return True, crgImg.menu, 0

        else:
            return False, crgImg.instrucoes, 2

    #--Telas dos Créditos--#
    if c == 3:
        if b == 1:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.creditos, 3
        
    #--Telas das opções--#
    if c == 4:
        if b == 1:
            return True, crgImg.opcoes, 4, 0
        
        if b == 2:
            return True, crgImg.opcoes, 4, 1

        if b == 3:
            return True, crgImg.opcoes, 4, 2

        if b == 4:
            return True, crgImg.opcoes, 4, 3

        if b == 5:
            return True, crgImg.menu, 0

        else:
            return False, crgImg.opcoes, 4

    """------------"""
    #--Instruções.2--#
    """------------"""
    if c == 20:
        if b == 1:
            return True, crgImg.instrucoes, 2
        
        if b == 2:
            return True, crgImg.instruCava, 21
        
        if b == 3:
            return True, crgImg.instruBisp, 22
        
        if b == 4:
            return True, crgImg.instruTorr, 23
        
        if b == 5:
            return True, crgImg.instruDama, 24

        if b == 6:
            return True, crgImg.instruRei, 25

        if b == 7:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.instruPeao, 20

    if c == 21:
        if b == 1:
            return True, crgImg.instruPeao, 20
        
        if b == 2:
            return True, crgImg.instrucoes, 2
        
        if b == 3:
            return True, crgImg.instruBisp, 22
        
        if b == 4:
            return True, crgImg.instruTorr, 23
        
        if b == 5:
            return True, crgImg.instruDama, 24

        if b == 6:
            return True, crgImg.instruRei, 25

        if b == 7:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.instruCava, 21

    if c == 22:
        if b == 1:
            return True, crgImg.instruPeao, 20
        
        if b == 2:
            return True, crgImg.instruCava, 21
        
        if b == 3:
            return True, crgImg.instrucoes, 2
        
        if b == 4:
            return True, crgImg.instruTorr, 23
        
        if b == 5:
            return True, crgImg.instruDama, 24

        if b == 6:
            return True, crgImg.instruRei, 25

        if b == 7:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.instruBisp, 22

    if c == 23:
        if b == 1:
            return True, crgImg.instruPeao, 20
        
        if b == 2:
            return True, crgImg.instruCava, 21
        
        if b == 3:
            return True, crgImg.instruBisp, 22
        
        if b == 4:
            return True, crgImg.instrucoes, 2
        
        if b == 5:
            return True, crgImg.instruDama, 24

        if b == 6:
            return True, crgImg.instruRei, 25

        if b == 7:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.instruTorr, 23

    if c == 24:
        if b == 1:
            return True, crgImg.instruPeao, 20
        
        if b == 2:
            return True, crgImg.instruCava, 21
        
        if b == 3:
            return True, crgImg.instruBisp, 22
        
        if b == 4:
            return True, crgImg.instruTorr, 23
        
        if b == 5:
            return True, crgImg.instrucoes, 2

        if b == 6:
            return True, crgImg.instruRei, 25

        if b == 7:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.instruDama, 24

    if c == 25:
        if b == 1:
            return True, crgImg.instruPeao, 20
        
        if b == 2:
            return True, crgImg.instruCava, 21
        
        if b == 3:
            return True, crgImg.instruBisp, 22
        
        if b == 4:
            return True, crgImg.instruTorr, 23
        
        if b == 5:
            return True, crgImg.instruDama, 24

        if b == 6:
            return True, crgImg.instrucoes, 2

        if b == 7:
            return True, crgImg.menu, 0
        
        else:
            return False, crgImg.instruRei, 25

    #--eE--#
    if c == 100:
        if b == 0:
            return True, crgImg.menu, 0
