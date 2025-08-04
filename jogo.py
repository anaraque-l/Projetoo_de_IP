import pygame
import random
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
IMAGENS['ladrao'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'ladrao.webp')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['policia'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'policia.webp')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['acelera_ladrao'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'acelera_ladrao.webp')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['desacelera_ladrao'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'desacelera_ladrao.webp')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['acelera_policia'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'acelera_policia.webp')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['desacelera_policia'] = pygame.transform.scale(pygame.image.load(os.path.join('.', 'desacelera_policia.webp')).convert_alpha(), (TAMANHO_CELULA, TAMANHO_CELULA))
IMAGENS['coletável']=pygame.transform.scale(pygame.image.load(os.path.join('.', 'arma.webp')).convert_alpha(),(TAMANHO_CELULA, TAMANHO_CELULA))

#Velocidades e durações
VELOCIDADE_MS_PADRAO = 100
VELOCIDADE_MS_ACELERADA = 50
VELOCIDADE_MS_DESACELERADA = 200
DURACAO_EFEITO_MS = 5000

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
        if self.tipo=='ladrao':
            self.contagemcoletaveis=0

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
            if self.velocidade_ms != VELOCIDADE_MS_ACELERADA and self.velocidade_ms != VELOCIDADE_MS_DESACELERADA:
                self.velocidade_ms = VELOCIDADE_MS_PADRAO
        else:
            self.velocidade_ms = VELOCIDADE_MS_PADRAO

    def aplicar_efeito(self, tipo_objeto, agora):
        if tipo_objeto == 'acelera_ladrao' and self.tipo == 'ladrao':
            self.velocidade_ms = VELOCIDADE_MS_ACELERADA
            self.tempo_efeito = agora + DURACAO_EFEITO_MS
        elif tipo_objeto == 'desacelera_ladrao' and self.tipo == 'ladrao':
            self.velocidade_ms = VELOCIDADE_MS_DESACELERADA
            self.tempo_efeito = agora + DURACAO_EFEITO_MS
        elif tipo_objeto == 'acelera_policia' and self.tipo == 'policia':
            self.velocidade_ms = VELOCIDADE_MS_ACELERADA
            self.tempo_efeito = agora + DURACAO_EFEITO_MS
        elif tipo_objeto == 'desacelera_policia' and self.tipo == 'policia':
            self.velocidade_ms = VELOCIDADE_MS_DESACELERADA
            self.tempo_efeito = agora + DURACAO_EFEITO_MS

class ObjetoJogo:
    TIPOS = ['acelera_ladrao', 'desacelera_ladrao', 'acelera_policia', 'desacelera_policia']
    TEMPO_DE_VIDA_MS = 10000
    TEMPO_DE_VIDA_Ms2=  9000

    def __init__(self, x, y, diferenciacao=None):
        self.x = x
        self.y = y
        if (diferenciacao):
            self.tipo=diferenciacao
        else:
            self.tipo = random.choice(self.TIPOS)
        self.imagem = IMAGENS[self.tipo]
        self.criacao = pygame.time.get_ticks()

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x * TAMANHO_CELULA + OFFSET_X, self.y * TAMANHO_CELULA + OFFSET_Y))

class Jogo:
    def __init__(self):
        self.rodando = True
        self.clock = pygame.time.Clock()
        self.fps = 35
        self.ladrao = Jogador(31, 1, IMAGENS['ladrao'], {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d}, 'ladrao')
        self.policia = Jogador(31, 14, IMAGENS['policia'], {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}, 'policia')
        self.saida_x, self.saida_y = 1, 1
        self.objetos = []
        self.coletaveis=[]
        self.tempo_proximo_objeto = pygame.time.get_ticks() + 10000
        self.tempo_proximo_coletavel=pygame.time.get_ticks()+ 9000
        
        # --- ADICIONADO: Configurações do timer ---
        self.tempo_limite = 120000  # 2 minutos em milissegundos
        self.tempo_inicio = pygame.time.get_ticks()
       

    def encontrar_posicao_aleatoria(self):
        vazios = []
        for y, linha in enumerate(LABIRINTO):
            for x, celula in enumerate(linha):
                if celula == ' ' and (x, y) not in [(self.saida_x, self.saida_y), (self.ladrao.x, self.ladrao.y), (self.policia.x, self.policia.y)]:
                    vazios.append((x, y))
        return random.choice(vazios) if vazios else None

    def criar_objeto(self):
        posicao = self.encontrar_posicao_aleatoria()
        if posicao:
            objeton=ObjetoJogo(posicao[0], posicao[1],diferenciacao=False)
            if(objeton.tipo!= 'coletável'):
                self.objetos.append(objeton)
    
    def criar_coletavel(self):
        posicao=self.encontrar_posicao_aleatoria()
        if posicao:
            self.coletaveis.append(ObjetoJogo(posicao[0], posicao[1], diferenciacao= 'coletável'))

    def desenhar_labirinto(self):
        TELA.fill(COR_CAMINHO)
        for y, linha in enumerate(LABIRINTO):
            for x, celula in enumerate(linha):
                rect = pygame.Rect(x * TAMANHO_CELULA + OFFSET_X, y * TAMANHO_CELULA + OFFSET_Y, TAMANHO_CELULA, TAMANHO_CELULA)
                if celula == '#':
                    pygame.draw.rect(TELA, BRANCO, rect)
                elif celula == 'S':
                    pygame.draw.rect(TELA, COR_SAIDA, rect)

    def desenhar_objetos(self):
        for objeto in self.objetos:
            objeto.desenhar(TELA)
        for coletavel in self.coletaveis:
            coletavel.desenhar(TELA)
    
    def verificar_colisoes(self, agora): 
        objetos_a_remover = []
        remover_coletaveis=[]
        for objeto in self.objetos:
            if agora - objeto.criacao > ObjetoJogo.TEMPO_DE_VIDA_MS:
                objetos_a_remover.append(objeto)
            elif (self.ladrao.x, self.ladrao.y) == (objeto.x, objeto.y):
                self.ladrao.aplicar_efeito(objeto.tipo, agora)
                objetos_a_remover.append(objeto)
            elif (self.policia.x, self.policia.y) == (objeto.x, objeto.y):
                self.policia.aplicar_efeito(objeto.tipo, agora)
                objetos_a_remover.append(objeto)

        for coletavel in self.coletaveis:
            if agora-coletavel.criacao > ObjetoJogo.TEMPO_DE_VIDA_Ms2:
                remover_coletaveis.append(coletavel)
            elif(self.ladrao.x, self.ladrao.y)==(coletavel.x,coletavel.y):
                self.ladrao.contagemcoletaveis+=1
                remover_coletaveis.append(coletavel)
            elif(self.policia.x, self.policia.y)==(coletavel.x,coletavel.y):
                remover_coletaveis.append(coletavel)

        for objeto in objetos_a_remover:
            self.objetos.remove(objeto)
        
        for coletavel in remover_coletaveis:
            self.coletaveis.remove(coletavel)

    def contadornatela(self):
        fonte=pygame.font.Font(None,36)
        contador=fonte.render(f'Armas: {self.ladrao.contagemcoletaveis}/5', True, PRETO)
        TELA.blit(contador,(10,10))

    # timer na tela 
    def desenhar_timer(self, agora):
        tempo_restante_ms = self.tempo_limite - (agora - self.tempo_inicio)
        if tempo_restante_ms < 0:
            tempo_restante_ms = 0
        
        segundos_totais = tempo_restante_ms // 1000
        minutos = segundos_totais // 60
        segundos = segundos_totais % 60

        texto_timer = f"Tempo: {minutos:02d}:{segundos:02d}"
        fonte = pygame.font.Font(None, 36)
        superficie_texto = fonte.render(texto_timer, True, PRETO)
        pos_x = LARGURA_TELA - superficie_texto.get_width() - 10
        TELA.blit(superficie_texto, (pos_x, 10))


    def verificar_fim_de_jogo(self, agora):
        fonte = pygame.font.Font(None, 74)

        # 1. Policial pega o Ladrão (Maior prioridade)
        if self.ladrao.x == self.policia.x and self.ladrao.y == self.policia.y:
            texto = fonte.render("A Polícia Pegou o Ladrão!", True, AZUL)
            TELA.blit(texto, texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2)))
            self.rodando = False

        # 2. Ladrão coleta todos os itens (Segunda prioridade)
        elif self.ladrao.contagemcoletaveis >= 5:
            texto = fonte.render('Ladrão Venceu!', True, VERMELHO)
            TELA.blit(texto, texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2)))
            self.rodando = False

        # 3. Tempo esgota (Menor prioridade)
        elif agora - self.tempo_inicio >= self.tempo_limite:
            texto = fonte.render("Tempo Esgotado! Policial Venceu!", True, AZUL)
            TELA.blit(texto, texto.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 2)))
            self.rodando = False
        
        # Se o jogo terminou, mostra a mensagem e espera um pouco
        if not self.rodando:
            pygame.display.flip()
            pygame.time.wait(3000)


    def loop_principal(self):
        while self.rodando:
            agora = pygame.time.get_ticks()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            #Apenas continua a lógica do jogo se self.rodando for True
            if self.rodando:
                if agora >= self.tempo_proximo_objeto:
                    self.criar_objeto()
                    self.tempo_proximo_objeto = agora + 10000
                
                if agora>=self.tempo_proximo_coletavel:
                    self.criar_coletavel()
                    self.tempo_proximo_coletavel=agora + 9000

                keys = pygame.key.get_pressed()
                self.ladrao.verificar_efeito(agora)
                self.policia.verificar_efeito(agora)
                self.ladrao.mover(keys, agora)
                self.policia.mover(keys, agora)
                self.verificar_colisoes(agora)

                #desenho
                self.desenhar_labirinto()
                self.desenhar_objetos()
                self.ladrao.desenhar(TELA)
                self.policia.desenhar(TELA)
                self.contadornatela()
           
                self.desenhar_timer(agora)
    
                self.verificar_fim_de_jogo(agora)
                
                pygame.display.flip()
                self.clock.tick(self.fps)

        pygame.quit()


jogo = Jogo()
jogo.loop_principal()
