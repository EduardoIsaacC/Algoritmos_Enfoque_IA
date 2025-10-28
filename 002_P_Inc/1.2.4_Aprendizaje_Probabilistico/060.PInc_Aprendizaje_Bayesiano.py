# Probabilidades a priori
P_spam = 0.2
P_no_spam = 0.8

# Verosimilitud: probabilidad de observar "dinero" dado el tipo de correo
P_dinero_given_spam = 0.9
P_dinero_given_no_spam = 0.1

# Aplicación del Teorema de Bayes
numerador = P_dinero_given_spam * P_spam
denominador = (P_dinero_given_spam * P_spam) + (P_dinero_given_no_spam * P_no_spam)
P_spam_given_dinero = numerador / denominador

print(" Aprendizaje Bayesiano ")
print(f"P(Spam | 'dinero') = {P_spam_given_dinero:.3f}")
