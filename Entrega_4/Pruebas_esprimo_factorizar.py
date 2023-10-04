# import random
# import time

def es_primo(n):
    primo = True
    if n % 2 == 0:
        primo = False
        return primo
    i = 3
    while i <= (n- 1)//i:
        if n % i == 0:
            primo = False
            break
        i += 2
        
    return primo

def factorizar(n):
    fact = []
    mult = []
    i = 2
    while i <= n:
        m = 0
        while n % i == 0:
            n //= i
            m += 1
        if m > 0:
            fact += [i]
            mult += [m]
        i += 1
           
    return [fact,mult]

def factores_y_multiplicidad(N):
    factores = []
    multiplicidad = []
    i = 2
    
    while i * i <= N:
        count = 0
        while N % i == 0:
            N //= i
            count += 1
        if count > 0:
            factores.append(i)
            multiplicidad.append(count)
        i += 1
    
    if N > 1:
        factores.append(N)
        multiplicidad.append(1)
    
    return factores, multiplicidad

# n = random.randint(100000, 99999999)

# inicio_1 = time.time()
# resultado_1 = factorizar(n)
# fin_1 = time.time()
# tiempo_ejecucion = fin_1 - inicio_1
# print(f"Tiempo de ejecución de test: {tiempo_ejecucion/60} minutos \n", n, resultado_1) 


# inicio_2 = time.time()
# resultado_2 = factores_y_multiplicidad(n)
# fin_2 = time.time()
# tiempo_ejecucion = fin_2 - inicio_2
# print(f"Tiempo de ejecución de test: {tiempo_ejecucion/60} minutos \n", n, resultado_2) 

# n = random.randint(1000000000000, 99999999999999999)
# inicio = time.time()
# resultado = es_primo(n)
# fin = time.time()
# tiempo_ejecucion = fin - inicio
# print(f"Tiempo de ejecución de test: {tiempo_ejecucion/60} minutos \n", n, resultado)           
