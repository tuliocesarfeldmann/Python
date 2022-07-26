class No:
    def __init__(self, key, dir, esq):
        self.item = key
        self.dir = dir
        self.esq = esq

    def __repr__(self) -> str:
        return str(self.item)