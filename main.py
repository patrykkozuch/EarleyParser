from lfia.parser import Parser
from lfia.grammar import Grammar

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
