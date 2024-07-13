## Documentação de Uso do Algoritmo para Visualização de Árvore Geradora Mínima

### Descrição Geral

Este algoritmo é um aplicativo de interface gráfica que permite a criação e visualização de uma Árvore Geradora Mínima (MST) usando o algoritmo de Prim. A interface é construída utilizando a biblioteca `pygame` e permite a interação do usuário para adicionar nós e arestas ao grafo e, em seguida, calcular a MST.

### Pré-requisitos

- Python 3.x
- Pygame
- Módulos adicionais:
  - `src.back.prim`
  - `src.front.colors`
  - `src.front.edge`
  - `src.front.node`

### Instalação

1. **Instale o pygame:**
   ```sh
   pip install pygame
   ```

### Execução do Programa

1. **Execute o script `main.py`:**
   ```sh
   python main.py
   ```

### Uso da Interface

#### Janela Principal

- **Dimensões:** 800x600 pixels
- **Título:** "Minimal Spanning Tree"

#### Adicionando Nós

1. Clique com o botão esquerdo do mouse em qualquer lugar na janela para adicionar um nó.

#### Conectando Nós

1. Clique em um nó e, em seguida, clique em outro nó para conectar os dois.
2. Uma janela pop-up aparecerá solicitando o custo da aresta.
3. Digite o custo e pressione `Enter`.

#### Calculando a Árvore Geradora Mínima

1. Pressione a barra de espaço (`Space`) para calcular a MST.
2. As arestas que fazem parte da MST serão destacadas em verde.

#### Resetando a Cores das Arestas

1. Pressione a tecla `R` para resetar as cores das arestas.


### Observações

- A interação é baseada em eventos do pygame, como cliques e pressionamento de teclas.
- O cálculo da MST utiliza o algoritmo de Prim, implementado no módulo `Graph`.
