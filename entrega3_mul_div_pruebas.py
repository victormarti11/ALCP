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

# Lista de números aleatorios de 10000 elementos
num_aleat = [random.randint(0, 9) for _ in range(10000)]


def mul2(x):
    c = 0                                               # Acarreo
    doble_x = []                                        # Lista vacía para almacenar el resultado
    
    for digito in x:
        doble = digito * 2 + c                          # Multiplicamos el dígito por 2 y sumamos el acarreo
        doble_x.append(doble % 10)                      # Agregamos al final de la lista la cifra de las unidades
        c = doble // 10                                 # Actualizamos el acarreo para el siguiente dígito
        
    if c > 0:                                           # Si aún hay un acarreo pendiente
        doble_x.append(c)                               # Agregamos al final de la lista la cifra correspondiente

    return doble_x


# Complejidad en tiempo
inicio = time.time()
resultado = mul2(num_aleat)
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución de mul2: {tiempo_ejecucion} segundos \n")

### OJO! LA LISTA ORIGINAL SE DA LA VUELTA POR EL REVERSE, NO LOGRO DEJARLA TAL CUAL
### div2() creo que se puede eliminar del todo

def div2(x):                                            # Funciona pero va más lento que la plus
    c = 0                                               # Acarreo
    mitad_x = []
    x.reverse()                                         # Para aprovechar la estructura de mul2()
    #print(x)                                           # es necesario revertir la lista
    for digito in x:
        mitad = math.floor((digito+c*10)*(1/2))         # La mitad de digito más el acarreo hecho decena, si hubiera
        # print (f"La mitad de {digito} es {mitad}")
        mitad_x = [mitad] + mitad_x                     # Añadimos la cifra al principio de la lista
        # print(f"He añadido {mitad%10}")
        if digito % 2 == 1:                             # Si dígito es impar nos llevamos una de acarreo
            c = 1
        else:                                           # Si dígito es par no llevamos acarreo
            c = 0

    return mitad_x

# Complejidad en tiempo
inicio = time.time()
resultado = div2(num_aleat)
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución de div2: {tiempo_ejecucion} segundos \n")

def div2_plus(x):                                       # Funciona y va más rápido que la normal
    c = 0                                               # Acarreo
    mitad_x = []
    x.reverse()                                         # Para aprovechar la estructura de mul2()
    #print(x)                                           # es necesario revertir la lista
    for digito in x:
        mitad = (digito+c*10)//2                        # La mitad de digito más el acarreo hecho decena, si hubiera
        # print (f"La mitad de {digito} es {mitad}")
        mitad_x = [mitad] + mitad_x                     # Añadimos la cifra al principio de la lista
        # print(f"He añadido {mitad%10}")
        if digito % 2 == 1:                             # Si dígito es impar nos llevamos una de acarreo
            c = 1
        else:                                           # Si dígito es par no llevamos acarreo
            c = 0
            
    return mitad_x

# Complejidad en tiempo
inicio = time.time()
resultado = div2_plus(num_aleat)
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución de div2_plus: {tiempo_ejecucion} segundos \n")

def lst2num(l):                                                         # Transforma una lista en un número entero
    exp = 0                                                             # Ej: [1,2,3] --> 321
    result = 0
    for i in l:
        result += i*10**exp
        exp += 1
    return result

def remover_ceros(a):                                                   # De lista a lista reducida
    # a = lista de dí­gitos decimales                                    # Ej: [1,2,3,0] --> [1,2,3]
    n = len(a)
    while n >= 1 and a[n - 1] == 0:
        n -= 1
    del a[n:]
    return a

def test():
    limit = 1000
    equal = True
    count = 1
    print(f"Test ha comenzado con límite {limit}")
    while equal:
        num_aleat = [random.randint(0, 9) for _ in range(10000)]        # Lista aleatoria de longitud 10000
        num_aleat = remover_ceros(num_aleat)                            # Se convierte a lista reducida
        if (2*lst2num(num_aleat)) != lst2num(mul2(num_aleat)):          # Compara mult2() convirtiéndo a número
            print(f"Ha fallado en mul2 la entrada {num_aleat}")
            print(f"count {count}\n")
            equal = False
        elif lst2num(num_aleat)//2 != lst2num(div2_plus(num_aleat)):    # Compara div2_plus() convirtiendo a número
            print(f"Ha fallado en div2 la entrada {num_aleat}")
            print(f"count {count}\n")
            equal = False
        count += 1
        
        if count == limit:                                              # No ha encontrado una desigualdad
            print(f"Count {count}\n")                                   # y el contador ha llegado al límite
            break

# Complejidad en tiempo
inicio = time.time()
resultado = test()
fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución de test: {tiempo_ejecucion} segundos \n")              
        
    
    
