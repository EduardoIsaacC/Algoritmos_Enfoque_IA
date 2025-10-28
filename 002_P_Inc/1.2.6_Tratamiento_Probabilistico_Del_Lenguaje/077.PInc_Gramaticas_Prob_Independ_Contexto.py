import nltk
from nltk import PCFG
from nltk.parse.generate import generate
from nltk.parse.viterbi import ViterbiParser

# Definición de la gramática probabilística
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | Det Adj N [0.4]
VP -> V NP [0.7] | V NP PP [0.3]
PP -> P NP [1.0]
Det -> 'el' [0.5] | 'la' [0.5]
N -> 'perro' [0.5] | 'gato' [0.5]
Adj -> 'grande' [0.5] | 'pequeño' [0.5]
V -> 'persigue' [0.5] | 'observa' [0.5]
P -> 'en' [1.0]
""")

# Mostrar todas las reglas
print("=== Reglas de la Gramática ===")
for prod in grammar.productions():
    print(prod)
print()

# Generar algunas oraciones posibles
print(" Ejemplos de oraciones generadas por la PCFG ")
for sentence in generate(grammar, n=5):
    print(' '.join(sentence))
print()

# Analizador probabilístico (Viterbi)
parser = ViterbiParser(grammar)

# Oración a analizar
sentence = ['el', 'gato', 'observa', 'el', 'perro']

print(f"Análisis probabilístico de la oración: {' '.join(sentence)} ")
for tree in parser.parse(sentence):
    print(tree)
    print(f"Probabilidad total: {tree.prob():.6f}")
    tree.pretty_print()
