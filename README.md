# Minimum Spanning Tree

**Número da Lista**: 23<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0055006  |  Gian Medeiros Rosa |
| 20/0073249  |  Pedro Vitor Augusto de Jesus |

## Sobre

Este algoritmo é um aplicativo de interface gráfica que permite a criação e visualização de uma Árvore Geradora Mínima (MST) usando o algoritmo de Prim. A interface é construída utilizando a biblioteca `pygame` e permite a interação do usuário para adicionar nós e arestas ao grafo e, em seguida, calcular a MST.
A ideia é que possa ser utilizado como uma ferramenta de aprendizado para visualizar o funcionamento do algoritmo de Prim e a construção de uma MST.

## Screenshots

![image](https://github.com/user-attachments/assets/ae423559-2b30-4831-9b63-545e65c7d4be)
![image](https://github.com/user-attachments/assets/25953580-83cb-441f-b9dd-e31cc8572598)

## Instalação

### Pré-requisitos

- Python 3.x
- Pygame
- Módulos adicionais:
  - `src.back.prim`
  - `src.front.colors`
  - `src.front.edge`
  - `src.front.node`


1. **Instale o pygame:**
   ```sh
   pip install pygame
   ```

## Uso

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

## Apresentação

https://youtu.be/czThOZ6x0Wk

## Outros

- A interação é baseada em eventos do pygame, como cliques e pressionamento de teclas.
- O cálculo da MST utiliza o algoritmo de Prim, implementado no módulo `Graph`.
