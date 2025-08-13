# Royal Rush 
## Integrantes da Equipe

- Ana Raquel Rodrigues  
- Clarissa Honório  
- Jaiane Evilásio  
- Lavinya Souza  
- Luciano Paixão  
- Marcos Silva  
 
---

## Descrição Geral do Projeto
O projeto “Royal Rush” é um jogo 2D desenvolvido em Python utilizando a biblioteca Pygame, criado para a disciplina de Introdução à Programação do curso de Sistemas de Informação do Centro de Informática da UFPE (CIn-UFPE).

No jogo, o Rei Gelado tenta capturar a Princesa Jujuba, que busca escapar pelo labirinto da Floresta Doce enquanto coleta itens para ajudá-la na fuga. O jogo permite que dois jogadores joguem simultaneamente no mesmo dispositivo, cada um controlando um dos personagens com objetivos opostos.

Com uma ambientação inspirada na temática do desenho “Hora de Aventura”, o jogo proporciona uma experiência interativa, unindo elementos de estratégia, rapidez e cooperação na mesma tela.

## Estrutura do Projeto

```
Royal_Rush/
├── assets/                  # Recursos do jogo
│   ├── graphics/            # Imagens dos sprites e do mapa
│   └── levels/              # Arquivos de nível
├── src/                     # Código-fonte do jogo
│   ├── config/              # Arquivos de configuração
│   ├── core/                # Lógica central do jogo
│   ├── entities/            # Entidades e personagens do jogo
│   │   ├── bullet/          # Representação das balas
│   │   ├── character/       # Representação dos personagens (Inimigos e o jogador)
│   │   ├── collectable/     # Representação dos coletáveis
│   │   └── world/           # Representação do mundo e seus elementos
│   ├── off_game_screens/    # Telas de menu, game over, etc.
│   ├── __init__.py          # Módulo de inicialização
│   └── entities_enum.py     # Enumeração de entidades
├── .gitignore               # Arquivos e diretórios ignorados pelo Git
├── README.md                # Relatório/documentação do projeto
├── main.py                  # Arquivo principal que inicia o jogo
└── requirements.txt         # Dependências do projeto
```


---

## Arquitetura do Projeto

O projeto foi desenvolvido em Python, utilizando a biblioteca Pygame. A estrutura do código foi organizada em três classes principais:

- **`Jogador`**: Responsável por representar os personagens controlados (Princesa Jujuba e Rei Gelado), com atributos como posição, velocidade, estado atual e imagem associada. Essa classe também gerencia a movimentação e as interações básicas dos personagens dentro do labirinto.
- **`ObjetoJogo`**: Gerencia os itens coletáveis distribuídos no mapa, incluindo a lógica para sua geração aleatória, renderização na tela e efeitos temporários que modificam a jogabilidade quando coletados pelos jogadores.
- **`Jogo`**: Controla o loop principal do jogo, responsável por atualizar a tela, processar eventos de entrada (como teclas pressionadas), verificar colisões entre jogadores e objetos, aplicar regras de vitória e derrota, e administrar o fluxo geral da aplicação.
Variáveis principais foram definidas no início do código, como largura e altura da tela, caminhos das imagens, velocidades dos personagens e estrutura do labirinto.

---

## Capturas de Tela
### Tela Inicial:
<img width="712" height="570" alt="image" src="https://github.com/user-attachments/assets/235986c7-be9d-42d7-ae68-b211683a309c" />


### História:
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/c5c4d0ba-9c85-46b7-aa59-60c78555f035" />


### Como Jogar:
<img width="687" height="591" alt="image" src="https://github.com/user-attachments/assets/35247b3f-45d7-4329-a925-31541204a846" />


### Labirinto:
<img width="1179" height="544" alt="image" src="https://github.com/user-attachments/assets/271fac9d-f4d6-4ce7-8074-c34af3b0de18" />


## Ferramentas e Justificativas

- **Python**: Linguagem utilizada na disciplina, de fácil leitura e adequada para jogos simples.
- **Pygame**: Biblioteca que permite a criação de jogos 2D com recursos gráficos, sons e controle de eventos de teclado.
- **GitHub**: Controle de versão e colaboração eficiente entre os membros do grupo.
- **sys**: Utilizada para encerrar o programa imediatamente após o usuário fechar a janela.
- **random**: Utilizada para gerar elementos ou eventos aleatórios no jogo.
- **os**: Utilizada para manipulação de caminhos e importação de arquivos (imagens, sons).

---

## Divisão de Trabalho

- Inicialmente, Jaiane Evilásio elaborou a base lógica do código, e, a partir dela, todo o grupo contribuiu para o aprimoramento, adicionando recursos como o temporizador, a lógica de exibição dos coletáveis e outras funcionalidades.

- Após consolidarmos essa base, realizamos uma reunião para definir a temática do jogo e, juntos, escolhemos criar um “Polícia e Ladrão” inspirado no universo de “Hora de Aventura”, em que o Rei Gelado tenta capturar a Princesa Jujuba, enquanto ela foge do temível vilão.

- Na etapa visual, Lavinya Souza, Clarissa Honório e Ana Raquel Rodrigues lideraram a criação das imagens temáticas, mas todos colaboraram com ideias e ajustes até a implementação final no código.

- Por fim, Marcos Silva e Luciano Paixão ficaram responsáveis pela documentação (README.md, apresentação de slides e preenchimento dos acompanhamentos), com apoio e revisão de todo o grupo.

- Assim, apesar da divisão inicial de tarefas, todo o desenvolvimento lógica, programação, arte e documentação foi fruto de um trabalho conjunto e colaborativo.

---

## Conceitos Utilizados na Disciplina

- **Estruturas condicionais**: Utilizadas para controlar a movimentação dos personagens e verificar eventos no jogo.
- **Estruturas de repetição**: Utilizadas no loop principal para manter o jogo em execução e verificar constantemente as condições de término.
- **Listas**: Utilizadas para criar e manipular o labirinto do jogo, facilitando a visualização e definição de obstáculo e para verificar efeitos dos coletáveis, gerar posições aleatórias e verificar a presença de objetos em determinadas posições.
- **Funções**: Criadas para verificar efeitos dos coletáveis, gerar posições aleatórias e verificar a presença de objetos em determinadas posições.
- **Tuplas**: Definição de constantes, como cores.
- **Dicionários**: Mapeamento de imagens e efeitos.
- **Programação orientada a objetos**: Aplicada na criação das classes principais, como Jogador, ObjetoJogo e Jogo.

---

## Desafios, Erros e Lições Aprendidas

**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**  
O maior erro foi tentar unificar as alterações de todos os membros diretamente na branch principal (`main`), o que gerou conflitos de código. Após perceber o problema, organizamos as contribuições por meio de branches de teste individuais e realizamos as fusões com maior cautela.

**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**  
O maior desafio foi a adaptação da movimentação de dois jogadores simultaneamente no mesmo teclado, garantindo fluidez sem sobreposição de comandos. Isso foi solucionado com o uso de eventos do Pygame e testes frequentes em notebooks, verificando o conforto de cada lado do teclado.

**Quais as lições aprendidas durante o projeto?**  
- A importância de uma boa organização com controle de versão desde o início.
- A eficácia da divisão de tarefas bem definida.
- O valor de testes constantes e colaboração entre os membros.
- A utilidade da programação orientada a objetos para modularização de jogos.

---

## Instruções de Execução

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Instale as dependências:
```bash
pip install pygame
```

3. Execute o jogo:
```bash
python jogo.py
```

---

## Controles

Este é um jogo para dois jogadores jogando no mesmo dispositivo. As teclas foram escolhidas considerando a posição física no teclado, especialmente em notebooks.

| Ação                  | Princesa Jujuba (Jogador 1) | Rei Gelado (Jogador 2) |
|-----------------------|-----------------------------|-------------------------|
| Mover para cima       | W                           | Seta para cima          |
| Mover para baixo      | S                           | Seta para baixo         |
| Mover para a esquerda | A                           | Seta para a esquerda    |
| Mover para a direita  | D                           | Seta para a direita     |
