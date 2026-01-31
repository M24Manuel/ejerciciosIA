"""
Ejercicios 

Autor: Manuel Evangelista TIburcio
"""

import random
import time
from typing import List, Tuple, Callable, Any




def medir_tiempo(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """
    Mide el tiempo de ejecución de una función.
    
    Args:
        func: Función a ejecutar
        *args, **kwargs: Argumentos para la función
    
    Returns:
        Tupla (resultado, tiempo_en_segundos)
    """
    inicio = time.perf_counter()
    resultado = func(*args, **kwargs)
    fin = time.perf_counter()
    return resultado, fin - inicio


def formato_tiempo(segundos: float) -> str:
    """Formatea el tiempo de manera legible."""
    if segundos < 1e-6:
        return f"{segundos * 1e9:.2f} ns"
    elif segundos < 1e-3:
        return f"{segundos * 1e6:.2f} µs"
    elif segundos < 1:
        return f"{segundos * 1e3:.2f} ms"
    else:
        return f"{segundos:.4f} s"



# EJERCICIO 1: CONTRASEÑA ALEATORIA
"""
ANÁLISIS DE COMPLEJIDAD - Ejercicio 1


De que va:
    Generar contraseña aleatoria de longitud entre 7 y 10 caracteres.
    Cada carácter proviene del rango ASCII 33-126 (caracteres imprimibles). :D

Complejidad: O(n)
    Donde n es la longitud de la contraseña (7 ≤ n ≤ 10).
    
    Desglose:
    - random.randint(7, 10): O(1)
    - Bucle de generación: O(n) iteraciones
        - random.randint(33, 126): O(1) por iteración
        - chr(): O(1) por iteración
        - Append a lista: O(1) amortizado
    - ''.join(): O(n) para concatenar n caracteres
    
    Total: O(1) + O(n) + O(n) = O(n)
    
    Dado que n está acotado (7 ≤ n ≤ 10), en la práctica es O(1),
    pero el análisis general es O(n) respecto a la longitud.

Complejidad en tamaño: O(n)
    - Lista de caracteres: O(n)
    - String resultante: O(n)
    
    Total: O(n)
    
    Nota: Dado que n ≤ 10, el espacio es constante en la práctica.

algo de optimizacion:
    1. Uso de lista + join() en lugar de concatenación de strings
       (evita crear múltiples objetos string intermedios)
    2. Generación directa con chr() sin tabla de lookup
    3. Sin validaciones innecesarias dado el rango fijo
"""


def generar_contrasena() -> str:
    """
    Genera una contraseña aleatoria.
    
    Especificaciones:
        - Longitud: entre 7 y 10 caracteres (aleatorio)
        - Caracteres: ASCII 33-126 (imprimibles, excluyendo espacio)
    
    Returns:
        str: Contraseña generada aleatoriamente
    
    Complejidad Temporal: O(n) donde n es la longitud (7-10)
    Complejidad Espacial: O(n)
    """
    longitud = random.randint(7, 10)
    
    # Generación usando list comprehension (más eficiente que concatenación)
    caracteres = [chr(random.randint(33, 126)) for _ in range(longitud)]
    
    return ''.join(caracteres)


def demo_ejercicio_1():
    
    print("=" * 70)
    print("EJERCICIO 1: CONTRASEÑA ALEATORIA")
    print("=" * 70)
    
    print(" ANÁLISIS DE COMPLEJIDAD:")
    print("   • Complejidad Temporal: O(n), donde n = longitud (7-10)")
    print("   • Complejidad Espacial: O(n)")
    print("   • En la práctica: O(1) dado que n está acotado superiormente")
    
    print(" GENERACIÓN DE CONTRASEÑAS:")
    print("-" * 50)
    
    tiempos = []
    for i in range(10):
        contrasena, tiempo = medir_tiempo(generar_contrasena)
        tiempos.append(tiempo)
        print(f"   [{i+1:2d}] '{contrasena}' (len={len(contrasena):2d}) | "
              f"Tiempo: {formato_tiempo(tiempo)}")
    
    print("-" * 50)
    promedio = sum(tiempos) / len(tiempos)
    print(f"   Tiempo promedio: {formato_tiempo(promedio)}")
    print(f"   Tiempo mínimo:   {formato_tiempo(min(tiempos))}")
    print(f"   Tiempo máximo:   {formato_tiempo(max(tiempos))}")



# EJERCICIO 2: MULTIPLICACIÓN DE MATRICES n×n

"""
Complejidad - Ejercicio 2


De que va:
    Multiplicar dos matrices cuadradas de tamaño n×n.
    C[i][j] = Σ(k=0 to n-1) A[i][k] * B[k][j]

Complejida en tiempo: O(n³)
    
    Desglose del algoritmo clásico:
    - Bucle externo (filas de A): n iteraciones
        - Bucle medio (columnas de B): n iteraciones
            - Bucle interno (suma de productos): n iteraciones
                - Acceso a elementos: O(1)
                - Multiplicación: O(1)
                - Suma: O(1)
    
    Total: n × n × n × O(1) = O(n³)
    

Complejidad espacial: O(n²)
    
    Desglose:
    - Matriz A: n × n = O(n²)
    - Matriz B: n × n = O(n²)
    - Matriz C (resultado): n × n = O(n²)
    - Variables auxiliares: O(1)
    
    Total: O(n²) + O(n²) + O(n²) = O(n²)
    
    Si consideramos solo el espacio adicional (sin contar entrada):
    Espacio auxiliar: O(n²) para la matriz resultado

Optimizaciones:
    1. Acceso contiguo a memoria: iteramos por filas (row-major order)
    2. Uso de listas nativas de Python (más rápido que numpy para n pequeño)
    4. Inicialización directa de la matriz resultado con ceros
"""


def crear_matriz_aleatoria(n: int, min_val: int = 0, max_val: int = 99) -> List[List[int]]:
    """
    Crea una matriz n×n con valores aleatorios.
    
    Args:
        n: Dimensión de la matriz
        min_val: Valor mínimo (inclusive)
        max_val: Valor máximo (inclusive)
    
    Returns:
        Matriz n×n como lista de listas
    
    Complejidad Temporal: O(n²)
    Complejidad Espacial: O(n²)
    """
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]


def multiplicar_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Multiplica dos matrices cuadradas usando el algoritmo clásico.
    
    Args:
        A: Primera matriz n×n
        B: Segunda matriz n×n
    
    Returns:
        Matriz resultado C = A × B
    
    Complejidad Temporal: O(n³)
    Complejidad Espacial: O(n²) para la matriz resultado
    
    Optimizaciones:
        - Acceso secuencial a filas de A (mejor caché)
        - Precálculo de fila actual de A
    """
    n = len(A)
    
    # Inicializar matriz resultado con ceros - O(n²)
    C = [[0] * n for _ in range(n)]
    
    # Algoritmo de multiplicación clásico - O(n³)
    for i in range(n):
        # Precalcular fila de A para mejor localidad de caché
        fila_a = A[i]
        for j in range(n):
            suma = 0
            for k in range(n):
                suma += fila_a[k] * B[k][j]
            C[i][j] = suma
    
    return C


def imprimir_matriz(matriz: List[List[int]], nombre: str = "Matriz", 
                    max_mostrar: int = 10) -> None:
    """
    Imprime una matriz de forma formateada.
    
    Para matrices grandes, muestra solo las esquinas.
    """
    n = len(matriz)
    print(f"\n{nombre} ({n}×{n}):")
    
    if n <= max_mostrar:
        # Mostrar matriz completa
        for fila in matriz:
            print("  [" + ", ".join(f"{x:4d}" for x in fila) + "]")
    else:
        # Mostrar esquinas para matrices grandes
        print(f"  (Mostrando esquinas, matriz muy grande para visualizar completa)")
        corner = min(3, n)
        
        # Esquina superior izquierda
        for i in range(corner):
            fila_str = ", ".join(f"{matriz[i][j]:4d}" for j in range(corner))
            print(f"  [{fila_str}, ..., {matriz[i][-1]:4d}]")
        
        print("  " + "." * 30)
        
        # Esquina inferior
        for i in range(n - corner, n):
            fila_str = ", ".join(f"{matriz[i][j]:4d}" for j in range(corner))
            print(f"  [{fila_str}, ..., {matriz[i][-1]:4d}]")


def verificar_multiplicacion(A: List[List[int]], B: List[List[int]], 
                             C: List[List[int]], muestras: int = 5) -> bool:
    """
    Verifica la corrección de la multiplicación en posiciones aleatorias.
    
    Complejidad: O(muestras × n)
    """
    n = len(A)
    for _ in range(muestras):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        esperado = sum(A[i][k] * B[k][j] for k in range(n))
        if C[i][j] != esperado:
            return False
    return True


def demo_ejercicio_2():
    """Demostración del Ejercicio 2 con diferentes tamaños."""
    print("\n" + "=" * 70)
    print("EJERCICIO 2: MULTIPLICACIÓN DE MATRICES n×n")
    print("=" * 70)
    
    print(" ANÁLISIS DE COMPLEJIDAD:")
    print("   • Complejidad Temporal: O(n³)")
    print("   • Complejidad Espacial: O(n²)")
    print("   • Algoritmo: Multiplicación clásica (óptimo para n moderado)")
    
    # Tamaños a probar
    tamanos = [10, 100, 500, 1000]
    
    print(" RESULTADOS POR TAMAÑO:")
    print("-" * 70)
    print(f"{'Tamaño':>10} | {'Tiempo Creación':>18} | {'Tiempo Mult.':>18} | {'Verificado':>10}")
    print("-" * 70)
    
    resultados = []
    
    for n in tamanos:
        # Crear matrices
        (A, B), tiempo_creacion = medir_tiempo(
            lambda: (crear_matriz_aleatoria(n), crear_matriz_aleatoria(n))
        )
        
        # Multiplicar
        C, tiempo_mult = medir_tiempo(multiplicar_matrices, A, B)
        
        # Verificar
        correcto = verificar_multiplicacion(A, B, C)
        
        resultados.append({
            'n': n,
            'tiempo_creacion': tiempo_creacion,
            'tiempo_mult': tiempo_mult,
            'correcto': correcto
        })
        
        print(f"{n:>10} | {formato_tiempo(tiempo_creacion):>18} | "
              f"{formato_tiempo(tiempo_mult):>18} | {'✓ Sí':>10}" if correcto 
              else f"{n:>10} | {formato_tiempo(tiempo_creacion):>18} | "
              f"{formato_tiempo(tiempo_mult):>18} | {'✗ No':>10}")
        
        # Mostrar matriz para tamaños pequeños
        if n <= 10:
            imprimir_matriz(A, "Matriz A")
            imprimir_matriz(B, "Matriz B")
            imprimir_matriz(C, "Resultado C = A × B")
    
    print("-" * 70)
    
    # Análisis de crecimiento
    print(" ANÁLISIS DE CRECIMIENTO (verificación empírica de O(n³)):")
    print("-" * 50)
    
    for i in range(1, len(resultados)):
        prev = resultados[i-1]
        curr = resultados[i]
        
        ratio_n = curr['n'] / prev['n']
        ratio_tiempo = curr['tiempo_mult'] / prev['tiempo_mult'] if prev['tiempo_mult'] > 0 else float('inf')
        ratio_esperado = ratio_n ** 3
        
        print(f"   n: {prev['n']:>5} → {curr['n']:>5} (×{ratio_n:.1f})")
        print(f"   Tiempo: {formato_tiempo(prev['tiempo_mult']):>12} → {formato_tiempo(curr['tiempo_mult']):>12}")
        print(f"   Ratio real: {ratio_tiempo:>8.2f}×")
        print(f"   Ratio esperado O(n³): {ratio_esperado:>8.2f}×")
        print()


# EJECUCIÓN PRINCIPAL


def main():
    """Función principal que ejecuta todos los ejercicios."""
   
    print(" EJERCICIOS")

   
    # Semilla para reproducibilidad (comentar para resultados aleatorios)
    # random.seed(42)
    
    # Ejecutar ejercicio 1
    demo_ejercicio_1()
    
    # Ejecutar ejercicio 2
    demo_ejercicio_2()
    
    print("\n" + "═" * 70)
    print("   RESUMEN DE COMPLEJIDADES")
    print("═" * 70)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │  Ejercicio                    │  Tiempo    │  Espacio           │
    ├─────────────────────────────────────────────────────────────────┤
    │  1. Contraseña Aleatoria      │  O(n)*     │  O(n)*             │
    │  2. Multiplicación Matrices   │  O(n³)     │  O(n²)             │
    └─────────────────────────────────────────────────────────────────┘
    
    * Donde n es la longitud de la contraseña (7-10), efectivamente O(1)
    
    Nota: El análisis considera las operaciones dominantes y asume que
    las operaciones aritméticas básicas son O(1).
    """)


if __name__ == "__main__":
    main()
