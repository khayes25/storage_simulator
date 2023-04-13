class File:
    def __init__(self, name, size, hidden, read_only):
        self.name = name
        self.size = size
        self.hidden = hidden
        self.read_only = read_only