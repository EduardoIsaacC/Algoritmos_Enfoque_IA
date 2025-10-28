import random

#1. Gramática lexicalizada manual
# Cada regla tiene estructura: (LHS, RHS, probabilidad, palabra_cabeza)
# LHS = categoría padre
# RHS = lista de categorías hijas o terminales
# probabilidad = peso probabilístico
# palabra_cabeza = head word (palabra principal del constituyente)

gramatica_lex = [
    # Reglas principales
    ("S", ["NP", "VP"], 1.0, "come"),
    
    # Sintagmas nominales (NP)
    ("NP", ["Det", "N"], 0.6, "gato"),
    ("NP", ["Det", "Adj", "N"], 0.4, "pescado"),
    
    # Sintagma verbal (VP)
    ("VP", ["V", "NP"], 0.8, "come"),
    ("VP", ["V", "NP", "PP"], 0.2, "come"),
    
    # Preposición
    ("PP", ["P", "NP"], 1.0, "en"),
    
    # Palabras terminales con su “head”
    ("Det", ["el"], 0.5, "el"),
    ("Det", ["la"], 0.5, "la"),
    ("N", ["gato"], 0.4, "gato"),
    ("N", ["pescado"], 0.4, "pescado"),
    ("N", ["coche"], 0.2, "coche"),
    ("Adj", ["negro"], 0.5, "negro"),
    ("Adj", ["grande"], 0.5, "grande"),
    ("V", ["come"], 0.7, "come"),
    ("V", ["muerde"], 0.3, "muerde"),
    ("P", ["en"], 1.0, "en")
]

#2. Función recursiva para generar oraciones
def generar(simbolo="S"):
    """Genera una oración aleatoria según la gramática."""
    reglas = [r for r in gramatica_lex if r[0] == simbolo]
    if not reglas:
        return [simbolo]
    # selecciona una regla según sus probabilidades
    pesos = [r[2] for r in reglas]
    regla = random.choices(reglas, weights=pesos)[0]
    resultado = []
    for elem in regla[1]:
        resultado += generar(elem)
    return resultado

#3. Generar varias oraciones
print(" Ejemplos de oraciones generadas (L-PCFG) ")
for i in range(5):
    oracion = generar()
    print(" ".join(oracion))
print()

# 4. Evaluar probabilidad condicional léxica 
# Ejemplo: comparar "come pescado" vs "come coche"
def prob_lexicalizada(verbo, objeto):
    """Probabilidad condicional P(objeto | verbo)"""
    if verbo == "come":
        if objeto == "pescado": return 0.9
        elif objeto == "coche": return 0.1
    if verbo == "muerde":
        if objeto == "pescado": return 0.3
        elif objeto == "coche": return 0.7
    return 0.05

pares = [("come", "pescado"), ("come", "coche"), ("muerde", "pescado"), ("muerde", "coche")]
print(" Probabilidades condicionales léxicas ")
for v, o in pares:
    print(f"P({o} | {v}) = {prob_lexicalizada(v, o):.2f}")