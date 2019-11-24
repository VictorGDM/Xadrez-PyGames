import pygame

def criarPeca():
    class peca(pygame.sprite.Sprite):
        def _init_(self):
            pygame.sprite.Sprite._init_(self)

        def definirPosicao(self, peca, x, y):
            self.peca = pygame.image.load(f'telas/jogo/pecas/{peca}.png')
            self.rect = self.peca.get_rect()
            self.rect.x = x
            self.rect.y = y

        def colocar(self, superfice):
            superfice.blit(self.peca, self.rect)

    return peca()