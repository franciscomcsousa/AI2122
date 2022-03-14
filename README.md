# Inteligência Artificial 2021/22 (P3)

# Projeto: Numbrix

### 8 de março de 2022

## 1 Introdução

O projeto da unidade curricular de Inteligência Artificial (IA) tem como objetivo desenvolver
um programa em Python que resolva o problema Numbrix utilizando técnicas de procura de
IA.

## 2 Descrição do problema

O problema Numbrix é baseado no jogo Hidato que foi introduzido por Gyora Benedek na
sequência do sucesso do jogo Sudoku.
O jogo decorre sobre um tabuleiro com umagrelha quadrada. Cada célula da grelha pode
conter um número inteiro positivo.
Dada um tabuleiro com uma grelhaN×N, o objetivo do Numbrix é preencher a grelha
com umasequência de números adjacenteshorizontal ou verticalmente. Inicialmente, a
grelha contém alguns números cuja posição não pode ser alterada. Podemos assumir que os
números a ser colocados na grelha variam entre 1 eN×N.
A Figura 1 mostra um exemplo da disposição inicial de um tabuleiro com uma grelha
3 ×3. A Figura 2 mostra uma solução para esse mesmo tabuleiro. Podemos assumir que uma
instância de Numbrix tem umaúnica solução.

## 3 Objetivo

O objetivo deste projeto é o desenvolvimento de um programa em Python 3.8 que, dada uma
instância de Numbrix, retorna uma solução, i.e., uma grelha totalmente preenchida.
O programa deve ser desenvolvido num ficheironumbrix.py, que recebe como argumento
da linha de comandos o caminho para um ficheiro que contém um instância de Numbrix no
formato descrito na secção 4.1. O programa deve resolver o problema utilizando uma técnica
de procura à escolha e imprimir a solução para ostandard outputno formato descrito na secção
4.2.

Utilização:

```
python3 numbrix.py <instance_file>
```

#### 2

#### 6

```
Figura 1: Exemplo de uma instância de Numbrix
```
```
9 4 3
8 5 2
7 6 1
```
```
Figura 2: Exemplo de uma solução para uma instância de Numbrix
```
## 4 Formato de input e output

Nos ficheiros de input e output, cada linha corresponde ao conteúdo de cada uma das linhas da
grelha.

### 4.1 Formato do input

Os ficheiros de input (.txt) representam instâncias do problema Numbrix e seguem o seguinte
formato:

- A primeira linha tem apenas um inteiroNque indica a dimensão da grelhaN×N;
- AsNlinhas seguintes indicam o conteúdo de cada uma dasNlinhas da grelha. Uma
    posição vazia é representada pelo número 0. N.b. uma posição pode ter um número com
    mais que um caracter, por exemplo 10
- Cada linha contém\na indicar o seu fim e as colunas são separadas por\t.

Exemplo

O ficheiro de input que descreve a instância da Figura 1 é o seguinte:

3\n
0\t0\t0\n
0\t0\t2\n
0\t6\t0\n

3
0 0 0
0 0 2
0 6 0


### 4.2 Formato do output

O output do programa deve descrever uma solução para o problema de Numbrix descrito no
ficheiro de input, i.e., uma grelha completamente preenchida em que os números inteiros nela
inseridos estejam colocados sequencialmente de forma adjacente horizontal ou verticalmente.
O output a escrever nostandard outputdeve seguir o seguinte formato:

- cada uma dasNlinhas indica o conteúdo de cada uma dasNlinhas da grelha
- tanto as linhas como as colunas ocorrem ordenadamente, de forma crescente
- todas as linhas, incluindo a última, são terminadas pelo carater newline, i.e.\n

Exemplo

O output que descreve a solução da Figura 2 é:

9\t4\t3\n
8\t5\t2\n
7\t6\t1\n

9 4 3
8 5 2
7 6 1

## 5 Implementação

Nesta secção é descrito o código que poderá ser usado no projeto e o código que deverá ser
implementado no projeto.

### 5.1 Código a utilizar

Para a realização deste projecto devem ser utilizados os ficheiros a ser disponibilizados no site
da unidade curricular com a implementação emPythondos algoritmos de procura^1. O mais
importante é compreender para que servem e como usar as funcionalidades implementadas
nestes ficheiros.
Estes ficheiros não devem ser alterados. Se houver necessidade de alterar definições in-
cluídas nestes ficheiros, estas alterações devem ser feitas no ficheiro de código desenvolvido
que contém a implementação do projeto.

(^1) Este código é adaptado a partir do código disponibilizado com o livroArtificial Intelligence: a Modern
Approache que está disponível emhttps://github.com/aimacode.


5.1.1 Procuras

No ficheirosearch.pyestão implementadas as estruturas necessárias para correr os diferentes
algoritmos de procura. Destacam-se:

- ClasseProblem: Representação abstrata do problema de procura;
- Funçãobreadth_first_tree_search: Procura em largura primeiro;
- Funçãodepth_first_tree_search: Procura em profundidade primeiro;
- Funçãogreedy_search: Procura gananciosa;
- Funçãoastar_search: Procura A*.

5.1.2 ClasseNumbrixState

Esta classe representa os estados utilizados nos algoritmos de procura. O membroboardarma-
zena a configuração do tabuleiro a que o estado corresponde. Abaixo é apresentado o código
desta classe. Podem ser feitas alterações a esta classe, estas devem ser devidamente justifica-
das, por exemplo modificações ao método__lt__(self, other)para suportar funções de
desempate mais complexas.

class NumbrixState:
state_id = 0

```
def __init__(self, board):
self.board = board
self.id = NumbrixState.state_id
NumbrixState.state_id += 1
```
```
def __lt__(self, other):
""" Este método é utilizado em caso de empate na gestão da lista
de abertos nas procuras informadas. """
return self.id < other.id
```
### 5.2 Código a implementar

5.2.1 ClasseBoard

A classeBoardé a representação interna de um tabuleiro de Numbrix. A implementação
desta classe e respectivos métodos é livre. Deve, no entanto, incluir os métodosget_number,
adjacent_vertical_numberseadjacent_horizontal_numbersque recebem dois argu-
mentos, as coordenadas no tabuleiro (linha, coluna), e devem devolver um tuplo com dois
inteiros que correspondem aos valores imediatos na vertical (abaixo, acima) e na horizontal


(esquerda, direita), respectivamente. N.b, caso não exista número adjacente, i.e. na extremi-
dade do tabuleiro, o número a retornar deve serNone. Estes métodos serão utilizados para
fazer testes à restante implementação da classe.

class Board:
""" Representação interna de um tabuleiro de Numbrix. """

```
def get_number(self, row: int, col: int) –> int:
""" Devolve o valor na respetiva posição do tabuleiro. """
# TODO
pass
```
```
def adjacent_vertical_numbers(self, row: int, col: int) -> (int, int):
""" Devolve os valores imediatamente abaixo e acima,
respectivamente. """
# TODO
pass
```
```
def adjacent_horizontal_numbers(self, row: int, col: int) -> (int, int):
""" Devolve os valores imediatamente à esquerda e à direita,
respectivamente. """
# TODO
pass
```
```
# TODO: outros metodos da classe
```
5.2.2 Funçãoparse_instance

A funçãoparse_instanceé responsável por ler o tabuleiro descrito no ficheiro de input e
devolver um objeto do tipoBoardque o represente.

def parse_instance(filename: str):
""" Lê o ficheiro cujo caminho é passado como argumento e retorna
uma instância da classe Board. """
# TODO
pass

5.2.3 ClasseNumbrix

A classeNumbrixherda da classeProblemdefinida no ficheirosearch.pydo código a utilizar
e deve implementar os métodos necessários ao seu funcionamento.


O métodoactionsrecebe como argumento um estado e retorna uma lista de ações que
podem ser executadas a partir desse estado. O métodoresultrecebe como argumento um
estado e uma ação, e retorna o resultado de aplicar essa ação a esse estado. Em ambos os
métodos, uma ação corresponde a preencher um número numa determinada posição. Cada
ação é representada sob a forma de um tuplo com 3 inteiros (indíce da linha, indíce da coluna,
número a preencher na dada posição), por exemplo,(2, 1, 8)representa a ação “preencher
o número 8 na posição linha 2 coluna 1”.
Para suportar as procuras informadas, nomeadamente a procura gananciosa e a procura
A*, deve desenvolver uma heurística que consiga guiar da forma mais eficiente possível estas
procuras. A heurística corresponde à implementação do métodohda classeNumbrix. Esta
função recebe como argumento umnode, a partir do qual se pode aceder ao estado atual em
node.state.
De seguida é disponibilizado um protótipo da classeNumbrixque pode ser usado como
base para a sua implementação.


class Numbrix(Problem):
def __init__(self, board: Board):
""" O construtor especifica o estado inicial. """
# TODO
pass

```
def actions(self, state: NumbrixState):
""" Retorna uma lista de ações que podem ser executadas a
partir do estado passado como argumento. """
# TODO
pass
```
```
def result(self, state: NumbrixState, action):
""" Retorna o estado resultante de executar a 'action' sobre
'state' passado como argumento. A ação a executar deve ser uma
das presentes na lista obtida pela execução de
self.actions(state). """
# TODO
pass
```
```
def goal_test(self, state: NumbrixState):
""" Retorna True se e só se o estado passado como argumento é
um estado objetivo. Deve verificar se todas as posições do tabuleiro
estão preenchidas com uma sequência de números adjacentes. """
# TODO
pass
```
```
def h(self, node: Node):
""" Função heuristica utilizada para a procura A*. """
# TODO
pass
```
5.2.4 Exemplos de utilização

De seguida, são apresentados alguns exemplos da utilização do código a desenvolver, assim
como o respetivo output. Estes exemplos podem ser utilizados para testar a implementação.
Considere que o ficheiroi1.txtse encontra na diretoria a partir da qual o código está a ser
executado e que contém a instância descrita na secção 4.1.


Exemplo 1:

# Ler tabuleiro do ficheiro 'i1.txt' (Figura 1):
board = Board.parse_instance("i1.txt")
print("Initial:\n", board.to_string(), sep="")

# Imprimir valores adjacentes
print(board.adjacent_vertical_numbers(2, 2))
print(board.adjacent_horizontal_numbers(2, 2))

print(board.adjacent_vertical_numbers(1, 1))
print(board.adjacent_horizontal_numbers(1, 1))

Output:

Initial:
0 0 0
0 0 2
0 6 0

(None, 2)
(6, None)
(6, 0)
(0, 2)


Exemplo 2:

# Ler tabuleiro do ficheiro 'i1.txt' (Figura 1):
board = Board.parse_instance("i1.txt")

# Criar uma instância de Numbrix:
problem = Numbrix(board)

# Criar um estado com a configuração inicial:
initial_state = NumbrixState(board)

# Mostrar valor na posição (2, 2):
print(initial_state.board.get_number(2, 2))

# Realizar acção de inserir o número 1 na posição (2, 2)
result_state = problem.result(initial_state, (2, 2, 1))

# Mostrar valor na posição (2, 2):
print(result_state.board.get_number(2, 2))

Output:

0
1


Exemplo 3:

# Ler tabuleiro do ficheiro 'i1.txt' (Figura 1):
board = Board.parse_instance("i1.txt")

# Criar uma instância de Numbrix:
problem = Numbrix(board)

# Criar um estado com a configuração inicial:
s0 = NumbrixState(board)
print("Initial:\n", s0.board.to_string(), sep="")

# Aplicar as ações que resolvem a instância
s1 = problem.result(s0, (2, 2, 1))
s2 = problem.result(s1, (0, 2, 3))
s3 = problem.result(s2, (0, 1, 4))
s4 = problem.result(s3, (1, 1, 5))
s5 = problem.result(s4, (2, 0, 7))
s6 = problem.result(s5, (1, 0, 8))
s7 = problem.result(s6, (0, 0, 9))

# Verificar se foi atingida a solução
print("Is goal?", problem.goal_test(s7))
print("Solution:\n", s7.board.to_string(), sep="")

Output:

Initial:
0 0 0
0 0 2
0 6 0
Is goal? True
Solution:
9 4 3
8 5 2
7 6 1


Exemplo 4:

# Ler tabuleiro do ficheiro 'i1.txt' (Figura 1):
board = Board.parse_instance(input_file)

# Criar uma instância de Numbrix:
problem = Numbrix(board)

# Obter o nó solução usando a procura A*:
goal_node = astar_search(problem)

# Verificar se foi atingida a solução
print("Is goal?", problem.goal_test(goal_node.state))
print("Solution:\n", goal_node.state.board.to_string(), sep="")

Output:

Is goal? True
Solution:
9 4 3
8 5 2
7 6 1

O valor de retorno das funções de procura é um objeto do tipoNode. Do nó de retorno pode
ser retiradas as diversas informaçãoes, por exemplo, estado final (goal_node.state), a acção
que levou ao estado finalgoal_node.action, e o nó precedentegoal_node.parent.

## 6 Avaliação

A nota do projecto será baseada nos seguintes critérios:

- Execução correcta (75% - 15 val.). Estes valores correspondem a testes realizados via
    submissão no Mooshak.
- Relatório (25% - 5 val.).

## 7 Condições de realização e prazos

- O projecto deve ser realizado em grupos de2 alunos
- Inscrições de grupos no Fénix já de encontram abertas, até21 de Março, até às 15:
- Entrega do projeto no Mooshak:26 de Abril, até às 23:


O código do projeto tem de ser entregue obrigatoriamente por via electrónica através do
sistema Mooshak. As inscrições dos grupos para o projeto serão feitas através do Fénix, este
passo é essencial para posterior acesso ao Mooshak.

### 7.1 Mooshak

A avaliação da execução do código do projecto será feita automaticamente através do sistema
Mooshak^2. Após o prazo de inscrição no Fénix e quando notificado pelo corpo docente siga
as seguintes instruções para registar e submeter no Mooskak:

- As credênciais de acesso ao Mooshak poderão ser obtidas no seguinte URL utilizando o
    número de grupo:http://acm.tecnico.ulisboa.pt/~mooshak/cgi-bin/ia2122p3getpass.
    A senha ser-lhe-á enviada para o email que tem configurado no Fenix. A senha pode não
    chegar de imediato, aguarde.
- Após ter recebido a sua senha por email, deve efetuar o login no sistema através da
    página:http://acp.tecnico.ulisboa.pt/~mooshak/. Preencha os campos com a
    informação fornecida no email.
- Deverá ser submetido o ficheironumbrix.pycontendo o código do seu projecto. O fi-
    cheiro de código deve conter em comentário, nas primeiras linhas, o grupo, o número e
    o nome dos alunos.
- Utilize o botão "Browse...", selecione o ficheiro com extensão .py contendo todo o có-
    digo do seu projeto. O seu ficheiro .py deve conter a implementação das funções pedidas
    no enunciado. De seguida clique no botão "Submit"para efetuar a submissão. Aguarde
    para que o sistema processe a sua submissão.
- Quando a submissão tiver sido processada, poderá visualizar na tabela o resultado cor-
    respondente.
Submeta o seu projeto atempadamente, dado que as restrições seguintes podem não lhe
permitir fazê-lo no último momento:
- Até ao prazo de entrega poderá efectuar o número de entregas que desejar, sendo utili-
zada para efeitos de avaliação aúltima entrega efectuada.
- Os testes considerados para efeitos de avaliação podem incluir ou não os exemplos dis-
ponibilizados, além de um conjunto de testes adicionais.
- O tempo de execução de cada teste está limitado (3 segundos), bem como a memória
utilizada (32768 Kb).
- Existe um intrevalo mínimo entre submissões de15 minutos.
- Só são permitidas 10 submissões em simultâneo no sistema, pelo que uma submissão
poderá ser recusada se este limite for excedido. Nesse caso tente mais tarde.

(^2) A versão de Python utilizada nos testes automáticos é Python 3.8.2.


Testes adicionais locais:testes-numbrix.zipcontém testes adicionais que podem ser usados
para a implementação do projeto.

### 7.2 Relatório

Deve produzir um relatório contendo um máximo de duas páginas de texto com fonte 12pt e
espaçamento normal. Para além destas duas páginas, pode acrescentar ao relatório imagens,
figuras e tabelas.
O relatório deve conter os resultados obtidos executando uma procura em largura primeiro,
uma procura em profundidade primeiro, uma procura gananciosa e uma procura A* nos testes
disponibilizados. Os resultados devem conter o tempo de execução, o número de nós ex-
pandidos e o número de nós gerados. Para obter alguns destes valores, pode usar no código
publicado a classeInstrumentedProbleme o exemplo da sua utilização que se encontra no
fim do ficheirosearch.py.
Deve ser feita uma análise crítica dos resultados obtidos, comparando em termos de com-
pletude e eficiência os diferentes métodos testados. Deve também analisar a heurística imple-
mentada e eventualmente compará-la com outras heurísticas avaliadas.

## 8 Cópias

Projectos iguais, ou muito semelhantes, originarão a reprovação na disciplina e, eventualmente,
o levantamento de um processo disciplinar. Os programas entregues serão testados em rela-
ção a soluções existentes na web. As analogias encontradas com os programas da web serão
tratadas como cópias.


