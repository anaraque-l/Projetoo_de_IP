import pygame
import random
import os
from collections import Counter
pygame.init()
pygame.mixer.init()



LARGURA_TELA = 1200
ALTURA_TELA = 800
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Princess Escape")

BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
COR_CAMINHO = (0, 100, 0)

MAPEAMENTO_PAREDES = {
    'C': 'coluna',
    'L': 'linha',
    'D': 'coluna_direita',
    'E': 'coluna_esquerda',
    'I': 'intersecao',
    'B': 'linha_baixo',
    'U': 'linha_cima',
    'W': 'cima_esquerda',
    'X': 'cima_direita',
    'Y': 'baixo_esquerda',
    'Z': 'baixo_direita'
}

LABIRINTO_STR = [
    "ZLLLLLBLLLLLLLBLLLLLLLBLLLLLLLLLY",
    "C     C       C       C         C",
    "C ZLL C LLLLY C ZLY LLULY LLLLY C",
    "C C   C     C   C C     C     C C",
    "C C LLULY C XLLLE C ZLL C LLY C C",
    "C C     C C     C   C   C   C   C",
    "C XLLLY C DLL C XLLLE LLULY XLL C",
    "C     C   C   C     C     C     C",
    "DLLLY XLL C LLILLLL C LLLLULLLY C",
    "C   C     C   C     C         C C",
    "C C XLLLLLW C C ZLLLULLLLLY C C C",
    "C C         C   C         C C   C",
    "C XLL LLLLLLW C C ZLLLLLL C XLL C",
    "C             C   C             C",
    "XLLLLLLLLLLLLLULLLULLLLLLLLLLLLLW",
]
LABIRINTO = [list(linha) for linha in LABIRINTO_STR]

TAMANHO_CELULA = min(LARGURA_TELA // len(LABIRINTO[0]), ALTURA_TELA // len(LABIRINTO))

LARGURA_LABIRINTO = len(LABIRINTO[0]) * TAMANHO_CELULA
ALTURA_LABIRINTO = len(LABIRINTO) * TAMANHO_CELULA

OFFSET_X = (LARGURA_TELA - LARGURA_LABIRINTO) // 2
OFFSET_Y = (ALTURA_TELA - ALTURA_LABIRINTO) // 2


CAMINHO_IMAGENS = "assets"

#inicialização e ajustes da musica e sons de coleta
pygame.mixer.music.load(os.path.join(CAMINHO_IMAGENS, 'musica.wav'))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
somdecoleta=pygame.mixer.Sound(os.path.join(CAMINHO_IMAGENS, 'somdagema.mp3'))
somdogunter=pygame.mixer.Sound(os.path.join(CAMINHO_IMAGENS, 'gunter.mp3'))
reiganhou=pygame.mixer.Sound(os.path.join(CAMINHO_IMAGENS, 'reiganhou.mp3'))
princesaganhou=pygame.mixer.Sound(os.path.join(CAMINHO_IMAGENS, 'princesa ganhou.mp3'))

FUNDO = pygame.transform.scale(
    pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'fundo.JPG')),
    (LARGURA_TELA, ALTURA_TELA)
)

IMAGENS = {
    # Imagens da princesa
    'princesa': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'princesa.png')), (TAMANHO_CELULA, TAMANHO_CELULA)), # Imagem padrão
    'princesa_D': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'princesaD.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'princesa_E': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'princesaE.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'princesa_BC': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'princesaBC.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),

    # Imagens do Rei Gelado
    'rei': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'rei.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'rei_D': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'reiD.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'rei_E': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'reiE.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'rei_BC': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'reiBC.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),

    # Outras imagens
    'gunter': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'gunter5.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'desacelera_policia': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'desacelera_policia.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'mentinha': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'mentol.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'gema': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'gema22.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'arvore': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'arvore.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'arbusto': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'abustoo.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'arvore_rosa': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'arvore_rosa.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),'coluna': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_coluna.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'linha': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_linha.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'coluna_direita': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_coluna_direita.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'coluna_esquerda': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_coluna_esquerda.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'intersecao': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_intersecao.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'linha_baixo': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_linha_baixo.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'linha_cima': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_linha_cima.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'cima_esquerda': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_cima_esquerda.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'cima_direita': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_cima_direita.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'baixo_esquerda': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_baixo_esquerda.png')), (TAMANHO_CELULA, TAMANHO_CELULA)),
    'baixo_direita': pygame.transform.scale(pygame.image.load(os.path.join(CAMINHO_IMAGENS, 'labirinto_baixo_direita.png')), (TAMANHO_CELULA, TAMANHO_CELULA))

    
}



VELOCIDADE_PADRAO = 150
VELOCIDADE_ACELERADA = 50
VELOCIDADE_DESACELERADA = 250
DURACAO_EFEITO = 5000  

def formatar_itens(contador):
    return "\n".join([f" - {item.replace('_', ' ').capitalize()}: {qtd}" for item, qtd in contador.items()])

class Jogador:
    def __init__(self, x, y, imagem, teclas, tipo):
        self.x = x
        self.y = y
        self.imagem_padrao = imagem 
        self.imagem_atual = imagem 
        self.teclas = teclas
        self.tipo = tipo
        self.velocidade = VELOCIDADE_PADRAO
        self.tempo_proximo = 0
        self.efeito_ate = 0
        self.congelado_ate = 0
        self.coletados = []

    def desenhar(self):
        TELA.blit(self.imagem_atual, (self.x * TAMANHO_CELULA + OFFSET_X, self.y * TAMANHO_CELULA + OFFSET_Y))

    def mover(self, teclas_pressionadas, agora):
        if agora < self.tempo_proximo:
            return
        if self.tipo == 'rei' and agora < self.congelado_ate:
            # deixa a imagem atual se o jogador estiver congelado
            return

        dx = dy = 0
        nova_imagem_key = None # chave para o dicionário de imagens

        if teclas_pressionadas[self.teclas['up']]:
            dy = -1
            if self.tipo == 'rei':
                nova_imagem_key = 'rei_BC'
            elif self.tipo == 'princesa':
                nova_imagem_key = 'princesa_BC'
        elif teclas_pressionadas[self.teclas['down']]:
            dy = 1
            if self.tipo == 'rei':
                nova_imagem_key = 'rei'
            elif self.tipo == 'princesa':
                nova_imagem_key = 'princesa'
        elif teclas_pressionadas[self.teclas['left']]:
            dx = -1
            if self.tipo == 'rei':
                nova_imagem_key = 'rei_E'
            elif self.tipo == 'princesa':
                nova_imagem_key = 'princesa_E'
        elif teclas_pressionadas[self.teclas['right']]:
            dx = 1
            if self.tipo == 'rei':
                nova_imagem_key = 'rei_D'
            elif self.tipo == 'princesa':
                nova_imagem_key = 'princesa_D'

        # Se houve movimento, atualize a imagem
        if nova_imagem_key:
            self.imagem_atual = IMAGENS[nova_imagem_key]
        
        novo_x, novo_y = self.x + dx, self.y + dy
        if 0 <= novo_y < len(LABIRINTO) and 0 <= novo_x < len(LABIRINTO[0]) and LABIRINTO[novo_y][novo_x] != '#':
            self.x, self.y = novo_x, novo_y
            self.tempo_proximo = agora + self.velocidade


    def aplicar_efeito(self, tipo_objeto, agora, jogo=None):
        if tipo_objeto == 'gunter':
            self.velocidade = VELOCIDADE_ACELERADA
            self.efeito_ate = agora + DURACAO_EFEITO
        elif tipo_objeto == 'desacelera_policia':
            self.velocidade = VELOCIDADE_DESACELERADA
            self.efeito_ate = agora + DURACAO_EFEITO
        elif tipo_objeto == 'mentinha' and self.tipo == 'princesa': #policial fica congelado
            if jogo:
                jogo.policia.congelado_ate = agora + DURACAO_EFEITO

    def verificar_efeito(self, agora):
        if agora > self.efeito_ate:
            self.velocidade = VELOCIDADE_PADRAO

class ObjetoJogo:
    TIPOS = ['gunter', 'desacelera_policia', 'mentinha', 'gema'] #"acelera ladrao" é o objeto que congela o policial

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

        self.ladrao = Jogador(1, 1, IMAGENS['princesa_E'], 
            {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d}, 'princesa')
        self.policia = Jogador(len(LABIRINTO[0]) - 2, len(LABIRINTO) - 2, IMAGENS['rei_E'], 
            {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}, 'rei')
        
        self.objetos = []
        self.tempo_ultimo_objeto = 0
        self.rodando = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.decoracoes = []
        
        
        self.gerar_cenario() 

        self.fila_objetos = []
        self.gerar_fila_objetos()
        self.tempo_inicio = pygame.time.get_ticks()
        self.fonte = pygame.font.SysFont(None, 36)
        self.vencedor = None 
        self.mensagem_vitoria = ""


        self.fila_objetos = []
        self.gerar_fila_objetos()

        self.tempo_inicio = pygame.time.get_ticks()

        self.fonte = pygame.font.SysFont(None, 36)
        self.vencedor = None 
        self.mensagem_vitoria = ""

    def gerar_fila_objetos(self): #aqui podemos manipular a quantidade de vezes que um objeto aparece
        fila = []
        fila += ['gema'] * 7
        fila += ['gunter'] * 2
        fila += ['desacelera_policia'] * 2
        fila += ['mentinha'] * 2
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
            self.gerar_fila_objetos()
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
        espessura_linha = 2

        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                if celula == '#':
                    # Verifica se tem decoração
                    decorado = False
                    for tipo in ['coluna', 'linha', 'coluna_direita', 'coluna_esquerda', 'intersecao', 'linha_baixo', 'linha_cima', 'cima_esquerda', 'cima_direita', 'baixo_esquerda', 'baixo_direita']:
                        if (x, y, tipo) in self.decoracoes:
                            imagem = IMAGENS.get(tipo)
                            if imagem:
                                TELA.blit(imagem, (x * TAMANHO_CELULA + OFFSET_X, y * TAMANHO_CELULA + OFFSET_Y))
                            decorado = True
                            break

                    if not decorado:
                        
                        esquerda = x * TAMANHO_CELULA + OFFSET_X
                        topo = y * TAMANHO_CELULA + OFFSET_Y
                        direita = esquerda + TAMANHO_CELULA
                        baixo = topo + TAMANHO_CELULA

                        pygame.draw.line(TELA, COR_LABIRINTO, (esquerda, topo), (direita, topo), espessura_linha)
                        pygame.draw.line(TELA, COR_LABIRINTO, (direita, topo), (direita, baixo), espessura_linha)
                        pygame.draw.line(TELA, COR_LABIRINTO, (direita, baixo), (esquerda, baixo), espessura_linha)
                        pygame.draw.line(TELA, COR_LABIRINTO, (esquerda, baixo), (esquerda, topo), espessura_linha)


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
                    if obj.tipo == 'gema' and jogador.tipo == 'princesa':
                        somdecoleta.play()
                        jogador.coletados.append(obj.tipo)
                        self.objetos.remove(obj)  # Remove o objeto coletado!
                        if jogador.coletados.count('gema') >= 5:
                            self.vencedor = 'Ladrão'
                            princesaganhou.play()
                            self.mensagem_vitoria = "A princesa conseguiu coletar as 5 gemas!"
                            self.rodando = False
                    elif obj.tipo == 'gema' and jogador.tipo == 'rei':
                         self.objetos.remove(obj) #se o policial toca e n remove sem coleta

                    elif obj.tipo == 'gunter': #ACELERA POLICIA EH PRA ACELERAR OS DOIS
                        somdogunter.play()
                        jogador.coletados.append(obj.tipo)
                        jogador.aplicar_efeito(obj.tipo, agora, jogo=self)
                        self.objetos.remove(obj)
                    
                    elif obj.tipo == 'desacelera_policia':# DESACELERA POLICIA PROS DOIS
                        jogador.coletados.append(obj.tipo)
                        jogador.aplicar_efeito(obj.tipo, agora, jogo=self)
                        self.objetos.remove(obj)
                    

                    elif obj.tipo == 'mentinha' and jogador.tipo == 'princesa':
                        jogador.coletados.append(obj.tipo)
                        jogador.aplicar_efeito(obj.tipo, agora, jogo=self)
                        self.objetos.remove(obj)
                    
                    elif obj.tipo == 'mentinha' and jogador.tipo == 'rei': #apenas remove
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

    def gerar_cenario(self):
        self.decoracoes = []  # Limpa as decorações de antes

        linhas = len(self.labirinto)
        colunas = len(self.labirinto[0])

        for y in range(linhas):
            for x in range(colunas):
                if self.labirinto[y][x] == '#':
                    

                    if y == linhas - 1:
                        #  linha  final  só arvore_rosa
                        self.decoracoes = [(dx, dy, t) for (dx, dy, t) in self.decoracoes if not (dx == x and dy == y)]
                        self.decoracoes.append((x, y, 'arvore_rosa'))
                    else:
                        if random.random() < 0.5:
                            self.decoracoes.append((x, y, 'arbusto'))
                        else:
                            self.decoracoes.append((x, y, 'arvore'))

        # Decorações fixas nos cantos 
        cantos_fixos = [
            (0, 0, 'arbusto'),
            (colunas - 1, 0, 'floresta'),
            (0, linhas - 1, 'arbusto'),
            (colunas - 1, linhas - 1, 'arvore_rosa'),
        ]

        for x, y, tipo in cantos_fixos:
            # Remove qualquer decoração existente nesse canto
            self.decoracoes = [(dx, dy, t) for (dx, dy, t) in self.decoracoes if not (dx == x and dy == y)]
            self.decoracoes.append((x, y, tipo))



    def eh_saida(self, x, y):
        if self.labirinto[y][x] != '#':
            return False

        linhas = len(self.labirinto)
        colunas = len(self.labirinto[0])

        if x == 0 or x == colunas - 1 or y == 0 or y == linhas - 1:
            # Se está na borda e tem um espaço livre ao lado, é saída
            if (x > 0 and self.labirinto[y][x - 1] == ' ') or \
            (x < colunas - 1 and self.labirinto[y][x + 1] == ' ') or \
            (y > 0 and self.labirinto[y - 1][x] == ' ') or \
            (y < linhas - 1 and self.labirinto[y + 1][x] == ' '):
                return True
        return False





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
                self.vencedor = 'Princesa'
                pygame.mixer.music.stop()
                princesaganhou.play()
                self.mensagem_vitoria = "O Rei Gelado não conseguiu capturar a Princesa a tempo!"
                self.rodando = False

            if self.policia.x == self.ladrao.x and self.policia.y == self.ladrao.y and not self.vencedor:
                self.vencedor = 'Rei'
                pygame.mixer.music.stop()
                reiganhou.play()
                self.mensagem_vitoria = "Oh não! O Rei Gelado capturou a Princesa Jujuba!"
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
            texto_ladrao = "Princesa Jujuba:" + formatar_itens(cont_ladrao)
            print()
            texto_policia = "Rei Gelado:" + formatar_itens(cont_policia)
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
