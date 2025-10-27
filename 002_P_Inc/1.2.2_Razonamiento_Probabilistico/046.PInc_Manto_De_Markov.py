# Representamos la red como un diccionario
# Cada variable tiene una lista de padres (nodos de los que depende)

red_bayesiana = {
    "Rain": [],                    # Lluvia no tiene padres
    "Sprinkler": ["Rain"],         # El aspersor depende de la lluvia
    "WetGrass": ["Rain", "Sprinkler"]  # Césped mojado depende de ambos
}

# Función para obtener los hijos de una variable
def hijos(variable):
    return [v for v, padres in red_bayesiana.items() if variable in padres]

# Función para calcular el Manto de Markov de una variable
def manto_de_markov(variable):
    padres = set(red_bayesiana[variable])
    hijos_var = set(hijos(variable))
    co_padres = set()
    
    # Buscar los padres de los hijos
    for h in hijos_var:
        co_padres.update(red_bayesiana[h])
    
    # Unir padres, hijos y co-padres
    manto = padres.union(hijos_var).union(co_padres)
    
    # No debe incluir la variable original
    if variable in manto:
        manto.remove(variable)
    return manto

# Mostrar el Manto de Markov de cada variable
print(" Manto de Markov en la Red Bayesiana del Jardín \n")
for nodo in red_bayesiana:
    print(f"MB({nodo}) = {manto_de_markov(nodo)}")