class Sector:
    def __init__(self, prev_sector=None, next_sector=None):
        self.prev_sector = prev_sector
        self.next_sector = next_sector
        self.data = [None] * 500