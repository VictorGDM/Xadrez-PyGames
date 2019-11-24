import pygame
import desenharTabuleiro, xadrez

pygame.init()
jogoExecutando = True
tabuleiro = xadrez.pegarTabuleiro()

# desenharTabuleiro.pintarTelaTexto(tabuleiro)

while jogoExecutando == True:
    desenharTabuleiro.pintarTelaGrafica(tabuleiro)
    desenharTabuleiro.capturarEvento()

    tabuleiro = xadrez.pegarTabuleiro()

    # linhaOrigem : int
    # linhaDestino : int
    # colunaOrigem : int
    # colunaDestino : int

    # print(f"Informe a linha e a colunha de origem: ")
    # linhaOrigem, colunaOrigem = int(input("Linha:")), int(input("Coluna:"))

    # print(f"Informe a linha e a colunha de destino: ")
    # linhaDestino, colunaDestino = int(input("Linha:")), int(input("Coluna:"))

    # moverPeca = xadrez.moverPeca(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino)

    # if moverPeca == 0:
    #     print("ERRO: Coordenadas inválidas")

    # elif moverPeca == 2:
    #     print("ERRO: Peça não pode ser movida deste jeito")

    # elif moverPeca == 3:
    #     print("ERRO: Existe uma peça da mesma cor na posição escolhida")

    # desenharTabuleiro.pintarTelaTexto(tabuleiro)
