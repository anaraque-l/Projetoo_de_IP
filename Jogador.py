import pygame
from configuracoes import *

class Jogador:
    def __init__(self, x, y, imagem_sprite, teclas_movimento, tipo):
        self.x = x
        self.y = y
        self.imagem = imagem_sprite
        self.teclas = teclas_movimento
        self.tipo = tipo
        self.velocidade_ms = VELOCIDADE_MS_PADRAO
        self.tempo_proximo_movimento = 0
        self.tempo_efeito = 0
        if self.tipo == 'ladrao':
            self.contagemcoletaveis = 0

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x * TAMANHO_CELULA + OFFSET_X, self.y * TAMANHO_CELULA + OFFSET_Y))

    def mover(self, keys, agora):
        if agora >= self.tempo_proximo_movimento:
            proximo_x, proximo_y = self.x, self.y
            if keys[self.teclas['up']]: proximo_y -= 1
            elif keys[self.teclas['down']]: proximo_y += 1
            elif keys[self.teclas['left']]: proximo_x -= 1
            elif keys[self.teclas['right']]: proximo_x += 1

            if 0 <= proximo_y < len(LABIRINTO) and 0 <= proximo_x < len(LABIRINTO[0]) and LABIRINTO[proximo_y][proximo_x] != '#':
                self.x, self.y = proximo_x, proximo_y
                self.tempo_proximo_movimento = agora + self.velocidade_ms

    def verificar_efeito(self, agora):
        if self.tempo_efeito > agora:
            if self.velocidade_ms not in [VELOCIDADE_MS_ACELERADA, VELOCIDADE_MS_DESACELERADA]:
                self.velocidade_ms = VELOCIDADE_MS_PADRAO
        else:
            self.velocidade_ms = VELOCIDADE_MS_PADRAO

    def aplicar_efeito(self, tipo_objeto, agora):
        if tipo_objeto == 'acelera_ladrao' and self.tipo == 'ladrao':
            self.velocidade_ms = VELOCIDADE_MS_ACELERADA
        elif tipo_objeto == 'desacelera_ladrao' and self.tipo == 'ladrao':
            self.velocidade_ms = VELOCIDADE_MS_DESACELERADA
        elif tipo_objeto == 'acelera_policia' and self.tipo == 'policia':
            self.velocidade_ms = VELOCIDADE_MS_ACELERADA
        elif tipo_objeto == 'desacelera_policia' and self.tipo == 'policia':
            self.velocidade_ms = VELOCIDADE_MS_DESACELERADA

        self.tempo_efeito = agora + DURACAO_EFEITO_MS
