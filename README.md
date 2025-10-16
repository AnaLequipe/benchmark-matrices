# benchmark-matrices
Trabajo de Reproducibilidad
# Benchmark reproducible de multiplicación de matrices NxN

## Objetivo
Evaluar comparativamente el rendimiento de C++, Go, Java y Python en la multiplicación de matrices NxN bajo un entorno controlado y reproducible.

## Metodología
- Algoritmo: Naive O(N³)
- Semilla fija: 42
- Dimensiones: 500, 1000, 2000
- Repeticiones: 5 por configuración
- Variables: Tiempo de ejecución (segundos)

## Reproducibilidad
1. Crear entorno:# Benchmark reproducible de multiplicación de matrices NxN

## Objetivo
Evaluar comparativamente el rendimiento de C++, Go, Java y Python en la multiplicación de matrices NxN bajo un entorno controlado y reproducible.

## Metodología
- Algoritmo: Naive O(N³)
- Semilla fija: 42
- Dimensiones: 500, 1000, 2000
- Repeticiones: 5 por configuración
- Variables: Tiempo de ejecución (segundos)

## Enlaces del proyecto

- Código fuente en GitHub: [https://github.com/AnaLequipe/benchmark-matrices](https://github.com/AnaLequipe/benchmark-matrices)  
- Imagen Docker en Docker Hub: [https://hub.docker.com/repository/docker/annie752/benchmark-matrices/general](https://hub.docker.com/repository/docker/annie752/benchmark-matrices/general)


## Entorno reproducible con Docker

### Requisitos
- Tener instalado [Docker](https://www.docker.com/get-started).  
- Opcional: Git para clonar el repositorio.

### Construcción del contenedor
Desde la raíz del proyecto:

```bash
docker build -t benchmark-matrices .

# Pasos completos para reproducir el experimento
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
   
