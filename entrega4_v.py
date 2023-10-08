def es_certificado_valido(N,L):
    val = True
    if (not isinstance(N,int)) or (not isinstance(L,list)): # N no es entero o L no es lista
        val =  False
    elif 2 <= N <= 100:    #Caso 1
        if not es_primo(N) or L != ['caso1',N]:  # Si N no es primo o
            val = False                              # L es distinto de [' caso1 ',N] es falso
    elif N > 100:    # Caso 2
        l = len(L)
        if l < 4:   # Si N es primo, n-1 va a ser compuesto y al menos va a ser producto de
            return False  # 2 factores primos
        elif (L[0] != 'caso2') or (L[1] != N):
            return False
        for i in range(2,l): #Si los elementos a partir de N no son listas o los elementos de estas
            if ((not isinstance(L[i],list)) or (not isinstance(L[i][0],int)) # no son los correctos
                or (not isinstance(L[i][1],int)) or (not isinstance(L[i][2],list)) # devuelve False
                or (not isinstance(L[i][3],int))): 
                return False    
        n1 = 1
        for i in range(2,l):       # Comprobamos que los factores primos que nos dan de N-1
           n1 *= L[i][0]**L[i][1]  # Realmente dan N - 1
        if n1 != N - 1:         # Sino lo cumplen:
           return False         # devolvemos False
        
        for i in range(2,l):                            # Comprobamos que certificado(p_i) es 
           val = es_certificado_valido(L[i][0],L[i][2]) # válido de forma recursiva
           if val == False:                             # Si no lo es
              return val                                # Devolvemos False
        
        for i in range(2,l):                  # Comprobamos que x_i cumple la condición 2
           val = Lucas(L[i][3],L[i][0],L[1])  # del test de primalidad de Lucas          
           if val == False:                   # si alguno no lo cumple
               return val                     # devolvemos False
    else: # Caso 3 N < 2
        val = False # Devolvemos False
        
    return val


def es_primo(n): # Calcula número primos
    primo = True
    if n == 2:
        primo = True
        return primo
    elif n % 2 == 0:
        primo = False
        return primo
    i = 3
    while i < n:
        if n % i == 0:
            primo = False
            break
        i += 2
        
    return primo

#Comprueba que el entero x, comprueba la condición 2 del test de primalidad de Lucas
#para un número N y p factor primo de N -1
def Lucas(x,p,N): 
    return (potencia_mod(x,N-1,N) == 1) and (potencia_mod(x,(N-1)//p,N) != 1) 
    
#Funciones vistas en clase para calcular a^k mod(N) y a*b mod(N)          
def potencia_mod(a,k,N):
    if k == 0:
        r = 1 
    elif k % 2 == 0:
        r = potencia_mod(a, k//2, N) 
        r = multiplicar_mod(r,r,N)
    else:
        r = potencia_mod(a,k-1,N)
        r = multiplicar_mod(a,r,N)
    return r


def multiplicar_mod(a,b,N):
    c = a * b 
    c %= N
    return c
