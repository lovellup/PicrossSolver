from square import Square
from rule import Rule

class Board:

    def __init__(self, dimensions, horizontal_rules, vertical_rules):
        self.dimensions = dimensions
        self.board = []
        self.validate_rules(horizontal_rules)
        self.horizontal_rules = horizontal_rules
        self.validate_rules(vertical_rules)
        self.vertical_rules = vertical_rules
        for i in range(dimensions):
            self.board.append([])
            for j in range(dimensions):
                self.board[i].append(Square(i, j, ''))

    def validate_rules(self, rules):
        if len(rules) != self.dimensions:
            raise AttributeError('Rules not right length')
        for rule in rules:
            if len(rule) > self.dimensions:
                raise AttributeError('Rules total too long')

    def __str__(self):
        board_state = []
        for i in range(self.dimensions):
            board_state.append([])
            for j in range(self.dimensions):
                board_state[i].append(self.board[i][j].state)
        return str(board_state)