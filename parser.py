from collections import deque
from enum import Enum


class Grammar():
    terminals: list[str] = []
    nonterminals: list[str] = []
    productions: list[tuple] = []
    start: str

    def __init__(self, terminals, nonterminals, productions, start):
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.productions = productions
        self.start = start

    def is_terminal(self, ch):
        return ch in self.terminals

    def is_nonterminal(self, ch):
        return ch in self.nonterminals

    class CHAR_TYPE(Enum):
        TERMINAL = 1,
        NON_TERMINAL = 2


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

class Parser:
    G: Grammar

    def __init__(self, G: Grammar):
        self.G = G

    def parse(self, word):

        q:list[list[State]] = [[] for _ in range(len(word)+1)]
        G.productions.append(('S\'', G.start))

        q[0].append(State('S\'', G.start, 0, 0, 0))
        i = 0
        while i < len(word):
            j = 0
            while j < len(q[i]):
                state = q[i][j]

                if state.pos != len(state.r):
                    ch, k, type = self.read_character(state.r, state.pos)

                    if type == G.CHAR_TYPE.TERMINAL and ch == word[i]:
                        self.scan(state, ch, q, i)
                    elif type == G.CHAR_TYPE.NON_TERMINAL:
                        self.predict(state, ch, q, i)
                else:
                    self.complete(state, q, i)

                j += 1
            i += 1
            print(f"i = {i}")
        for state in q[-1]:
            if state.pos == len(state.r):
                self.complete(state, q, len(word))

        return self.is_finished(q)

    def read_character(self, w, st = 0) -> tuple[str, int, Grammar.CHAR_TYPE]:
        end = st + 1
        while end <= len(w):
            if G.is_terminal(w[st:end]):
                return w[st:end], end, G.CHAR_TYPE.TERMINAL

            if G.is_nonterminal(w[st:end]):
                return w[st:end], end, G.CHAR_TYPE.NON_TERMINAL

            end += 1

    def predict(self, state, ch, q, i):
        for prod in [prod for prod in self.G.productions if prod[0] == ch]:
            new_state = State(prod[0], prod[1], 0, i, i)

            if new_state not in q[i]:
                print(f"Przewidywanie: {new_state}")
                q[i].append(new_state)

    def scan(self, state, ch, q, i):
        new_state = State(state.l, state.r, state.pos + 1, state.h, i + 1)

        if new_state not in q[i+1]:
            print(f"Wczytywanie, {new_state}")
            q[i+1].append(new_state)

    def complete(self, state, q, i):
        for s in [s for s in q[state.h] if s.pos != len(s.r) and self.read_character(s.r, s.pos)[0] == state.l]:
            new_state = State(s.l, s.r, s.pos + 1, s.h, i)

            if new_state not in q[i]:
                print(f"Uzupełnianie {new_state}")
                q[i].append(new_state)

    def is_finished(self, q):
        return "Należy do gramatyki" if State('S\'', self.G.start, len(self.G.start), 0, len(q)-1) in q[-1] else "Nie należy do gramatyki"


if __name__ == '__main__':
    alph_line = input("Podaj alfabet, rodzielony przecinkami (np. a, b, c): ")
    nonterminal_line = input("Podaj symbole nieterminalne, rodzielone przecinkami (np. A, B, C): ")
    prods_line = input("Podaj listę produkcji w postacji: A -> b. Produkcje oddziel przecinkami: ")
    start = input("Podaj symbol startowy: ")

    terminals = [line.strip() for line in alph_line.strip().split(',')]
    nontterminals = [line.strip() for line in nonterminal_line.strip().split(',')]
    prods_line = [(a.strip(), b.strip()) for a, b in [line.strip().split('->') for line in prods_line.split(',')]]

    G = Grammar(terminals, nontterminals, prods_line, start)

    parser = Parser(G)

    print(parser.parse(input("Podaj słowo: ")))
