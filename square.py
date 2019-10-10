class Square:

    def __init__(self, row, column, state):
        self.row = row
        self.column = column
        self.state = state

    def __str__(self):
        return self.state

