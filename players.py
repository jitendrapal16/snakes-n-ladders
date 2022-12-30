class Player:
    def __init__(self, name, initial_rank):
        self.name     = name
        self.position = 0
        self.rank     = initial_rank

    def update_position(self, position):
        self.position = position

    def update_rank(self, rank):
        self.rank = rank
