class Rule:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return sum(self) + (len(self.values) - 1)
