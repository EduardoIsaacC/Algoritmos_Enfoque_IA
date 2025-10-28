import re
from collections import Counter, defaultdict

# 1. Definimos un corpus de ejemplo 
corpus_texto = """
hola mundo este es un mundo pequeño
hola mundo este es un ejemplo de modelo probabilistico
hola amigo este es un sistema inteligente
este sistema aprende del mundo
"""

#2. Preproceso básico del corpus 
# - minúsculas
# - quitar símbolos raros
# - tokenizar por espacios
def limpiar_y_tokenizar(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúñü\s]", "", texto)  # dejamos letras y espacios
    tokens = texto.split()
    return tokens

tokens = limpiar_y_tokenizar(corpus_texto)

print("Tokens del corpus:")
print(tokens)
print()

# 3. Construimos unigramas y bigramas
# Unigrama: una sola palabra
unigramas = Counter(tokens)

# Bigramas: pares consecutivos (w_i, w_{i+1})
bigramas = Counter()
for i in range(len(tokens) - 1):
    par = (tokens[i], tokens[i+1])
    bigramas[par] += 1

print("Frecuencias de unigramas:")
for palabra, cnt in unigramas.items():
    print(f"{palabra}: {cnt}")
print()

print("Frecuencias de bigramas:")
for par, cnt in bigramas.items():
    print(f"{par}: {cnt}")
print()

#4. Probabilidades
# P(w2 | w1) ≈ conteo(w1,w2) / conteo(w1)

def prob_condicional(w1, w2):
    num = bigramas[(w1, w2)]
    den = unigramas[w1]
    if den == 0:
        return 0.0
    return num / den

ejemplo_w1 = "hola"
print(f"Probabilidades de la palabra siguiente dado '{ejemplo_w1}':")
siguientes_posibles = [b for (a,b) in bigramas.keys() if a == ejemplo_w1]
for w2 in set(siguientes_posibles):
    print(f"P({w2} | {ejemplo_w1}) = {prob_condicional(ejemplo_w1, w2):.3f}")
print()

#5. Predicción simple de la siguiente palabra
def palabra_mas_probable_despues_de(w1):
    candidatos = []
    for (a,b), cnt in bigramas.items():
        if a == w1:
            p = prob_condicional(w1, b)
            candidatos.append((b, p))
    if not candidatos:
        return None
    # elegimos la palabra con prob más alta
    candidatos.sort(key=lambda x: x[1], reverse=True)
    return candidatos[0]

siguiente = palabra_mas_probable_despues_de("hola")
print("Dado 'hola', la palabra más probable que sigue es:", siguiente)
print()

#6. Probabilidad aproximada de una oración
# Usamos modelo de bigramas:
# P(w1,w2,...,wn) ~ P(w1) * Π P(wi | wi-1)

def prob_oracion_bigramas(oracion_tokens):
    if len(oracion_tokens) == 0:
        return 0.0
    # P(w1) ~ frecuencia de w1 / total de palabras
    total_palabras = sum(unigramas.values())
    p_total = unigramas[oracion_tokens[0]] / total_palabras

    # multiplicamos las condicionales
    for i in range(1, len(oracion_tokens)):
        w_prev = oracion_tokens[i-1]
        w_curr = oracion_tokens[i]
        p_total *= prob_condicional(w_prev, w_curr)
    return p_total

oracion1 = "hola mundo este es un mundo pequeño".split()
oracion2 = "mundo hola es este un pequeño mundo".split()

p1 = prob_oracion_bigramas(oracion1)
p2 = prob_oracion_bigramas(oracion2)

print("Prob(oración 1) =", p1)
print("Prob(oración 2) =", p2)
print("La red considera más probable la oración 1 que la 2 (debería).")