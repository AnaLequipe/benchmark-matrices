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
- Variable dependiente: tiempo de ejecución (segundos).  

## Reproducibilidad y ejecución con Docker

### Pasos completos para reproducir el experimento

```bash
# 1. Abrir CMD o PowerShell

# 2. (Opcional) Iniciar sesión en Docker si deseas descargar imágenes privadas o hacer push
docker login

# 3. Crear carpeta local para guardar resultados
mkdir C:\Users\ANA\Desktop\benchmark-results

# -----------------------------
# Opción 1: Usando imagen desde Docker Hub
# -----------------------------
docker run --rm -v C:\Users\ANA\Desktop\benchmark-results:/app/results annie752/benchmark-matrices

# -----------------------------
# Opción 2: Clonando el repositorio desde GitHub y construyendo la imagen localmente
# -----------------------------
# Clonar el repositorio
git clone https://github.com/AnaLequipe/benchmark-matrices.git
cd benchmark-matrices

# Crear carpeta local para resultados
mkdir C:\Users\ANA\Desktop\benchmark-results

# Construir la imagen Docker localmente
docker build -t benchmark-matrices .

# Ejecutar el contenedor y guardar resultados en la carpeta local
docker run --rm -v C:\Users\ANA\Desktop\benchmark-results:/app/results benchmark-matrices

# -----------------------------
# 4. Verificar que los resultados se generaron
dir C:\Users\ANA\Desktop\benchmark-results

# Los archivos esperados:
# benchmark.csv   -> resultados de tiempos
# report.txt      -> resumen estadístico
# plot.png        -> gráfico de medias con intervalos de confianza

# 5. Abrir y analizar resultados
# CSV -> Excel, LibreOffice Calc o Python/pandas
# TXT -> Notepad o cualquier editor de texto
# PNG -> cualquier visor de imágenes
