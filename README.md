# ALCP: Entrega 5
## Práctica 5:
Implementar la función sqrt_mod(a, p, n) que calcule una solución de $x2≡a(mod p^n)$
 donde p es un primo impar, $n \geq 1$ y $0 \leq a< p^n$
. La solución devuelva debe estar en el intervalo $[0,p^{n−1}]$
. En caso de que la ecuación no tenga solución, la función debe devolver None. La implementación debe estar en el fichero entrega5.py e incluir todas las funciones auxiliares utilizadas. Fecha límite: 29/oct/2023, 23:59.


Casos de prueba:

[sqrt_mod(a, 17, 1) for a in range(17)] -> [0, 1, 6, None, 15, None, None, None, 5, 14, None, None, None, 9, None, 7, 4]  
sqrt_mod(3, 28091881, 1) -> 20378105  
sqrt_mod(3, 28091881, 4) -> 185205998304326718269046083598  
sqrt_mod(167042, 17, 7) -> 180047  
sqrt_mod(250563, 17, 5) -> None  
