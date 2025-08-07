import pygame
import random
import os
from collections import Counter
pygame.init()

LARGURA_TELA = 1200
ALTURA_TELA = 800
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Princess Escape")

BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
COR_CAMINHO = (0, 100, 0)

LABIRINTO_STR = [
    "#################################",
    "#     #       #       #         #",
    "# ### # ##### # ### ##### ##### #",
    "# #   #     #   # #     #     # #",
    "# # ##### # ##### # ### # ### # #",
    "# #     # #     #   #   #   #   #",
    "# ##### # ### # ##### ##### ### #",
    "#     #   #   #     #     #     #",
    "##### ### # ####### # ######### #",
    "#   #     #   #     #         # #",
    "# # ####### # # ########### # # #",
    "# #         #   #         # #   #",
    "# ### ####### # # ####### # ### #",
    "#             #   #             #",
    "#################################",
]
LABIRINTO = [list(linha) for linha in LABIRINTO_STR]

TAMANHO_CELULA = min(LARGURA_TELA // len(LABIRINTO[0]), ALTURA_TELA // len(LABIRINTO))

LARGURA_LABIRINTO = len(LABIRINTO[0]) * TAMANHO_CELULA
ALTURA_LABIRINTO = len(LABIRINTO) * TAMANHO_CELULA

OFFSET_X = (LARGURA_TELA - LARGURA_LABIRINTO) // 2
OFFSET_Y = (ALTURA_TELA - ALTURA_LABIRINTO) // 2


CAMINHO_IMAGENS = "assets"

FUNDO = pygame.transform.scale(
    pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'fundo.JPG')),
    (LARGURA_TELA, ALTURA_TELA)
)

IMAGENS = {
    'ladrao': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'ladrao.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'policia': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'policia.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'acelera_policia': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'gunter5.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'desacelera_policia': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'desacelera_policia.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'acelera_ladrao': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'mentol.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'arma': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'gema22.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    
}


VELOCIDADE_PADRAO = 150
VELOCIDADE_ACELERADA = 50
VELOCIDADE_DESACELERADA = 250
DURACAO_EFEITO = 5000  

def formatar_itens(contador):
    return "\n".join([f"- {item.replace('_', ' ').capitalize()}: {qtd}" for item, qtd in contador.items()])

class Jogador:
    def __init__(self, x, y, imagem, teclas, tipo):
        self.x = x
        self.y = y
        self.imagem = imagem
        self.teclas = teclas
        self.tipo = tipo
        self.velocidade = VELOCIDADE_PADRAO
        self.tempo_proximo = 0
        self.efeito_ate = 0
        self.congelado_ate = 0
        self.coletados = []

    def desenhar(self):
        TELA.blit(self.imagem, (self.x * TAMANHO_CELULA + OFFSET_X, self.y * TAMANHO_CELULA + OFFSET_Y))

    def mover(self, teclas_pressionadas, agora):
        if agora < self.tempo_proximo:
            return
        if self.tipo == 'policia' and agora < self.congelado_ate:
            return

        dx = dy = 0
        if teclas_pressionadas[self.teclas['up']]:
            dy = -1
        elif teclas_pressionadas[self.teclas['down']]:
            dy = 1
        elif teclas_pressionadas[self.teclas['left']]:
            dx = -1
        elif teclas_pressionadas[self.teclas['right']]:
            dx = 1

        novo_x, novo_y = self.x + dx, self.y + dy
        if 0 <= novo_y < len(LABIRINTO) and 0 <= novo_x < len(LABIRINTO[0]) and LABIRINTO[novo_y][novo_x] != '#':
            self.x, self.y = novo_x, novo_y
            self.tempo_proximo = agora + self.velocidade

    def aplicar_efeito(self, tipo_objeto, agora, jogo=None):
        if tipo_objeto == 'acelera_policia' and self.tipo == 'policia':
            self.velocidade = VELOCIDADE_ACELERADA
            self.efeito_ate = agora + DURACAO_EFEITO
        elif tipo_objeto == 'desacelera_policia' and self.tipo == 'policia':
            self.velocidade = VELOCIDADE_DESACELERADA
            self.efeito_ate = agora + DURACAO_EFEITO
        elif tipo_objeto == 'acelera_ladrao' and self.tipo == 'ladrao': #policial fica congelado
            if jogo:
                jogo.policia.congelado_ate = agora + DURACAO_EFEITO

    def verificar_efeito(self, agora):
        if agora > self.efeito_ate:
            self.velocidade = VELOCIDADE_PADRAO

class ObjetoJogo:
    TIPOS = ['acelera_policia', 'desacelera_policia', 'acelera_ladrao', 'arma'] #"acelera ladrao" é o objeto que congela o policial

    def __init__(self, x, y, tipo, criado_em):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.criado_em = criado_em

    def desenhar(self):
        TELA.blit(IMAGENS[self.tipo], (self.x * TAMANHO_CELULA + OFFSET_X, self.y * TAMANHO_CELULA + OFFSET_Y))

class Jogo:
    DURACAO_OBJETO = 8000      
    INTERVALO_NOVO_OBJETO = 4000  
    TEMPO_PARTIDA = 90 * 1000    #90 segundos

    def __init__(self):
        self.labirinto = LABIRINTO
        self.ladrao = Jogador(1, 1, IMAGENS['ladrao'], 
            {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d}, 'ladrao')
        self.policia = Jogador(len(LABIRINTO[0]) - 2, len(LABIRINTO) - 2, IMAGENS['policia'], 
            {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}, 'policia')
        self.objetos = []
        self.tempo_ultimo_objeto = 0
        self.rodando = True
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.fila_objetos = []
        self.gerar_fila_objetos()

        self.tempo_inicio = pygame.time.get_ticks()

        self.fonte = pygame.font.SysFont(None, 36)
        self.vencedor = None 
        self.mensagem_vitoria = ""

    def gerar_fila_objetos(self): #aqui podemos manipular a quantidade de vezes que um objeto aparece
        fila = []
        fila += ['arma'] * 7
        fila += ['acelera_policia'] * 2
        fila += ['desacelera_policia'] * 2
        fila += ['acelera_ladrao'] * 2
        random.shuffle(fila)
        self.fila_objetos = fila

    def encontrar_posicao_aleatoria(self):
        vazios = []
        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                if celula == ' ' and not self.tem_objeto_na_posicao(x, y) and (x, y) != (self.ladrao.x, self.ladrao.y) and (x, y) != (self.policia.x, self.policia.y):
                    vazios.append((x, y))
        return random.choice(vazios) if vazios else None

    def tem_objeto_na_posicao(self, x, y):
        for obj in self.objetos:
            if obj.x == x and obj.y == y:
                return True
        return False

    def gerar_objeto(self, agora):
        if not self.fila_objetos:
            return
        if agora - self.tempo_ultimo_objeto >= self.INTERVALO_NOVO_OBJETO:
            tipo = self.fila_objetos.pop(0)
            pos = self.encontrar_posicao_aleatoria()
            if pos:
                novo_objeto = ObjetoJogo(pos[0], pos[1], tipo, criado_em=agora)
                self.objetos.append(novo_objeto)
                self.tempo_ultimo_objeto = agora

    def limpar_objetos_expirados(self, agora):
        self.objetos = [obj for obj in self.objetos if agora - obj.criado_em < self.DURACAO_OBJETO]

    def desenhar_labirinto(self):
        TELA.blit(FUNDO, (0, 0))
        COR_LABIRINTO = (0, 100, 0)
        espessura_linha = 2  # linha fina e contínua

        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                if celula == '#':
                    esquerda = x * TAMANHO_CELULA + OFFSET_X
                    topo = y * TAMANHO_CELULA + OFFSET_Y
                    direita = esquerda + TAMANHO_CELULA
                    baixo = topo + TAMANHO_CELULA

                    # desenha as 4 linhas da célula
                    pygame.draw.line(TELA, COR_LABIRINTO, (esquerda, topo), (direita, topo), espessura_linha)     # topo
                    pygame.draw.line(TELA, COR_LABIRINTO, (direita, topo), (direita, baixo), espessura_linha)     # direita
                    pygame.draw.line(TELA, COR_LABIRINTO, (direita, baixo), (esquerda, baixo), espessura_linha)   # baixo
                    pygame.draw.line(TELA, COR_LABIRINTO, (esquerda, baixo), (esquerda, topo), espessura_linha)   # esquerda

    def desenhar_objetos(self):
        for obj in self.objetos:
            obj.desenhar()

    def desenhar_texto(self, texto, x, y, cor=BRANCO):
        img_texto = self.fonte.render(texto, True, cor)
        TELA.blit(img_texto, (x, y))

    def verificar_coletas(self, agora):
        for jogador in [self.ladrao, self.policia]:
            for obj in self.objetos[:]:  # faz uma cópia da lista para evitar problemas ao remover
                if jogador.x == obj.x and jogador.y == obj.y:
                    if obj.tipo == 'arma' and jogador.tipo == 'ladrao':
                        jogador.coletados.append(obj.tipo)
                        self.objetos.remove(obj)  # Remove o objeto coletado!
                        if jogador.coletados.count('arma') >= 5:
                            self.vencedor = 'Ladrão'
                            self.mensagem_vitoria = "Ladrão venceu coletando 5 armas!"
                            self.rodando = False

                    elif obj.tipo == 'acelera_policia' and jogador.tipo == 'policia':
                        jogador.coletados.append(obj.tipo)
                        jogador.aplicar_efeito(obj.tipo, agora, jogo=self)
                        self.objetos.remove(obj)

                    elif obj.tipo == 'desacelera_policia' and jogador.tipo == 'policia':
                        jogador.coletados.append(obj.tipo)
                        jogador.aplicar_efeito(obj.tipo, agora, jogo=self)
                        self.objetos.remove(obj)

                    elif obj.tipo == 'acelera_ladrao' and jogador.tipo == 'ladrao':
                        jogador.coletados.append(obj.tipo)
                        jogador.aplicar_efeito(obj.tipo, agora, jogo=self)
                        self.objetos.remove(obj)

    def mostrar_tela_vitoria(self):
        duracao_exibicao = 3000  
        inicio_vitoria = pygame.time.get_ticks()
        while pygame.time.get_ticks() - inicio_vitoria < duracao_exibicao:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            TELA.fill(PRETO)
            texto_img = self.fonte.render(self.mensagem_vitoria, True, BRANCO)
            ret_texto = texto_img.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2))
            TELA.blit(texto_img, ret_texto)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def loop_principal(self):
        agora = pygame.time.get_ticks()
        self.gerar_objeto(agora)

        while self.rodando:
            agora = pygame.time.get_ticks()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            teclas = pygame.key.get_pressed()
            self.ladrao.verificar_efeito(agora)
            self.policia.verificar_efeito(agora)

            self.ladrao.mover(teclas, agora)
            self.policia.mover(teclas, agora)

            self.verificar_coletas(agora)

            self.limpar_objetos_expirados(agora)

            self.gerar_objeto(agora)

            tempo_passado = agora - self.tempo_inicio
            tempo_restante_ms = max(0, self.TEMPO_PARTIDA - tempo_passado)

            if tempo_restante_ms == 0 and not self.vencedor:
                self.vencedor = 'Ladrão'
                self.mensagem_vitoria = "Ladrão venceu por tempo esgotado!"
                self.rodando = False

            if self.policia.x == self.ladrao.x and self.policia.y == self.ladrao.y and not self.vencedor:
                self.vencedor = 'Polícia'
                self.mensagem_vitoria = "Polícia venceu pegando o ladrão!"
                self.rodando = False

            self.desenhar_labirinto()
            self.desenhar_objetos()
            self.ladrao.desenhar()
            self.policia.desenhar()

            minutos = tempo_restante_ms // 60000
            segundos = (tempo_restante_ms % 60000) // 1000
            tempo_formatado = f"{minutos}:{segundos:02d}"
            #pra contar o numero de objetos 
            self.desenhar_texto(f"{tempo_formatado}", 930,10)
            cont_ladrao = Counter(jogo.ladrao.coletados)
            cont_policia = Counter(jogo.policia.coletados)
            #formatacao dos colecionáveis 
            texto_ladrao = "Ladrão:" + formatar_itens(cont_ladrao)
            print()
            texto_policia = "Polícia:" + formatar_itens(cont_policia)
            print()

            # Exibe na tela
            self.desenhar_texto(texto_ladrao, 10, 40)
            self.desenhar_texto(texto_policia, 10, 60)  

            pygame.display.flip()
            self.clock.tick(self.fps)

        if self.vencedor:
            print(f"{self.vencedor} venceu!")
            self.mostrar_tela_vitoria()

        pygame.quit()

jogo = Jogo()
jogo.loop_principal()
