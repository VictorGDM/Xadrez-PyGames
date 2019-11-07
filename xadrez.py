import pygame

pygame.init()

tabuleiro = [
    ['tp', 'cp', 'bp', 'dp', 'rp', 'bp', 'cp', 'tp'],
    ['pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp'],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb'],
    ['tb', 'cb', 'bb', 'db', 'rb', 'bb', 'cb', 'tb']
]

pecasPretas = ['tp', 'cp', 'bp', 'dp', 'rp', 'pp']
pecasBrancas = ['tb', 'cb', 'bb', 'db', 'rb', 'pb']

def peaoComerPeca(linhaOrigem, colunaOrigem):
    comer = False
    peca : str

    peca = tabuleiro[linhaOrigem][colunaOrigem]

    linhaAdjacente = (linhaOrigem + 1) if (peca == "pp") else (linhaOrigem - 1)
    adjacenteEsquerdo: colunaOrigem - 1
    adjacenteDireito: colunaOrigem + 1
    
    if (peca == "pp"):
        if (tabuleiro[linhaAdjacente][adjacenteDireito] in pecasBrancas) or (tabuleiro[linhaAdjacente][adjacenteEsquerdo] in pecasBrancas):
            comer = True
        else:
            return comer

    elif (peca == "pb"):
        if (tabuleiro[linhaAdjacente][adjacenteDireito] in pecasBrancas) or (tabuleiro[linhaAdjacente][adjacenteEsquerdo] in pecasBrancas):
            comer = True
        else:
            return comer

    else:
        return comer


    


def moverPeca(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino):
    mover = False
    peca : str

    deslocVertical = abs(linhaDestino - linhaOrigem)
    deslocHorizontal = abs(colunaDestino - colunaOrigem)

    if (
        linhaOrigem >= 0 and linhaOrigem < 8 and colunaOrigem >= 0 and colunaOrigem < 8
    ) and (
        linhaDestino >= 0 and linhaDestino < 8 and colunaDestino >= 0 and colunaDestino < 8
    ):
        peca = tabuleiro[linhaOrigem][colunaOrigem]

        if (peca == "tp" or peca == "tb") and (deslocVertical == 0 or deslocHorizontal == 0):
            mover = True

        if (peca == "bp" or peca == "bb") and (deslocVertical == deslocHorizontal):
            mover = True

        if (peca == "cp" or peca == "cb") and (
            (deslocVertical == 1 and deslocHorizontal == 2) or (deslocVertical == 2 and deslocHorizontal == 1)):
            mover = True

        if (peca == "dp" or peca == "db") and (
            (deslocVertical == deslocHorizontal) or (deslocVertical == 0 or deslocHorizontal == 0)):
            mover = True

        if (peca == "rp" or peca == "rb") and (
            (deslocVertical >= 0 and deslocVertical <= 1) and (deslocHorizontal >= 0 and deslocHorizontal <= 1)):
            mover = True

        if (peca == "pp") and ((linhaDestino - linhaOrigem) == 1) and (deslocHorizontal == 0):
            mover = True

        if (peca == "pb") and ((linhaOrigem - linhaDestino) == 1) and (deslocHorizontal == 0):
            mover = True

        if (peca == "rp" or peca == "rb") and (
            (deslocVertical >= 0 and deslocVertical <= 1) and (deslocHorizontal >= 0 and deslocHorizontal <= 1)):
            mover = True

        if (peca in pecasPretas) and (tabuleiro[linhaDestino][colunaDestino] in pecasBrancas):
            mover = True
        
        else:
            return 3

        if (peca in pecasBrancas) and (tabuleiro[linhaDestino][colunaDestino] in pecasPretas):
            mover = True
        
        else:
            return 3

        if mover == True:
            tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linhaOrigem][colunaOrigem]
            tabuleiro[linhaOrigem][colunaOrigem] = "  "
            return 1

        else:
            return 2

    else:
        return 0