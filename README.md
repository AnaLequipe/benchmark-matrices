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
# 1. Descargar la imagen desde Docker Hub
docker pull annie752/benchmark-matrices_new:latest

# 2. Crear una carpeta local para guardar los resultados
# (Esto la crea en tu escritorio o donde estés ejecutando el comando)
mkdir benchmark-results

# 3. Ejecutar el contenedor usando la imagen desde Docker Hub
# y guardar los resultados dentro de la carpeta local "benchmark-results"
#docker run --rm -v "%cd%/benchmark-results:/app/results" annie752/benchmark-matrices_new:latest
#EN WINDOWS
docker run --rm -v "${env:USERPROFILE}\Desktop\benchmark-results:/app/results" annie752/benchmark-matrices_prueba:latest
#EN LINUX Y IOS
docker run --rm -v "$HOME/Desktop/benchmark-results:/app/results" annie752/benchmark-matrices_prueba:latest
# Explicación:
# - --rm              → elimina el contenedor después de ejecutarse (limpio)
# - -v ...:/app/results → monta tu carpeta local para guardar resultados del benchmark
# - annie752/benchmark-matrices_new:latest → tu imagen publicada en Docker Hub

# 4. Verificar que los resultados se generaron
# En Windows (CMD o PowerShell)
dir benchmark-results

# En Linux o Mac
ls benchmark-results

# Archivos esperados:
# benchmark.csv   -> tiempos de ejecución por lenguaje

# 6️⃣ Visualizar los resultados
# Puedes abrirlos desde el "Desktop Docker" o desde tu PC local:
# - benchmark-results/benchmark.csv  → abrir con Excel o LibreOffice
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


