import random
from collections import defaultdict, Counter

#1. Corpus bilingüe de ejemplo (Español → Inglés)
corpus = [
    ("yo te amo", "i love you"),
    ("te amo", "love you"),
    ("yo te quiero", "i like you"),
    ("ella me ama", "she loves me"),
    ("me gusta el gato", "i like the cat"),
    ("el gato duerme", "the cat sleeps"),
]

#2. Construcción del modelo de traducción
# Conteo de co-ocurrencias palabra a palabra
traducciones = defaultdict(Counter)

for esp, eng in corpus:
    for w_esp in esp.split():
        for w_eng in eng.split():
            traducciones[w_esp][w_eng] += 1

# Normalización de probabilidades P(eng | esp)
modelo_traduccion = {}
for w_esp, conteos in traducciones.items():
    total = sum(conteos.values())
    modelo_traduccion[w_esp] = {w_eng: c / total for w_eng, c in conteos.items()}

#3. Modelo del lenguaje destino (bigramas)
modelo_lenguaje = defaultdict(Counter)
for _, eng in corpus:
    palabras = ["<s>"] + eng.split() + ["</s>"]
    for i in range(len(palabras) - 1):
        modelo_lenguaje[palabras[i]][palabras[i+1]] += 1

# Probabilidad condicional P(next | prev)
modelo_lenguaje_prob = {
    w: {s: c / sum(sigs.values()) for s, c in sigs.items()}
    for w, sigs in modelo_lenguaje.items()
}

#4. Traducción probabilística
def traducir(oracion):
    palabras = oracion.split()
    posibles = []
    for w in palabras:
        if w in modelo_traduccion:
            posibles.append(list(modelo_traduccion[w].keys()))
        else:
            posibles.append([w])
    return posibles

def generar_traduccion(posibles):
    resultado = []
    prev = "<s>"
    for opciones in posibles:
        # ponderar por modelo de lenguaje si existe
        if prev in modelo_lenguaje_prob:
            pesos = [modelo_lenguaje_prob[prev].get(o, 0.1) for o in opciones]
            palabra = random.choices(opciones, weights=pesos)[0]
        else:
            palabra = random.choice(opciones)
        resultado.append(palabra)
        prev = palabra
    return " ".join(resultado)

#5. Prueba del sistema
frases = ["yo te amo", "ella me ama", "me gusta el gato", "el gato duerme"]
print(" Traducción Automática Estadística (SMT) \n")
for f in frases:
    posibles = traducir(f)
    traduccion = generar_traduccion(posibles)
    print(f"{f:<20} → {traduccion}")
