import pygame 
import os

pygame.init()

#informações da tela
LARGURA_TELA = 1000
ALTURA_TELA = 750
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Ladrão e Polícia - com Classes")

#cores usadas
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
COR_SAIDA = (0, 255, 0)
COR_CAMINHO = (0, 100, 0)

#Labirinto
LABIRINTO_STR = [
    "#################################",
    "#S                              #",
    "# ##  ####  ##  ## ### ####  ## #",
    "# #   #     #   #  # # #    #   #",
    "# # # # ### # # # ## # # ### # ##",
    "# # # # # # # # #  # # # # # #  #",
    "# #   # # # # # #  #   # # # #  #",
    "# ##### # # # ###  # # # ### # ##",
    "# #   # # # # # #  # # # #   #  #",
    "# # # # # # # # #  # # # # # # ##",
    "# # # # # # # # #  # # # # # #  #",
    "# # # # # # # # #  # # # # # # ##",
    "# # # # # # # # #  # # # # # #  #",
    "# # # # # # # # #  # # # # # # ##",
    "#                               #",
    "#################################",
]
LABIRINTO = [list(linha) for linha in LABIRINTO_STR]

#tamanho das células
TAMANHO_CELULA = min(LARGURA_TELA // len(LABIRINTO[0]), ALTURA_TELA // len(LABIRINTO))
LARGURA_LABIRINTO = len(LABIRINTO[0]) * TAMANHO_CELULA
ALTURA_LABIRINTO = len(LABIRINTO) * TAMANHO_CELULA
OFFSET_X = (LARGURA_TELA - LARGURA_LABIRINTO) // 2
OFFSET_Y = (ALTURA_TELA - ALTURA_LABIRINTO) // 2


IMAGENS = {}
IMAGENS['ladrao'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'ladrao.png')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['policia'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'policia.png')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['acelera_ladrao'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'acelera_ladrao.png')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['desacelera_ladrao'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'desacelera_ladrao.png')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['acelera_policia'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'acelera_policia.png')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['desacelera_policia'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'desacelera_policia.png')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['coletável']=pygame.transform.scale(pygame.image.load(os.path.join('.', 'arma.png')).convert_alpha(),(TAMANHO_CELULA, TAMANHO_CELULA))

#Velocidades e durações
VELOCIDADE_MS_PADRAO = 100
VELOCIDADE_MS_ACELERADA = 50
VELOCIDADE_MS_DESACELERADA = 200
DURACAO_EFEITO_MS = 5000
