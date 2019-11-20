import pygame

pygame.init()
#204x30 - 796x620
laguraTabuleiro = 592
alturaTabuleiro = 592

def pintarTelaGrafica(tabuleiro):
    screen = pygame.display.set_mode((1000, 650))
    linha: int
    coluna:int
    w = laguraTabuleiro / 8
    h = alturaTabuleiro / 8
    x = 0
    y = 0

    cor = (0,0,0)

    pygame.draw.rect(screen, (0,0,0), [204, 30, 70, 70])

    for linha in range(8):
        for coluna in range(8):
            if (coluna + linha) % 2 == 0:
                cor = (0,0,0)
            else:
                cor = (255,255,255)

            x = coluna * w
            y = linha * h

    pygame.draw.rect(screen, cor, [x, y, w, h])
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
