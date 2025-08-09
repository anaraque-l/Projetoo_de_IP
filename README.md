# Polícia e Ladrão: Aventura no Labirinto de *Hora de Aventura*

## Integrantes da Equipe

- Ana Raquel Rodrigues  
- Clarissa Honório  
- Jaiane Evilásio  
- Lavinya Souza  
- Luciano Paixão  
- Marcos Silva  
 

---

## Arquitetura do Projeto

O projeto foi desenvolvido em Python, utilizando a biblioteca Pygame. A estrutura do código foi organizada em três classes principais:

- **`Jogador`**: Responsável por representar os personagens controlados (Princesa Jujuba e Rei Gelado), com atributos como posição, velocidade e imagem.
- **`ObjetoJogo`**: Gerencia os itens coletáveis no mapa, incluindo sua geração aleatória, exibição e efeitos.
- **`Jogo`**: Controla o loop principal do jogo, renderiza a tela, verifica colisões e condições de vitória/derrota.

Variáveis principais foram definidas no início do código, como largura e altura da tela, caminhos das imagens, velocidades dos personagens e estrutura do labirinto.

As imagens e demais recursos visuais foram organizados em diretórios específicos, facilitando a manutenção do projeto.

---

## Capturas de Tela


## Ferramentas e Justificativas

- **Python**: Linguagem utilizada na disciplina, de fácil leitura e adequada para jogos simples.
- **Pygame**: Biblioteca que permite a criação de jogos 2D com recursos gráficos, sons e controle de eventos de teclado.
- **Git & GitHub**: Controle de versão e colaboração eficiente entre os membros do grupo.
- **GitHub Desktop**: Interface gráfica que facilitou a sincronização entre as branches e evitou conflitos de código.

---

## Divisão de Trabalho

| Integrante             | Atividades Desenvolvidas                                                         |
|------------------------|----------------------------------------------------------------------------------|
| Jaiane Evilásio        | Estruturação da lógica base do jogo                                             |
| Lavinya Souza          | Ambientação e adaptação visual temática                                          |
| Clarissa Honório       | Implementação gráfica do labirinto                                              |
| Ana Raquel Rodrigues   | Inserção de imagens e adaptação visual                                           |
| Marcos Silva           | Elaboração da documentação e README.md                                           |
| Luciano Paixão         | Preparação da apresentação final do projeto                                      |

l
---

## Conceitos Utilizados na Disciplina

- **Condicionais (`if`, `else`)**: Verificação de colisões e condições de vitória.
- **Laços de repetição (`while`, `for`)**: Loop principal do jogo e movimentação de personagens.
- **Listas**: Representação do labirinto e objetos do jogo.
- **Funções**: Reutilização de código para carregamento de imagens e verificação de estado.
- **Tuplas**: Definição de constantes, como cores.
- **Dicionários**: Mapeamento de imagens e efeitos.
- **Programação orientada a objetos**: Criação de classes `Jogador`, `ObjetoJogo` e `Jogo` para modularização do projeto.

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
