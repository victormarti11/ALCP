from math import factorial as fac
import time

def factorial(n):
    fact = n
    i = n-1
    while i > 1:
        fact *= i
        i -= 1
    return fact

print(factorial((1477)))
print(fac(1477))

inicio = time.time()
resultado = factorial(1477)
fin = time.time()
iniciomath = time.time()
resultadomat = fac(1477)
finmath = time.time()
tiempo_ejecucion = fin - inicio
tiempo_ejecucionmath = finmath - iniciomath
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos \n")
print(f"Tiempo de ejecución: {tiempo_ejecucionmath} segundos \n")
