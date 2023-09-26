#       Arrate Esteve, Claudia;
#       González Montero, Sergio; 
#       Martín Martín, Víctor;
#       Miori Gutiérrez, Alberto;
#       Olmedo Moreno, Juan Cristóbal;

# Problema 3.7. Reimplementar el algoritmo gcd binario(x,y) del programa gcds.py
# del tema #2 para x, y ≥ 0 representados por listas de d´ıgitos (reducidas) y
# demostrar que su complejidad es O(n2), donde n = len(x)+len(y).
# Parte del ejercicio consiste en implementar la función mul2(x) que calcule
# el doble de un entero x ≥ 0.
# También se deben implementar las funciónes auxiliares mul2(x) y div2(x) que
# calculen el doble y la mitad de x, con la representación de listas de dígitos.
# Se espera que las funciones puedan manejar valores de len(x+y) hasta 10000.
import random
import time
import math
#from operaciones import remover_ceros

num_aleat = [random.randint(0, 9) for _ in range(10000)]


def mul2(x):
    c = 0                             # Acarreo
    doble_x = []                      # Lista vacía para almacenar el resultado
    
    for digito in x:
        doble = digito * 2 + c        # Multiplicamos el dígito por 2 y sumamos el acarreo
        doble_x.append(doble % 10)    # Agregamos al final de la lista la cifra de las unidades
        c = doble // 10               # Actualizamos el acarreo para el siguiente dígito
        
    if c > 0:                         # Si aún hay un acarreo pendiente
        doble_x.append(c)             # Agregamos al final de la lista la cifra correspondiente

    return doble_x


# Complejidad en tiempo
inicio = time.time()
resultado = mul2(num_aleat)
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución de mul2: {tiempo_ejecucion} segundos \n")


def div2(x):
    c = 0                                              # Acarreo
    mitad_x = []
    
    for digito in x:
        mitad = math.floor(digito *(1/2) + c)          # La mitad más el acarreo
        print (f"La mitad de {digito} es {mitad}")
        mitad_x.append(mitad % 10)                     # Añadimos la cifra en el lugar correspondiente
        print(f"He añadido {mitad%10}")
        c = mitad // 10
        print(f"Mi acarreo es {c}\n")                 

    if c > 0:
        print("Aún me queda un acarreo")
        mitad_x.append(c)
        print(f"He añadido {c}")
        

    return mitad_x


# Complejidad en tiempo
inicio = time.time()
resultado = div2(num_aleat)
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución de div2: {tiempo_ejecucion} segundos \n")

def lst2num(l):
    exp = 0
    result = 0
    for i in l:
        result += i*10**exp
        exp += 1
    return result

def remover_ceros(a):
    # a = lista de dí­gitos decimales
    n = len(a)
    while n >= 1 and a[n - 1] == 0:
        n -= 1
    del a[n:]
    return a

def proof():
    limit = 10*6
    equal = True
    count = 0
    while equal:
        num_aleat = [random.randint(0, 9) for _ in range(10)]
        num_aleat = remover_ceros(num_aleat)
        count += 1
        if (2*lst2num(num_aleat)) != lst2num(mul2(num_aleat)):
            print(f"Ha fallado en mul2 la entrada {num_aleat}")
            print(f"count {count}\n")
            equal = False
        elif math.floor((1/2)*lst2num(num_aleat)) != lst2num(div2(num_aleat)):
            print(f"Ha fallado en div2 la entrada {num_aleat}")
            print(f"count {count}\n")
            equal = False
        elif count == limit:
            break
