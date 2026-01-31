"""
Ejercicios de Análisis de Complejidad Computacional
====================================================
Módulo importable con funciones optimizadas para examen.

USO RÁPIDO EN GOOGLE COLAB:
    !pip install requests
    import requests
    exec(requests.get('https://raw.githubusercontent.com/TU_USUARIO/ejercicios-complejidad/main/ejercicios.py').text)
    
    # O clonando el repo:
    !git clone https://github.com/TU_USUARIO/ejercicios-complejidad.git
    from ejercicios-complejidad.ejercicios import *

Autor: [Tu Nombre]
"""

import random
import time
from typing import List, Tuple, Callable, Any


# =============================================================================
# UTILIDAD: MEDICIÓN DE TIEMPO
# =============================================================================

def medir_tiempo(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """
    Mide el tiempo de ejecución de una función.
    
    Ejemplo:
        resultado, tiempo = medir_tiempo(mi_funcion, arg1, arg2)
        print(f"Tiempo: {tiempo:.6f} segundos")
    """
    inicio = time.perf_counter()
    resultado = func(*args, **kwargs)
    fin = time.perf_counter()
    return resultado, fin - inicio


# =============================================================================
# EJERCICIO 1: CONTRASEÑA ALEATORIA
# =============================================================================
"""
ANÁLISIS DE COMPLEJIDAD:
    - Tiempo: O(n) donde n = longitud (7-10), efectivamente O(1)
    - Espacio: O(n)

RECURSOS MATEMÁTICOS:
    - Generación pseudoaleatoria uniforme
    - Mapeo ASCII (códigos 33-126 = caracteres imprimibles)

ESTRUCTURAS DE PROGRAMACIÓN:
    - List comprehension para generación eficiente
    - Función chr() para conversión ASCII → carácter

¿POR QUÉ ES ÓPTIMA?
    - Usa lista + join() en lugar de concatenación de strings
    - Concatenar strings crea objetos nuevos cada vez: O(n²)
    - Lista + join() es O(n) total
"""

def generar_contrasena() -> str:
    """
    Genera una contraseña aleatoria de 7-10 caracteres.
    Caracteres del rango ASCII 33-126 (imprimibles).
    
    Returns:
        str: Contraseña generada
    
    Complejidad: Tiempo O(n), Espacio O(n) donde n ∈ [7,10]
    """
    longitud = random.randint(7, 10)
    return ''.join(chr(random.randint(33, 126)) for _ in range(longitud))


# =============================================================================
# EJERCICIO 2: MULTIPLICACIÓN DE MATRICES n×n
# =============================================================================
"""
ANÁLISIS DE COMPLEJIDAD:
    - Tiempo: O(n³) - tres bucles anidados
    - Espacio: O(n²) - matriz resultado

RECURSOS MATEMÁTICOS:
    - Producto matricial: C[i][j] = Σ(k=0 to n-1) A[i][k] * B[k][j]
    - Álgebra lineal básica

ESTRUCTURAS DE PROGRAMACIÓN:
    - Tres bucles for anidados
    - List comprehension para inicialización
    - Acceso indexado a listas bidimensionales

¿POR QUÉ ES ÓPTIMA?
    - Algoritmo clásico O(n³) es óptimo para implementación directa
    - Existen algoritmos como Strassen O(n^2.807) pero tienen constantes
      muy altas y solo son útiles para matrices enormes (n > 1000)
    - Precálculo de fila mejora localidad de caché
"""

def crear_matriz(n: int, min_val: int = 0, max_val: int = 99) -> List[List[int]]:
    """Crea matriz n×n con valores aleatorios."""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]


def multiplicar_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Multiplica dos matrices cuadradas A × B.
    
    Args:
        A, B: Matrices n×n
    
    Returns:
        Matriz resultado C = A × B
    
    Complejidad: Tiempo O(n³), Espacio O(n²)
    """
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        fila_a = A[i]  # Optimización de caché
        for j in range(n):
            suma = 0
            for k in range(n):
                suma += fila_a[k] * B[k][j]
            C[i][j] = suma
    
    return C


def mostrar_matriz(M: List[List[int]], nombre: str = "M", limite: int = 8):
    """Muestra matriz formateada (parcial si es grande)."""
    n = len(M)
    print(f"\n{nombre} ({n}×{n}):")
    if n <= limite:
        for fila in M:
            print("  [" + ", ".join(f"{x:4d}" for x in fila) + "]")
    else:
        for i in range(3):
            print("  [" + ", ".join(f"{M[i][j]:4d}" for j in range(3)) + f", ..., {M[i][-1]:4d}]")
        print("  ...")
        print("  [" + ", ".join(f"{M[-1][j]:4d}" for j in range(3)) + f", ..., {M[-1][-1]:4d}]")


# =============================================================================
# FUNCIONES DE DEMOSTRACIÓN (para el examen)
# =============================================================================

def demo_contrasena(n_ejemplos: int = 5):
    """Demuestra el ejercicio 1 con medición de tiempo."""
    print("=" * 60)
    print("EJERCICIO 1: CONTRASEÑA ALEATORIA")
    print("=" * 60)
    print("\nComplejidad: Tiempo O(n), Espacio O(n) donde n ∈ [7,10]")
    print("\nContraseñas generadas:")
    for i in range(n_ejemplos):
        pwd, t = medir_tiempo(generar_contrasena)
        print(f"  {i+1}. '{pwd}' (len={len(pwd)}) - Tiempo: {t*1e6:.2f} µs")


def demo_matrices(n: int = 10):
    """Demuestra el ejercicio 2 con medición de tiempo."""
    print("\n" + "=" * 60)
    print("EJERCICIO 2: MULTIPLICACIÓN DE MATRICES")
    print("=" * 60)
    print(f"\nComplejidad: Tiempo O(n³), Espacio O(n²)")
    print(f"Tamaño de prueba: {n}×{n}")
    
    A = crear_matriz(n)
    B = crear_matriz(n)
    
    C, tiempo = medir_tiempo(multiplicar_matrices, A, B)
    
    mostrar_matriz(A, "A")
    mostrar_matriz(B, "B")
    mostrar_matriz(C, "C = A × B")
    print(f"\nTiempo de multiplicación: {tiempo:.6f} segundos")


def benchmark_matrices():
    """Benchmark para verificar O(n³)."""
    print("\n" + "=" * 60)
    print("BENCHMARK: Verificación empírica de O(n³)")
    print("=" * 60)
    
    tamanos = [10, 50, 100, 200, 500]
    print(f"\n{'n':>6} | {'Tiempo':>12} | {'Ratio vs anterior':>18}")
    print("-" * 45)
    
    tiempo_anterior = None
    for n in tamanos:
        A, B = crear_matriz(n), crear_matriz(n)
        _, tiempo = medir_tiempo(multiplicar_matrices, A, B)
        
        if tiempo_anterior:
            ratio = tiempo / tiempo_anterior
            print(f"{n:>6} | {tiempo:>10.4f}s | {ratio:>18.2f}×")
        else:
            print(f"{n:>6} | {tiempo:>10.4f}s | {'---':>18}")
        
        tiempo_anterior = tiempo


# =============================================================================
# EJECUCIÓN DIRECTA
# =============================================================================

if __name__ == "__main__":
    demo_contrasena()
    demo_matrices()
    # benchmark_matrices()  # Descomentar para benchmark completo
