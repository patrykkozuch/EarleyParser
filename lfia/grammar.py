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
