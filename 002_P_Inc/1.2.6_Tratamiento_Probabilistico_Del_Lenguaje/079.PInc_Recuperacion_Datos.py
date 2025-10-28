from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#1. Corpus de documentos simulados
documentos = [
    "La inteligencia artificial permite a las máquinas aprender de datos.",
    "El aprendizaje automático es una rama de la inteligencia artificial.",
    "Los modelos probabilísticos ayudan a predecir comportamientos futuros.",
    "El procesamiento del lenguaje natural analiza el texto humano.",
    "Las redes neuronales simulan el cerebro humano en sistemas de IA."
]

#2. Consulta del usuario
consulta = ["modelos de lenguaje en inteligencia artificial"]

#3. Calcular matriz TF-IDF
vectorizador = TfidfVectorizer()
tfidf = vectorizador.fit_transform(documentos + consulta)

#4. Calcular similitud coseno entre la consulta y cada documento
similaridades = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()

#5. Mostrar resultados ordenados
indices_ordenados = np.argsort(similaridades)[::-1]

print(" Resultados de Recuperación Probabilística \n")
for i in indices_ordenados:
    print(f"Documento {i+1}:")
    print(f" {documentos[i]}")
    print(f" Similitud con la consulta: {similaridades[i]:.3f}\n")