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


def pegarTabuleiro():
    return tabuleiro


def xequeMate():
    xeque = True
    rp = 0
    rb = 0

    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if ('rp' == tabuleiro[linha][coluna]):
                rp += 1
                break

    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if ('rb' == tabuleiro[linha][coluna]):
                rb += 1
                break

    if ((rp == 1) and (rb == 1)):
        xeque = False
    else:
        xeque = True

    return xeque


def pecaDoMesmoTime(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino):
    peca = tabuleiro[linhaOrigem][colunaOrigem]
    eDoTime = False

    if (peca in pecasPretas) and (tabuleiro[linhaDestino][colunaDestino] in pecasPretas):
        eDoTime = True

    if (peca in pecasBrancas) and (tabuleiro[linhaDestino][colunaDestino] in pecasBrancas):
        eDoTime = True

    return eDoTime


def peaoComerPeca(linhaOrigem, colunaOrigem):
    comer = False
    peca: str

    peca = tabuleiro[linhaOrigem][colunaOrigem]
    linhaAdjacente = (linhaOrigem + 1) if (peca == "pp") else (linhaOrigem - 1)
    adjacenteEsquerdo = (colunaOrigem - 1)
    adjacenteDireito = (colunaOrigem + 1)

    if (peca == "pp"):
        if ((tabuleiro[linhaAdjacente][adjacenteDireito] in pecasBrancas)
            or (tabuleiro[linhaAdjacente][adjacenteEsquerdo] in pecasBrancas)) and(
            (colunaOrigem > 0 and colunaOrigem < 8) and (
                linhaAdjacente >= 0 and linhaAdjacente <= 7)
        ):
            comer = True

    if (peca == "pb"):
        if ((tabuleiro[linhaAdjacente][adjacenteDireito] in pecasPretas)
                or (tabuleiro[linhaAdjacente][adjacenteEsquerdo] in pecasPretas)) and (
                (colunaOrigem > 0 and colunaOrigem < 8) and (
                    linhaAdjacente >= 0 and linhaAdjacente <= 7)
        ):
            comer = True

    return comer


def moverPeca(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino):
    mover = False
    peca: str

    deslocVertical = abs(linhaDestino - linhaOrigem)
    deslocHorizontal = abs(colunaDestino - colunaOrigem)

    mesmoTime = pecaDoMesmoTime(linhaOrigem, colunaOrigem, linhaDestino, colunaDestino)
    xeque = xequeMate()

    print (xeque)

    if (
        linhaOrigem >= 0 and linhaOrigem < 8 and colunaOrigem >= 0 and colunaOrigem < 8
    ) and (
        linhaDestino >= 0 and linhaDestino < 8 and colunaDestino >= 0 and colunaDestino < 8
    ) and (
        deslocVertical + deslocHorizontal > 0
    ) and (
        mesmoTime == False
    ) and (
        xeque == False
    ):
        peca = tabuleiro[linhaOrigem][colunaOrigem]

        peaoComer = peaoComerPeca(linhaOrigem, colunaOrigem)

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

        if ((peca == "pp") and ((linhaDestino - linhaOrigem) == 1) and (deslocHorizontal == 0)) or (
                (peca == "pp") and (peaoComer == True)):
            mover = True

        if ((peca == "pb") and ((linhaOrigem - linhaDestino) == 1) and (deslocHorizontal == 0)) or (
                (peca == "pb") and (peaoComer == True)):
            mover = True

        if (peca == "rp" or peca == "rb") and (
                (deslocVertical >= 0 and deslocVertical <= 1) and (deslocHorizontal >= 0 and deslocHorizontal <= 1)):
            mover = True

        if mover == True:
            tabuleiro[linhaDestino][colunaDestino] = tabuleiro[linhaOrigem][colunaOrigem]
            tabuleiro[linhaOrigem][colunaOrigem] = "  "
            return 1

        else:
            return 2

    else:
        return 0
