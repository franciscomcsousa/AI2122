# numbrix.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 56:
# 95579 Francisco Sousa
# 95674 Sara Aguincha

from ast import arg
from copy import deepcopy
import sys

from search import Problem, Node, astar_search, breadth_first_tree_search, depth_first_graph_search, \
    depth_first_tree_search, greedy_search, recursive_best_first_search
import re


class NumbrixState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = NumbrixState.state_id
        NumbrixState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """ Representação interna de um tabuleiro de Numbrix. """

    def __init__(self):
        self.board = []
        self.size = 0
        pass

    def get_number(self, row: int, col: int):
        """ Devolve o valor na respetiva posição do tabuleiro. """
        return self.board[row][col]

    def set_number(self, row: int, col: int, value: int):
        """ Altera o valor na respetiva posição do tabuleiro. """
        self.board[row][col] = value

    def is_number_in_board(self, value: int):
        """ Verifica se um dado valor existe no tabuleiro. """
        if value == 0:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == value:
                    return True
        return False

    def get_pred_succ(self, value: int):
        """ Retorna o predecessor e o sucessor de um dado valor. """
        if value == 1:
            return [value + 1, ]
        elif value == self.size ** 2:
            return [value - 1, ]
        else:
            return [value + 1, value - 1]

    def adjacent_vertical_numbers(self, row: int, col: int):
        """ Devolve os valores imediatamente abaixo e acima, 
        respectivamente. """
        if row - 1 >= 0 and not row + 1 < self.size:
            return (self.board[row - 1][col],)
        elif row + 1 < self.size and not row - 1 >= 0:
            return (self.board[row + 1][col],)
        else:
            return (self.board[row - 1][col], self.board[row + 1][col])

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """ Devolve os valores imediatamente à esquerda e à direita, 
        respectivamente. """
        if col - 1 >= 0 and not col + 1 < self.size:
            return (self.board[row][col - 1],)
        elif col + 1 < self.size and not col - 1 >= 0:
            return (self.board[row][col + 1],)
        else:
            return (self.board[row][col - 1], self.board[row][col + 1])

    def adjacent_vertical_positions(self, row: int, col: int):
        """ Devolve as posições imediatamente abaixo e acima,
        respectivamente. """
        if row - 1 >= 0 and not row + 1 < self.size:
            return (row - 1, col),
        elif row + 1 < self.size and not row - 1 >= 0:
            return (row + 1, col),
        else:
            return ((row - 1, col), (row + 1, col))

    def adjacent_horizontal_positions(self, row: int, col: int):
        """ Devolve as posições imediatamente à esquerda e à direita,
        respectivamente. """
        if col - 1 >= 0 and not col + 1 < self.size:
            return (row, col - 1),
        elif col + 1 < self.size and not col - 1 >= 0:
            return (row, col + 1),
        else:
            return ((row, col - 1), (row, col + 1))

    def get_neighbors(self, row: int, col: int):
        return self.adjacent_vertical_numbers(row, col) + self.adjacent_horizontal_numbers(row, col)

    def get_neighbors_positions(self, row: int, col: int):
        return self.adjacent_vertical_positions(row, col) + self.adjacent_horizontal_positions(row, col)

    def get_empty_positions(self):
        """ Retorna a lista de posições vazias"""
        empty_positions = []
        for i in range(board.size):
            for j in range(board.size):
                if board.get_number(i, j) == 0:
                    empty_positions += [(i, j)]
        return empty_positions

    @staticmethod
    def parse_instance(filename: str):
        """ Lê o ficheiro cujo caminho é passado como argumento e retorna
        uma instância da classe Board. """
        board = Board()

        with open(filename) as f:
            lines = f.readlines()

        for list in range(0, len(lines)):
            board.board += [[], ]
            temp = re.split("\t|\n", lines[list])
            for i in range(len(temp) - 1):
                board.board[list] += [int(temp[i]), ]
        board.size = board.board[0][0]
        board.board = board.board[1:]

        return board

    def print_board(self):
        """ Imprime o tabuleiro no ecrã. """
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end="\t")
            print()

    def get_empty_positions(self):
        """ Retorna uma lista de tuplos (row, col) que representam as
        posições vazias do tabuleiro. """
        empty_positions = []
        for i in range(board.size):
            for j in range(board.size):
                if board.get_number(i, j) == 0:
                    empty_positions += [(i, j)]
        return empty_positions

    # manhatan distance between two positions
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])



class Numbrix(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.initial = NumbrixState(board)
        self.position = [[], ] * ((board.size**2) + 1)

        for i in range(board.size):
            for j in range(board.size):
                if board.get_number(i, j) != 0:
                    self.position[board.get_number(i, j)] = [i, j]
                else:
                    self.position[board.get_number(i, j)] = [[], ]
        self.position[0] = []

    def get_next_position(self, current: int):
        """ Retorna uma lista de tuplos (row, col) que representam as
        posições vizinhas à posição (row, col) passada como argumento. """
        row, col = self.position[current]
        # For each entry of position
        while (current < len(self.position)):
            # If the position is empty
            if self.position[current] == []:
                current += 1
                continue
            # If the position is not empty
            else:
                return self.position[current]

    def actions(self, state: NumbrixState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        board = state.board
        actions = []
        # For each entry of self.position
        for i in range(len(self.position)):
            # If the position is empty
            if self.position[i] == []:
                continue
            # If the position is not empty
            else:
                temp_pred_succ = board.get_pred_succ(i)
                pred_succ = []
                for j in range(len(temp_pred_succ)):
                    if not board.is_number_in_board(temp_pred_succ[j]):
                        pred_succ += [temp_pred_succ[j],]
                # Already has pred and succ on board
                if(len(pred_succ) == 0):
                    continue
                neigh_pos = board.get_neighbors_positions(self.position[i][0], self.position[i][1])
                for pos in neigh_pos:
                    if board.is_number_in_board(board.get_number(pos[0], pos[1])):
                        continue

                    for k in range(len(pred_succ)):
                        actions += ((pos[0], pos[1], pred_succ[k]),)
        return actions

    def result(self, state: NumbrixState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de 
        self.actions(state). """
        deep_copy_state = deepcopy(state)
        deep_copy_state.board.set_number(action[0], action[1], action[2])
        self.position[action[2]] = [action[0], action[1]]
        return deep_copy_state

    def goal_test(self, state: NumbrixState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro 
        estão preenchidas com uma sequência de números adjacentes. """
        board = state.board
        # TODO - Alterar one liner
        for i in range(board.size):
            for j in range(board.size):
                if board.get_number(i, j) == 0:
                    return False
                neighbors = board.get_neighbors(i, j)
                pred_succ = board.get_pred_succ(board.get_number(i, j))
                for num in range(len(pred_succ)):
                    if pred_succ[num] not in neighbors:
                        return False
                continue
        return True

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de input de sys.argv[1],
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    board = Board.parse_instance(sys.argv[1])
    problem = Numbrix(board)
    result = depth_first_graph_search(problem)
    result.state.board.print_board()
