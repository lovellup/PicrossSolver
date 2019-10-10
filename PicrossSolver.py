# define board
# look for "easy" selections


def calculate_rule_length(rule):
    return sum(rule) + (len(rule) - 1)






vertical_rules = [[0], [1, 1], [0]]
horizontal_rules = [[1], [0], [1]]
board = Board(3, horizontal_rules, vertical_rules)
print(str(board))
