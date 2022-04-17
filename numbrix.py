# numbrix.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 56:
# 95579 Francisco Sousa
# 95674 Sara Aguincha

from ast import arg
from copy import deepcopy
import sys
from search import Problem, Node, astar_search, breadth_first_tree_search, depth_first_graph_search, depth_first_tree_search, greedy_search, recursive_best_first_search
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
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == value:
                    return True
        return False

    def get_pred_succ(self, value: int):
        """ Retorna o predecessor e o sucessor de um dado valor. """
        if value == 1:
            return value + 1,
        elif value == self.size**2:
            return value - 1,
        else:
            return value + 1, value - 1



    def adjacent_vertical_numbers(self, row: int, col: int):
        """ Devolve os valores imediatamente abaixo e acima, 
        respectivamente. """
        #TODO - improve this return with get_number
        return (self.board[row + 1][col] if row + 1 < self.size else None, self.board[row - 1][col] if (row - 1 >= 0) else None)
    
    def adjacent_horizontal_numbers(self, row: int, col: int):
        """ Devolve os valores imediatamente à esquerda e à direita, 
        respectivamente. """
        #TODO - improve this return with get_number
        return (self.board[row][col - 1] if col - 1 >= 0 else None, self.board[row][col + 1] if (col + 1 < self.size) else None)

    def manhattan_distance(self, state: NumbrixState, row: int, col: int, value: int):
        """ Retorna a distância entre o número passado como argumento e
        o número na posição (row, col) do tabuleiro. """
        return abs(state.board.get_number(row, col) - value)
        
    
    @staticmethod    
    def parse_instance(filename: str):
        """ Lê o ficheiro cujo caminho é passado como argumento e retorna
        uma instância da classe Board. """
        board = Board()

        with open(filename) as f:
            lines = f.readlines()
        
        for list in range(0, len(lines)):
            board.board += [[],]
            temp = re.split("\t|\n", lines[list])
            for i in range(len(temp) - 1):
                board.board[list] += [int(temp[i]),]
        board.size = board.board[0][0]
        board.board = board.board[1:]
        #pain

        return board

    def print_board(self):
        """ Imprime o tabuleiro no ecrã. """
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end="\t")
            print()

    def get_empty_positions(self, state: NumbrixState):
        """ Retorna uma lista de tuplos (row, col) que representam as
        posições vazias do tabuleiro. """
        board = state.board
        empty_positions = []
        for i in range(board.size):
            for j in range(board.size):
                if board.get_number(i, j) == 0:
                    empty_positions += [(i, j)]
        return empty_positions

class Numbrix(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.initial = NumbrixState(board)

    def actions(self, state: NumbrixState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        board = state.board
        empty_positions = board.get_empty_positions(state)
        actions = []
        for position in empty_positions:
            row, col = position
            vertical = board.adjacent_vertical_numbers(row, col)
            horizontal = board.adjacent_horizontal_numbers(row, col)
            if vertical[0] is not None and vertical[0] - 1 >= 0 and not board.is_number_in_board(vertical[0] - 1):
                actions += [(row, col, vertical[0] - 1)]
            if vertical[0] is not None and vertical[0] + 1 <= board.size ** 2 and not board.is_number_in_board(vertical[0] + 1):
                actions += [(row, col, vertical[0] + 1)]
            if vertical[1] is not None and vertical[1] - 1 >= 0 and not board.is_number_in_board(vertical[1] - 1):
                actions += [(row, col, vertical[1] - 1)]
            if vertical[1] is not None and vertical[1] + 1 <= board.size ** 2 and not board.is_number_in_board(vertical[1] + 1):
                actions += [(row, col, vertical[1] + 1)]
            if horizontal[0] is not None and horizontal[0] - 1 >= 0 and not board.is_number_in_board(horizontal[0] - 1):
                actions += [(row, col, horizontal[0] - 1)]
            if horizontal[0] is not None and horizontal[0] + 1 <= board.size ** 2 and not board.is_number_in_board(horizontal[0] + 1):
                actions += [(row, col, horizontal[0] + 1)]
            if horizontal[1] is not None and horizontal[1] - 1 >= 0 and not board.is_number_in_board(horizontal[1] - 1):
                actions += [(row, col, horizontal[1] - 1)]
            if horizontal[1] is not None and horizontal[1] + 1 <= board.size ** 2 and not board.is_number_in_board(horizontal[1] + 1):
                actions += [(row, col, horizontal[1] + 1)]
        return actions

    def result(self, state: NumbrixState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de 
        self.actions(state). """
        deep_copy_state = deepcopy(state)
        deep_copy_state.board.set_number(action[0], action[1], action[2])
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
                vertical_neighbors = board.adjacent_vertical_numbers(i, j)
                horizontal_neighbors = board.adjacent_horizontal_numbers(i, j)
                predecessor = False
                successor = False
                if board.get_number(i, j) - 1 in vertical_neighbors or board.get_number(i, j) - 1 in horizontal_neighbors:
                    predecessor = True
                if board.get_number(i, j) + 1 in vertical_neighbors or board.get_number(i, j) + 1 in horizontal_neighbors:
                    successor = True
                if not (predecessor and successor):
                    return False
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