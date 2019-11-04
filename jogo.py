import pygame
import desenharTabuleiro, xadrez

pygame.init()
jogoExecutando = True
tabuleiro = xadrez.pegarTabuleiro()

desenharTabuleiro.pintarTelaTexto(tabuleiro)

while jogoExecutando == True:
    linhaOrigem : int
    linhaDestino : int
    colunaOrigem : int
    colunaDestino : int

    print(f"Informe a linha e a colunha de origem: ")
    linhaOrigem, colunaOrigem = int(input("Linha:")), int(input("Coluna:"))

    
    print(f"Informe a linha e a colunha de destino: ")
    linhaDestino, colunaDestino = int(input("Linha:")), int(input("Coluna:"))

    moverPeca = xadrez.moverPeca(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino)
    
    if moverPeca == 2:
        print(f"ERRO: Peça não pode ser movida deste jeito")

    elif moverPeca == 0:
        print(f"ERRO: Coordenadas inválidas")

    tabuleiro = xadrez.pegarTabuleiro()
    desenharTabuleiro.pintarTelaTexto(tabuleiro)
