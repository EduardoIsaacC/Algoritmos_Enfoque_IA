import spacy

#1. Cargar modelo en español
nlp = spacy.load("es_core_news_sm")

#2. Texto de ejemplo
texto = """
Elon Musk fundó SpaceX en 2002 en California. 
También es CEO de Tesla y compró Twitter en 2022. 
La empresa tiene más de 10,000 empleados.
"""

#3. Procesar texto
doc = nlp(texto)

#4. Mostrar entidades detectadas
print(" Entidades Nombradas Detectadas ")
for ent in doc.ents:
    print(f"{ent.text:<20} → {ent.label_}")

#5. Contar tipos de entidades
from collections import Counter
tipos = Counter([ent.label_ for ent in doc.ents])

print("\n Resumen de Tipos de Entidades ")
for tipo, count in tipos.items():
    print(f"{tipo}: {count}")

#6. Relación probabilística simple (frecuencia relativa)
total = sum(tipos.values())
print("\n Probabilidad estimada de cada tipo ")
for tipo, count in tipos.items():
    prob = count / total
    print(f"P({tipo}) = {prob:.2f}")
