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

### Interpretación
- ANOVA de dos factores permite identificar:
  1. Si existe efecto significativo del **Lenguaje** sobre el tiempo.
  2. Si existe efecto significativo del **Tamaño de matriz** sobre el tiempo.
  3. Si existe **interacción** entre Lenguaje y Tamaño (es decir, si el efecto del Lenguaje depende del tamaño de la matriz).

- **Post-hoc Tukey HSD:** Si ANOVA detecta diferencias significativas, se comparan pares de niveles dentro de cada factor para identificar cuáles difieren.

- Los resultados se generan automáticamente en:
  - `results/report.txt` → tablas ANOVA y Tukey HSD  
  - `results/plot.png` → gráficos de medias con intervalos de confianza

## Reproducibilidad y ejecución con Docker

### Pasos completos para reproducir el experimento

```bash
# 1. Descargar la imagen desde Docker Hub
docker pull annie752/benchmark-matrices_prueba:latest

# 2. Crear una carpeta local en el escritorio para guardar los resultados
# (Esto la crea en tu escritorio o donde estés ejecutando el comando)
mkdir benchmark-results

# 3. Ejecutar el contenedor usando la imagen desde Docker Hub ingresando POWERSHELL
#EN WINDOWS
docker run --rm -it -v "$env:USERPROFILE\Desktop\benchmark-results:/app/results" annie752/benchmark-matrices_prueba snakemake --cores 4 -p

#EN LINUX Y IOS
docker run --rm -it -v "$HOME/Desktop/benchmark-results:/app/results" annie752/benchmark-matrices_prueba snakemake --cores 4 -p

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
# report.txt      -> análisis estadístico ANOVA + Tukey HSD
# plot.png        -> gráficos de medias + intervalos de confianza

# 6️⃣ Visualizar los resultados
# Puedes abrirlos desde el "Desktop Docker" o desde tu PC local:
# - benchmark-results/benchmark.csv  → abrir con Excel o LibreOffice
# -----------------------------
# Opción 2: Clonando el repositorio y construyendo la imagen localmente
git clone https://github.com/AnaLequipe/benchmark-matrices.git
cd benchmark-matrices
mkdir benchmark-results
docker build -t benchmark-matrices_prueba .
docker run --rm -v benchmark-results:/app/results benchmark-matrices_prueba
ls benchmark-results


