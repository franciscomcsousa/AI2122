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
    def __init__(self, board: list, size: int):
        self.board = board
        self.size = size
        self.positions = [[], ] * ((self.size ** 2) + 1)

        for i in range(self.size):
            for j in range(self.size):
                if self.get_number(i, j) != 0:
                    self.positions[self.get_number(i, j)] = [i, j]
                else:
                    self.positions[self.get_number(i, j)] = [[], ]
        self.positions[0] = []

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
            return self.board[row - 1][col],
        elif row + 1 < self.size and not row - 1 >= 0:
            return self.board[row + 1][col],
        else:
            return self.board[row - 1][col], self.board[row + 1][col]

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """ Devolve os valores imediatamente à esquerda e à direita, 
        respectivamente. """
        if col - 1 >= 0 and not col + 1 < self.size:
            return self.board[row][col - 1],
        elif col + 1 < self.size and not col - 1 >= 0:
            return self.board[row][col + 1],
        else:
            return self.board[row][col - 1], self.board[row][col + 1]

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

    def is_neighbor(self, value1: int, value2: int):
        if  self.positions[value1] == [] or self.positions[value2] == []:
            return False
        return self.positions[value1] in self.get_neighbors(self.positions[value2][0], self.positions[value2][1])

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

        with open(filename) as f:
            lines = f.readlines()
        list_board = []
        for list in range(0, len(lines)):
            list_board += [[], ]
            temp = re.split("\t|\n", lines[list])
            for i in range(len(temp) - 1):
                list_board[list] += [int(temp[i]), ]
        size = list_board[0][0]
        list_board = list_board[1:]

        board = Board(list_board,size)
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

    def get_minimum_value(self):
        for i in range(len(self.positions)):
            if self.positions[i] != []:
                return i

    def get_maximum_value(self):
        for i in range(len(self.positions) - 1, 0, -1):
            if self.positions[i] != []:
                return i

    def next_value(self, number: int):
        for i in range(number, len(self.positions)):
            if self.positions[min(i + 1, len(self.positions) - 1)] != []:
                return i + 1

    # manhatan distance between two positions
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def is_sequence(self, value1, value2):
        if value1 == None or value2 == None:
            return False
        for i in range(value1, value2 + 1):
            if self.positions[i] == []:
                return False
        return True


class TreeNode:
    def __init__(self, value: int, pos):
        """ O construtor especifica o estado inicial. """
        self.value = value
        self.parent = None
        self.sonList = []
        self.pos = pos

    def set_parent(self, parent):
        self.parent = parent

    def add_son(self, value, pos):
        son = TreeNode(value, pos)
        son.set_parent(self)
        self.sonList += [son,]
        return son

    def get_parent(self):
        return self.parent

    def get_son_list(self):
        return self.sonList


class Numbrix(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.initial = NumbrixState(board)

    def get_next_position(self, current: int):
        """ Retorna uma lista de tuplos (row, col) que representam as
        posições vizinhas à posição (row, col) passada como argumento. """
        row, col = board.positions[current]
        # For each entry of position
        while current < len(board.positions):
            # If the position is empty
            if board.positions[current] == []:
                current += 1
                continue
            # If the position is not empty
            else:
                return board.positions[current]

    def actions(self, state: NumbrixState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        board = state.board
        actions = []
        edgeMin, edgeMax = self.get_minimum_sequence_edges(state)
        minimum = board.get_minimum_value()
        maximum = board.get_maximum_value()

        # means that the middle is already done
        if edgeMin is None or edgeMax is None:
            # chooses to start with the maximum number
            # TODO for now it completes the maximum first and then the minimum
            if maximum != board.size ** 2:
                position = board.positions[maximum]
                neighbours = board.get_neighbors_positions(position[0], position[1])
                for pos in neighbours:
                    if board.is_number_in_board(board.get_number(pos[0], pos[1])):
                        continue
                    actions += [[[pos[0], pos[1], maximum + 1],],]
                return actions
            elif minimum != 1:
                position = board.positions[minimum]
                neighbours = board.get_neighbors_positions(position[0], position[1])
                for pos in neighbours:
                    if board.is_number_in_board(board.get_number(pos[0], pos[1])):
                        continue
                    actions += [[[pos[0], pos[1], minimum - 1],],]
                return actions

        return self.get_sequences(state, edgeMin, edgeMax)


    def get_minimum_sequence_edges(self, state: NumbrixState):
        board = state.board
        positions = board.positions
        minSequenceValue = board.size ** 2
        edgeMin = None
        edgeMax = None

        for i in range(board.get_minimum_value(), board.get_maximum_value()):
            if board.positions[i] == []:
                continue

            #TODO - If minSequenceValue == 1 the function can return
            if board.next_value(i) - i < minSequenceValue and board.positions[min(i + 1, board.get_maximum_value())] == []:
                edgeMin = i
                edgeMax = board.next_value(i)
                minSequenceValue = board.next_value(i) - i

        return edgeMin, edgeMax



    def get_sequences(self, state: NumbrixState, edgeMin: int, edgeMax: int):
        sequenceList = []
        board = state.board
        positions = board.positions
        tree = {}
        root = TreeNode(edgeMin, positions[edgeMin])
        tree[str(root.value)] = [root,]
        self.expand_tree_node(state, root, edgeMax, tree)

        if str(edgeMax) not in tree.keys():
            return sequenceList

        for node in tree[str(edgeMax)]:
            sequenceList += [self.get_path_to_root(node, root),]

        return sequenceList

    def get_sequences_edge_max(self, state: NumbrixState, edgeMin: int, edgeMax: int):
        sequenceList = []
        board = state.board
        positions = board.positions
        tree = {}
        root = TreeNode(edgeMin, positions[edgeMin])
        tree[str(root.value)] = [root,]
        self.expand_tree_node_edge_max(state, root, edgeMax, tree)

        if str(edgeMax) not in tree.keys():
            return sequenceList

        for node in tree[str(edgeMax)]:
            sequenceList += [self.get_path_to_root(node, root),]

        return sequenceList

    def get_sequences_edge_min(self, state: NumbrixState, edgeMin: int, edgeMax: int):
        sequenceList = []
        board = state.board
        positions = board.positions
        tree = {}
        root = TreeNode(edgeMin, positions[edgeMin])
        tree[str(root.value)] = [root,]
        self.expand_tree_node_edge_min(state, root, edgeMax, tree)

        if str(edgeMax) not in tree.keys():
            return sequenceList

        for node in tree[str(edgeMax)]:
            sequenceList += [self.get_path_to_root(node, root),]

        return sequenceList

    def get_path_to_root(self, node: TreeNode, root: TreeNode):
        sequence = []
        while node.get_parent().value != root.value:
            sequence += [[node.get_parent().pos[0], node.get_parent().pos[1], node.get_parent().value], ]
            node = node.get_parent()
        return sequence


    def expand_tree_node(self, state: NumbrixState, node: TreeNode, objective: int, tree: dict):

        deep_copy_state = deepcopy(state)
        board = deep_copy_state.board

        board.set_number(node.pos[0], node.pos[1], node.value)
        board.positions[node.value] = [node.pos[0], node.pos[1]]

        if node.value == objective - 1:
            if objective in board.get_neighbors(node.pos[0], node.pos[1]):
                assert node.value + 1 == objective
                son = node.add_son(node.value + 1, board.positions[objective])
                if str(son.value) in tree.keys():
                    tree[str(son.value)] += [son, ]
                else:
                    tree[str(son.value)] = [son, ]
            return

        if board.manhattan_distance(board.positions[objective], node.pos) > abs(node.value - objective):
            return

        neighborsPos = board.get_neighbors_positions(node.pos[0], node.pos[1])

        for neighborPos in neighborsPos:
            if board.get_number(neighborPos[0], neighborPos[1]) != 0:
                continue
            son = node.add_son(node.value + 1, neighborPos)
            if str(son.value) in tree.keys():
                tree[str(son.value)] += [son,]
            else:
                tree[str(son.value)] = [son,]
            self.expand_tree_node(deep_copy_state, son, objective, tree)


    def expand_tree_node_edge_max(self, state: NumbrixState, node: TreeNode, objective: int, tree: dict):

        deep_copy_state = deepcopy(state)
        board = deep_copy_state.board

        board.set_number(node.pos[0], node.pos[1], node.value)
        board.positions[node.value] = [node.pos[0], node.pos[1]]

        if node.value == objective - 1:
            son = node.add_son(node.value + 1, board.positions[objective])
            if str(son.value) in tree.keys():
                tree[str(son.value)] += [son, ]
            else:
                tree[str(son.value)] = [son, ]
            return

        neighborsPos = board.get_neighbors_positions(node.pos[0], node.pos[1])

        for neighborPos in neighborsPos:
            if board.get_number(neighborPos[0], neighborPos[1]) != 0:
                continue
            son = node.add_son(node.value + 1, neighborPos)
            if str(son.value) in tree.keys():
                tree[str(son.value)] += [son,]
            else:
                tree[str(son.value)] = [son,]
            self.expand_tree_node_edge_max(deep_copy_state, son, objective, tree)

    def expand_tree_node_edge_min(self, state: NumbrixState, node: TreeNode, objective: int, tree: dict):

        deep_copy_state = deepcopy(state)
        board = deep_copy_state.board

        board.set_number(node.pos[0], node.pos[1], node.value)
        board.positions[node.value] = [node.pos[0], node.pos[1]]

        if node.value == objective + 1:
            son = node.add_son(node.value - 1, board.positions[objective])
            if str(son.value) in tree.keys():
                tree[str(son.value)] += [son, ]
            else:
                tree[str(son.value)] = [son, ]
            return

        neighborsPos = board.get_neighbors_positions(node.pos[0], node.pos[1])

        for neighborPos in neighborsPos:
            if board.get_number(neighborPos[0], neighborPos[1]) != 0:
                continue
            son = node.add_son(node.value - 1, neighborPos)
            if str(son.value) in tree.keys():
                tree[str(son.value)] += [son,]
            else:
                tree[str(son.value)] = [son,]
            self.expand_tree_node_edge_min(deep_copy_state, son, objective, tree)

    def result(self, state: NumbrixState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de 
        self.actions(state). """
        deep_copy_state = deepcopy(state)
        for placement in action:
            deep_copy_state.board.set_number(placement[0], placement[1], placement[2])
            deep_copy_state.board.positions[placement[2]] = [placement[0], placement[1]]

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

    # TODO: outros metodos da classe coco


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro de input de sys.argv[1],
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    board = Board.parse_instance(sys.argv[1])
    problem = Numbrix(board)
    #print(problem.get_sequences(problem.initial, problem.get_minimum_sequence_edges(problem.initial)[0], problem.get_minimum_sequence_edges(problem.initial)[1]))
    #problem.get_sequences(problem.initial, 11, 15)
    result = depth_first_tree_search(problem)
    result.state.board.print_board()
