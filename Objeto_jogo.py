import pygame
import random
from configuracoes import *

class ObjetoJogo:
    TIPOS = ['acelera_ladrao', 'desacelera_ladrao', 'acelera_policia', 'desacelera_policia']
    TEMPO_DE_VIDA_MS = 10000
    TEMPO_DE_VIDA_Ms2 = 9000

    def __init__(self, x, y, diferenciacao=None):
        self.x = x
        self.y = y
        self.tipo = diferenciacao if diferenciacao else random.choice(self.TIPOS)
        self.imagem = IMAGENS[self.tipo]
        self.criacao = pygame.time.get_ticks()

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x * TAMANHO_CELULA + OFFSET_X, self.y * TAMANHO_CELULA + OFFSET_Y))
