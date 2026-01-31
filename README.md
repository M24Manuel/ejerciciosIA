# Ejercicios de Complejidad Computacional

**Autor:** [Tu Nombre Completo]  
**Materia:** [Nombre de la Materia]  
**Institución:** UNAM - Facultad de Ciencias

---

## 📋 Descripción

Implementaciones optimizadas de ejercicios de análisis de complejidad computacional en Python. Cada función incluye:

- Análisis de complejidad temporal
- Análisis de complejidad espacial
- Explicación de recursos matemáticos utilizados
- Justificación de la optimización

---

## 🚀 Uso Rápido en Google Colab

### Opción 1: Importar directamente desde GitHub

```python
# Método más rápido - ejecutar en una celda
!pip install requests -q
import requests
exec(requests.get('https://raw.githubusercontent.com/TU_USUARIO/ejercicios-complejidad/main/ejercicios.py').text)

# Ahora puedes usar las funciones directamente:
print(generar_contrasena())

A = crear_matriz(10)
B = crear_matriz(10)
C = multiplicar_matrices(A, B)
mostrar_matriz(C, "Resultado")
```

### Opción 2: Clonar repositorio

```python
!git clone https://github.com/TU_USUARIO/ejercicios-complejidad.git
%cd ejercicios-complejidad

from ejercicios import *

# Ejecutar demos
demo_contrasena()
demo_matrices(10)
```

---

## 📁 Ejercicios Incluidos

### Ejercicio 1: Contraseña Aleatoria

```python
pwd = generar_contrasena()
print(pwd)  # Ej: "xK#9@mPq"
```

| Aspecto | Valor |
|---------|-------|
| **Complejidad Temporal** | O(n) donde n ∈ [7,10] |
| **Complejidad Espacial** | O(n) |
| **Recurso Matemático** | Distribución uniforme, mapeo ASCII 33-126 |
| **Estructura** | List comprehension + join() |

**¿Por qué es óptima?**
- Usa `join()` en lugar de concatenación (`+=`), evitando crear strings intermedios
- Generación directa con `chr()` sin tablas de lookup

---

### Ejercicio 2: Multiplicación de Matrices n×n

```python
A = crear_matriz(100)
B = crear_matriz(100)
C = multiplicar_matrices(A, B)
mostrar_matriz(C)
```

| Aspecto | Valor |
|---------|-------|
| **Complejidad Temporal** | O(n³) |
| **Complejidad Espacial** | O(n²) |
| **Recurso Matemático** | C[i][j] = Σ A[i][k] × B[k][j] |
| **Estructura** | Triple bucle anidado |

**¿Por qué es óptima?**
- Algoritmo clásico es el más eficiente para n < 1000
- Precálculo de fila mejora localidad de caché
- Strassen (O(n^2.807)) solo conviene para matrices enormes

---

## 📊 Funciones Disponibles

| Función | Descripción |
|---------|-------------|
| `generar_contrasena()` | Genera contraseña aleatoria 7-10 chars |
| `crear_matriz(n)` | Crea matriz n×n con valores 0-99 |
| `multiplicar_matrices(A, B)` | Multiplica matrices A × B |
| `mostrar_matriz(M, nombre)` | Imprime matriz formateada |
| `medir_tiempo(func, *args)` | Mide tiempo de ejecución |
| `demo_contrasena()` | Demo ejercicio 1 |
| `demo_matrices(n)` | Demo ejercicio 2 |
| `benchmark_matrices()` | Verifica O(n³) empíricamente |

---

## 🎯 Guía para el Examen

1. **Abrir Google Colab**
2. **Ejecutar celda de importación** (Opción 1 arriba)
3. **Esperar input de la profesora**
4. **Llamar función correspondiente**
5. **Explicar verbalmente:**
   - Cómo funciona el algoritmo
   - Recursos matemáticos usados
   - Estructuras de programación empleadas
   - Por qué es óptima la solución

---

## 📝 Licencia

Proyecto académico - UNAM Facultad de Ciencias
