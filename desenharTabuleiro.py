import pygame

pygame.init()

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
        

