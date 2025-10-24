import subprocess
import csv
import os
import time
import platform
from datetime import datetime
import shutil
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import seaborn as sns
import matplotlib.pyplot as plt

GO_EXE = "matrix_benchmark.exe" if platform.system() == "Windows" else "matrix_benchmark"

# -------------------- CONFIGURACIÓN --------------------
Ns = [500, 1000, 2000]   # tamaños de matrices
#Ns = [10]   # tamaños de matrices
repeticiones = 5
semilla = 42
max_val = 10

languages = {
    "cpp": {
        "compile": ["g++", "-O3", "src/cpp/matrix_benchmark.cpp", "-o", f"src/cpp/matrix_benchmark{'.exe' if platform.system()=='Windows' else ''}"],
        "run": [f"src/cpp/matrix_benchmark{'.exe' if platform.system()=='Windows' else ''}"]
    },
    "go": {
        "compile": ["go", "build", "-o", f"src/go/{GO_EXE}", "src/go/matrix_benchmark.go"],
        "run": [f"src/go/{GO_EXE}"]
    },
    "java": {
        "compile": ["javac", "src/java/MatrixBenchmark.java"],
        "run": ["java", "-cp", "src/java", "MatrixBenchmark"]
    },
    "python": {
        "compile": None,
        "run": ["python", "src/python/matrix_benchmark.py"]
    }
}
csv_dir = "results"
os.makedirs(csv_dir, exist_ok=True)
csv_file = os.path.join(csv_dir, "benchmark.csv")

print("🚀 Iniciando ejecución del benchmark...\n")

# Si existe un resultado anterior, lo respaldamos con fecha y hora
if os.path.exists(csv_file):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"results/benchmark_{timestamp}.csv"
    shutil.copy2(csv_file, backup_file)
    print(f"📦 Copia de seguridad creada: {backup_file}")


# -------------------- COMPILAR --------------------
print("⚙️  Compilando todos los lenguajes necesarios...\n")
for lang, cmds in languages.items():
    if cmds["compile"]:
        print(f"🔹 Compilando {lang}...")
        subprocess.run(cmds["compile"], check=True)
    else:
        print(f"⚡ {lang} no requiere compilación.")

# -------------------- EJECUTAR Y MEDIR --------------------
print("🏃 Ejecutando benchmarks, esto puede tardar unos minutos...\n")


with open(csv_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Id", "Lenguaje", "N", "Tiempo_segundos"])

    id_counter = 1
    for lang, cmds in languages.items():
        for N in Ns:
            for rep in range(repeticiones):
                print(f"▶ Ejecutando {lang}, N={N}, repetición {rep+1}...")
                start = time.time()

                # Ejecuta el programa con los parámetros
                process = subprocess.run(
                    [*cmds["run"]],
                    input=f"{semilla}\n{max_val}\n{N}\n",
                    text=True,
                    capture_output=True
                )

                end = time.time()
                duracion = end - start

                # Guardar en CSV
                writer.writerow([id_counter, lang, N, duracion])
                id_counter += 1

print("\n✅ Benchmark completado correctamente.")
print(f"\n✅ Resultados guardados en {csv_file}")


# -------------------- ANALISIS ESTADISTICO --------------------
df = pd.read_csv(csv_file)

# Two-Way ANOVA con interacción
modelo = ols('Tiempo_segundos ~ C(Lenguaje) * C(N)', data=df).fit()
anova_result = sm.stats.anova_lm(modelo)
anova_csv = os.path.join(csv_dir, "anova.csv")
anova_result.to_csv(anova_csv)
print(f"\n📊 ANOVA guardado en {anova_csv}")

# Tukey HSD por Lenguaje
tukey = pairwise_tukeyhsd(endog=df['Tiempo_segundos'], groups=df['Lenguaje'], alpha=0.05)
tukey_summary = pd.DataFrame(data=tukey.summary().data[1:], columns=tukey.summary().data[0])
tukey_csv = os.path.join(csv_dir, "tukey.csv")
tukey_summary.to_csv(tukey_csv, index=False)
print(f"\n🔍 Tukey HSD guardado en {tukey_csv}")

# Gráfico de medias por Lenguaje y N
plt.figure(figsize=(8,5))
sns.pointplot(data=df, x="N", y="Tiempo_segundos", hue="Lenguaje", errorbar=('ci', 95), dodge=True)
plt.title("Benchmark: Tiempo promedio por Lenguaje y N")
plt.ylabel("Tiempo (segundos)")
plt.xlabel("Tamaño de matriz N")
plt.tight_layout()
plot_file = os.path.join(csv_dir, "plots.png")
plt.savefig(plot_file)
plt.close()
print(f"\n📈 Gráfico guardado en {plot_file}")