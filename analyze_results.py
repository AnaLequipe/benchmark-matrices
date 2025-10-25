import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Directorio de resultados
csv_dir = "results"
os.makedirs(csv_dir, exist_ok=True)
csv_file = os.path.join(csv_dir, "benchmark.csv")

# -------------------- CARGAR DATOS --------------------
print("📂 Cargando resultados desde:", csv_file)
df = pd.read_csv(csv_file)

# -------------------- ANÁLISIS ESTADÍSTICO --------------------
print("📊 Realizando ANOVA de dos factores (Lenguaje × N)...")
modelo = ols('Tiempo_segundos ~ C(Lenguaje) * C(N)', data=df).fit()
anova_result = sm.stats.anova_lm(modelo)

anova_csv = os.path.join(csv_dir, "anova.csv")
anova_result.to_csv(anova_csv)
print(f"✅ ANOVA guardado en {anova_csv}")

# -------------------- PRUEBA TUKEY HSD --------------------
print("🔍 Ejecutando prueba post-hoc Tukey HSD...")
tukey = pairwise_tukeyhsd(endog=df['Tiempo_segundos'], groups=df['Lenguaje'], alpha=0.05)
tukey_summary = pd.DataFrame(data=tukey.summary().data[1:], columns=tukey.summary().data[0])

tukey_csv = os.path.join(csv_dir, "tukey.csv")
tukey_summary.to_csv(tukey_csv, index=False)
print(f"✅ Tukey HSD guardado en {tukey_csv}")

# -------------------- GRÁFICOS --------------------
print("📈 Generando gráficos de resultados...")

plt.figure(figsize=(8,5))
sns.pointplot(data=df, x="N", y="Tiempo_segundos", hue="Lenguaje", errorbar=('ci', 95), dodge=True)
plt.title("Benchmark: Tiempo promedio por Lenguaje y N")
plt.ylabel("Tiempo (segundos)")
plt.xlabel("Tamaño de matriz N")
plt.tight_layout()

plot_file = os.path.join(csv_dir, "plots.png")
plt.savefig(plot_file)
plt.close()
print(f"✅ Gráfico guardado en {plot_file}")

print("\n🎉 Análisis estadístico completado correctamente.")
