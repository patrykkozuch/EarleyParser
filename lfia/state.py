class State:
    h: int
    pos: int
    l: str
    r: str
    i: int

    def __init__(self, l, r, pos, h, i):
        self.l = l
        self.r = r
        self.pos = pos
        self.h = h
        self.i = i

    def __str__(self):
        return f"{self.l} -> {self.r[:self.pos]}*{self.r[self.pos:]} [{self.h}, {self.i}]"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.l == other.l and self.r == other.r and self.pos == other.pos and self.h == other.h