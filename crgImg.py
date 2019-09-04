import pygame
pygame.init()

###-----------------------------------------------------------###
"""
Carrega as imagens utilizadas no jogo
"""
###-----------------------------------------------------------###
tema = 2

#--Menu_Padrão--#
menu = pygame.image.load(f'telas/menu/menu{tema}/menu.png')
menu1 = pygame.image.load(f'telas/menu/menu{tema}/menuJogar.png')
menu2 = pygame.image.load(f'telas/menu/menu{tema}/menuInstrucoes.png')
menu3 = pygame.image.load(f'telas/menu/menu{tema}/menuCreditos.png')
menu4 = pygame.image.load(f'telas/menu/menu{tema}/menuOpcoes.png')
menu5 = pygame.image.load(f'telas/menu/menu{tema}/menuSair.png')

# #--Tema_Cinza--#
# menu = pygame.image.load('telas/menu/menu1/menu.png')
# menu1 = pygame.image.load('telas/menu/menu1/menuJogar.png')
# menu2 = pygame.image.load('telas/menu/menu1/menuInstrucoes.png')
# menu3 = pygame.image.load('telas/menu/menu1/menuCreditos.png')
# menu4 = pygame.image.load('telas/menu/menu1/menuOpcoes.png')
# menu5 = pygame.image.load('telas/menu/menu1/menuSair.png')

# #--Tena_Marrom--#
# menu = pygame.image.load('telas/menu/menu2/menu.png')
# menu1 = pygame.image.load('telas/menu/menu2/menuJogar.png')
# menu2 = pygame.image.load('telas/menu/menu2/menuInstrucoes.png')
# menu3 = pygame.image.load('telas/menu/menu2/menuCreditos.png')
# menu4 = pygame.image.load('telas/menu/menu2/menuOpcoes.png')
# menu5 = pygame.image.load('telas/menu/menu2/menuSair.png')

# #--Tema_Verde--#
# menu = pygame.image.load('telas/menu/menu3/menu.png')
# menu1 = pygame.image.load('telas/menu/menu3/menuJogar.png')
# menu2 = pygame.image.load('telas/menu/menu3/menuInstrucoes.png')
# menu3 = pygame.image.load('telas/menu/menu3/menuCreditos.png')
# menu4 = pygame.image.load('telas/menu/menu3/menuOpcoes.png')
# menu5 = pygame.image.load('telas/menu/menu3/menuSair.png')

#--Instruções--#
instrucoes = pygame.image.load('telas/submenu/instrucoes/instrucoes.png')
instruVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesVoltar.png')
instruPeao = pygame.image.load('telas/submenu/instrucoes/instrucoesPeao.png')
instruCava = pygame.image.load('telas/submenu/instrucoes/instrucoesCavalo.png')
instruBisp = pygame.image.load('telas/submenu/instrucoes/instrucoesBispo.png')
instruTorr = pygame.image.load('telas/submenu/instrucoes/instrucoesTorre.png')
instruDama = pygame.image.load('telas/submenu/instrucoes/instrucoesDama.png')
instruRei = pygame.image.load('telas/submenu/instrucoes/instrucoesRei.png')
# instruPeaoVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesPeaoVoltar.png')
# instruCavaVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesCavaloVoltar.png')
# instruBispVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesBispoVoltar.png')
# instruTorrVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesTorreVoltar.png')
# instruDamaVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesDamaVoltar.png')
# instruReiVolt = pygame.image.load('telas/submenu/instrucoes/instrucoesReiVoltar.png')

#--Créditos--#
creditos = pygame.image.load('telas/submenu/creditos/creditos.png')
creditosVolt = pygame.image.load('telas/submenu/creditos/creditosVoltar.png')

#--Opções--#
opcoes = pygame.image.load(f'telas/submenu/opcoes/opcao{tema}/opcao.png')
opcoesVoltar = pygame.image.load(f'telas/submenu/opcoes/opcao{tema}/opcaoVoltar.png')

#--Jogo--#
jogo = pygame.image.load('telas/jogo/jogo.png')
jogo1 = pygame.image.load('telas/jogo/jogoSair.png')


eE = pygame.image.load('telas/submenu/sair/eE.png')
"""
# def mdrTema(t):
#         #--Menu_Padrão--#
#         menu = pygame.image.load(f'telas/menu/menu{t}/menu.png')
#         menu1 = pygame.image.load(f'telas/menu/menu{t}/menuJogar.png')
#         menu2 = pygame.image.load(f'telas/menu/menu{t}/menuInstrucoes.png')
#         menu3 = pygame.image.load(f'telas/menu/menu{t}/menuCreditos.png')
#         menu4 = pygame.image.load(f'telas/menu/menu{t}/menuOpcoes.png')
#         menu5 = pygame.image.load(f'telas/menu/menu{t}/menuSair.png')
"""
