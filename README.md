# Benchmark reproducible de multiplicación de matrices NxN

## Objetivo
Evaluar comparativamente el rendimiento de cuatro lenguajes de programación (C++, Go, Java y Python) en la multiplicación de matrices cuadradas NxN bajo un entorno controlado y reproducible, asegurando buenas prácticas de documentación, control de entornos y análisis estadístico.

## Hipótesis
- **H₀ (nula):** No hay diferencia significativa entre los lenguajes en el tiempo de ejecución de la multiplicación de matrices NxN.  
- **H₁ (alternativa):** Sí existen diferencias significativas entre los lenguajes; los compilados (C++, Go) presentan mejor rendimiento que los interpretados o con máquina virtual (Java, Python).

## Metodología
- Algoritmo naive O(N³) (triple bucle) de multiplicación de matrices.  
- Matrices generadas aleatoriamente con semilla fija = 42.  
- Tamaños de matrices: 500, 1000, 2000.  
- Repeticiones: 5 ejecuciones por configuración.  
- Numeros de las matrices: [1-10]
- Variable dependiente: tiempo de ejecución (segundos).  

## Reproducibilidad y ejecución con Docker

### Pasos completos para reproducir el experimento

```bash
# Abrir CMD o PowerShell
# -----------------------------
# Opción 1: Usando imagen desde Docker Hub
# -----------------------------
docker run --rm -v benchmark-results:/app/results annie752/benchmark-matrices

# -----------------------------
# Opción 2: Clonando el repositorio desde GitHub y construyendo la imagen localmente
# -----------------------------
# Clonar el repositorio
git clone https://github.com/AnaLequipe/benchmark-matrices.git
cd benchmark-matrices

# Crear carpeta local para resultados
mkdir benchmark-results

# Construir la imagen Docker localmente
docker build -t benchmark-matrices .

# Ejecutar el contenedor y guardar resultados en la carpeta local
docker run --rm -v benchmark-results:/app/results benchmark-matrices

# -----------------------------
# 4. Verificar que los resultados se generaron
dir benchmark-results

# Los archivos esperados:
# benchmark.csv   -> resultados de tiempos

# 5. Abrir y analizar resultados
# CSV -> Excel
