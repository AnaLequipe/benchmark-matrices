# -----------------------------------------------------------
# Snakefile - Pipeline de Benchmark Reproducible
# -----------------------------------------------------------

# 1️⃣ Regla principal
rule all:
    input:
        "results/benchmark.csv",
        "results/anova.csv",
        "results/tukey.csv",
        "results/plots.png"

# 2️⃣ Compilar C++
rule compile_cpp:
    output:
        "src/cpp/matrix_benchmark"
    shell:
        "g++ -O3 src/cpp/matrix_benchmark.cpp -o src/cpp/matrix_benchmark"

# 3️⃣ Compilar Go
rule compile_go:
    output:
        "src/go/matrix_benchmark"
    shell:
        "go build -o src/go/matrix_benchmark src/go/matrix_benchmark.go"

# 4️⃣ Compilar Java
rule compile_java:
    output:
        "src/java/MatrixBenchmark.class"
    shell:
        "javac src/java/MatrixBenchmark.java"

# 5️⃣ Ejecutar el benchmark (usa tu run.py)
rule run_benchmark:
    input:
        "src/cpp/matrix_benchmark",
        "src/go/matrix_benchmark",
        "src/java/MatrixBenchmark.class"
    output:
        "results/benchmark.csv"
    shell:
        "python run.py"

# 6️⃣ ANOVA y Tukey
rule analyze:
    input:
        "results/benchmark.csv"
    output:
        "results/anova.csv",
        "results/tukey.csv",
        "results/plots.png"
    shell:
        "python run.py"
