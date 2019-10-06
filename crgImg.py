import pygame
pygame.init()

###-----------------------------------------------------------###
"""
Carrega as imagens utilizadas no jogo
"""
###-----------------------------------------------------------###

#--Menu--#
menu = pygame.image.load('telas/menu/menu0/menu.png')
menu1 = pygame.image.load('telas/menu/menu0/menuJogar.png')
menu2 = pygame.image.load('telas/menu/menu0/menuInstrucoes.png')
menu3 = pygame.image.load('telas/menu/menu0/menuCreditos.png')
menu4 = pygame.image.load('telas/menu/menu0/menuOpcoes.png')
menu5 = pygame.image.load('telas/menu/menu0/menuSair.png')

#--Instruções--#
instrucoes = pygame.image.load('telas/submenu/instrucoes/instrucoes.png')
instruVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesVoltar.png')
instruPeao = pygame.image.load('telas/submenu/instrucoes/instrucoesPeao.png')
instruCava = pygame.image.load('telas/submenu/instrucoes/instrucoesCavalo.png')
instruBisp = pygame.image.load('telas/submenu/instrucoes/instrucoesBispo.png')
instruTorr = pygame.image.load('telas/submenu/instrucoes/instrucoesTorre.png')
instruDama = pygame.image.load('telas/submenu/instrucoes/instrucoesDama.png')
instruRei = pygame.image.load('telas/submenu/instrucoes/instrucoesRei.png')
instruPeaoVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesPeaoVoltar.png')
instruCavaVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesCavaloVoltar.png')
instruBispVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesBispoVoltar.png')
instruTorrVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesTorreVoltar.png')
instruDamaVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesDamaVoltar.png')
instruReiVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesReiVoltar.png')

#--Créditos--#
creditos = pygame.image.load('telas/submenu/creditos/creditos.png')
creditosVolt = pygame.image.load('telas/submenu/creditos/creditosVoltar.png')

#--Opções--#
opcoes = pygame.image.load('telas/submenu/opcoes/opcao0/opcao.png')
opcoesVoltar = pygame.image.load('telas/submenu/opcoes/opcao0/opcaoVoltar.png')

#--Jogo--#
jogo = pygame.image.load('telas/jogo/jogo0/jogo.png')
jogo1 = pygame.image.load('telas/jogo/jogo0/jogoSair.png')


def mdrTema(t):
    global menu, menu1, menu2, menu3, menu4, menu5
    global opcoes, opcoesVoltar
    global jogo, jogo1

    menu = pygame.image.load(f'telas/menu/menu{t}/menu.png')
    menu1 = pygame.image.load(f'telas/menu/menu{t}/menuJogar.png')
    menu2 = pygame.image.load(f'telas/menu/menu{t}/menuInstrucoes.png')
    menu3 = pygame.image.load(f'telas/menu/menu{t}/menuCreditos.png')
    menu4 = pygame.image.load(f'telas/menu/menu{t}/menuOpcoes.png')
    menu5 = pygame.image.load(f'telas/menu/menu{t}/menuSair.png')

    opcoes = pygame.image.load(f'telas/submenu/opcoes/opcao{t}/opcao.png')
    opcoesVoltar = pygame.image.load(f'telas/submenu/opcoes/opcao{t}/opcaoVoltar.png')

    jogo = pygame.image.load(f'telas/jogo/jogo{t}/jogo.png')
    jogo1 = pygame.image.load(f'telas/jogo/jogo{t}/jogoSair.png')


eE = pygame.image.load('telas/submenu/sair/eE.png')
