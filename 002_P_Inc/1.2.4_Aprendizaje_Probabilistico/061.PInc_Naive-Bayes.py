# Probabilidades a priori
P_spam = 0.4
P_no_spam = 0.6

# Probabilidades condicionales
P_palabra_dado_spam = {
    "oferta": 0.8,
    "gratis": 0.7,
    "dinero": 0.9
}

P_palabra_dado_no_spam = {
    "oferta": 0.1,
    "gratis": 0.2,
    "dinero": 0.1
}

# Correo recibido
correo = ["oferta", "dinero"]

# Calcular probabilidades
P_spam_total = P_spam
P_no_spam_total = P_no_spam

for palabra in correo:
    P_spam_total *= P_palabra_dado_spam[palabra]
    P_no_spam_total *= P_palabra_dado_no_spam[palabra]

# Normalización
P_spam_posterior = P_spam_total / (P_spam_total + P_no_spam_total)
P_no_spam_posterior = P_no_spam_total / (P_spam_total + P_no_spam_total)

print(" Clasificador Naïve Bayes ")
print(f"P(Spam | correo) = {P_spam_posterior:.3f}")
print(f"P(No Spam | correo) = {P_no_spam_posterior:.3f}")
print(f"Resultado: {'SPAM' if P_spam_posterior > P_no_spam_posterior else 'NO SPAM'}")