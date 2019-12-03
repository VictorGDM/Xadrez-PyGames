import pygame, sys
import crgImg, xadrez, pecas

pygame.init()
#204x30 - 796x620
tabuleiro = xadrez.pegarTabuleiro()
laguraTabuleiro = 592
alturaTabuleiro = 592

linhaOrigem = -1
colunaOrigem = -1

def sonClick():
    pygame.mixer.music.load('sons/click/click.mp3')
    pygame.mixer.music.play()

def cavalo():
    pygame.mixer.music.load('sons/cavalo/cavalo.mp3')
    pygame.mixer.music.play()

def bispo():
    pygame.mixer.music.load('sons/bispo/bispo.mp3')
    pygame.mixer.music.play()

def torre():
    pygame.mixer.music.load('sons/torre/torre.mp3')
    pygame.mixer.music.play()


def capturarEvento():
    global linhaOrigem, colunaOrigem
    objPeca = pecas.criarPeca()

    w = laguraTabuleiro / 8
    h = alturaTabuleiro / 8

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            sonClick()
            x, y = pygame.mouse.get_pos()
            x -= 204
            y -= 30

            colunaClic = int(x / w)
            linhaClic = int(y / h)

            print(f'{colunaClic} {x} / {linhaClic} {y}')

            if (x >= 0 and x <= 592) and (y >= 0 and y <= 592):
                if (linhaOrigem == -1):
                    linhaOrigem = linhaClic
                    colunaOrigem = colunaClic
            
                else:
                    mp = xadrez.moverPeca(linhaOrigem, colunaOrigem, linhaClic, colunaClic)
                    if mp == 0 or mp == 2 or mp == 3:
                        linhaOrigem = -2
                        colunaOrigem = -2
                
                    if mp == 1:
                        linhaOrigem = -1
                        colunaOrigem = -1

                    linhaOrigem = -1
                    colunaOrigem = -1


def definirImagensDasPecas():
    pecas = {
        "pp" : crgImg.pp,
        "pb" : crgImg.pb,
        "bp" : crgImg.bp,
        "bb" : crgImg.bb,
        "cp" : crgImg.cp,
        "cb" : crgImg.cb,
        "tp" : crgImg.tp,
        "tb" : crgImg.tb,
        "dp" : crgImg.dp,
        "db" : crgImg.db,
        "rp" : crgImg.rp,
        "rb" : crgImg.rb,
    }
    return pecas

def pintarTelaGrafica(tabuleiro, tema, tela):
    tela = tela
    screen = pygame.display.set_mode((1000, 650))
    linha: int
    coluna: int
    w = int(laguraTabuleiro / 8)
    h = int(alturaTabuleiro / 8)
    x = 0
    y = 0

    cor = (0,0,0)

    screen.blit(tela, (0, 0))
    # pygame.draw.rect(screen, (0,0,0), [204, 30, 70, 70])

    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tema == 0:
                if (coluna + linha) % 2 == 0:
                    cor = (255,255,255)
                else:
                    cor = (0,0,0)
            if tema == 1:
                if (coluna + linha) % 2 == 0:
                    cor = (255,255,255)
                else:
                    cor = (77,77,77)
            if tema == 2:
                if (coluna + linha) % 2 == 0:
                    cor = (255,204,153)
                else:
                    cor = (102,51,0)
            if tema == 3:
                if (coluna + linha) % 2 == 0:
                    cor = (229,252,229)
                else:
                    cor = (75,143,75)

            x = (coluna * w) + 204
            y = (linha * h) + 30

            pygame.draw.rect(screen, cor, [x, y, w, h])

            peca = tabuleiro[linha][coluna]
            objPeca = pecas.criarPeca()
            
            if (peca != ' '):                
                if peca == 'pp':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'pb':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'bp':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'bb':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)

                if peca == 'cp':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'cb':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'tp':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'tb':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'dp':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'db':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'rp':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)
                
                if peca == 'rb':
                    objPeca.definirPosicao(peca, x , y)
                    objPeca.colocar(screen)

            if (linhaOrigem == linha and colunaOrigem == coluna):
                objPeca.definirPosicao('sq', x , y)
                objPeca.colocar(screen)

            if (linhaOrigem == -2 and colunaOrigem == -2):
                objPeca.definirPosicao('eq', x , y)
                objPeca.colocar(screen)

    pygame.display.update()
            

def pintarTelaTexto(tabuleiro):
    for linha in range(len(tabuleiro)):
        for redesenhar in range(3):
            for coluna in range(len(tabuleiro[linha])):

                peca = tabuleiro[linha][coluna]

                letra = "--" if (linha + coluna) % 2 == 0 else "  "
                letra = peca if (redesenhar == 1 and peca != "  " ) else letra

                if (linha + coluna) % 2 == 0:
                    print(f"--{letra}--", end="")
                else:
                    print(f"  {letra}  ", end="")
            print()
