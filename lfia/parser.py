from .state import State
from .grammar import Grammar


class Parser:
    G: Grammar

    def __init__(self, G: Grammar):
        self.G = G

    def parse(self, word):

        q: list[list[State]] = [[] for _ in range(len(word) + 1)]
        self.G.productions.append(('S\'', self.G.start))

        initial = State('S\'', self.G.start, 0, 0, 0)
        q[0].append(initial)
        print()
        print(f"Sytuacja początkowa: {initial}")
        i = 0
        scan_output = ""
        while i < len(word):
            j = 0
            while j < len(q[i]):
                state = q[i][j]

                if state.pos != len(state.r):
                    ch, k, type = self.read_character(state.r, state.pos)

                    if type == Grammar.CHAR_TYPE.TERMINAL and ch == word[i]:
                        scan_output = self.scan(state, ch, q, i)
                    elif type == Grammar.CHAR_TYPE.NON_TERMINAL:
                        self.predict(state, ch, q, i)
                else:
                    self.complete(state, q, i)

                j += 1
            i += 1
            print(f"i = {i}")
            print(scan_output)
        for state in q[-1]:
            if state.pos == len(state.r):
                self.complete(state, q, len(word))

        return self.is_finished(q)

    def read_character(self, w, st=0) -> tuple[str, int, Grammar.CHAR_TYPE]:
        end = st + 1
        while end <= len(w):
            if self.G.is_terminal(w[st:end]):
                return w[st:end], end, Grammar.CHAR_TYPE.TERMINAL

            if self.G.is_nonterminal(w[st:end]):
                return w[st:end], end, Grammar.CHAR_TYPE.NON_TERMINAL

            end += 1

    def predict(self, state, ch, q, i):
        for prod in [prod for prod in self.G.productions if prod[0] == ch]:
            new_state = State(prod[0], prod[1], 0, i, i)

            if new_state not in q[i]:
                print(f"Przewidywanie: {new_state}")
                q[i].append(new_state)

    def scan(self, state, ch, q, i):
        new_state = State(state.l, state.r, state.pos + 1, state.h, i + 1)

        if new_state not in q[i + 1]:
            to_print = f"Wczytywanie, {new_state}"
            q[i + 1].append(new_state)
            return to_print

    def complete(self, state, q, i):
        for s in [s for s in q[state.h] if s.pos != len(s.r) and self.read_character(s.r, s.pos)[0] == state.l]:
            new_state = State(s.l, s.r, s.pos + 1, s.h, i)

            if new_state not in q[i]:
                print(f"Uzupełnianie {new_state}")
                q[i].append(new_state)

    def is_finished(self, q):
        return "Należy do gramatyki" if State('S\'', self.G.start, len(self.G.start), 0, len(q) - 1) in q[
            -1] else "Nie należy do gramatyki"
