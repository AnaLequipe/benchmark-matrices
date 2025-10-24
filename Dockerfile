# 1. Imagen base
FROM ubuntu:22.04

# 2. Mantenedor
LABEL maintainer="Ana Lequipe <analequipe752@gmail.com>"

# 3. Instalamos Python, pip y herramientas necesarias
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    g++ \
    golang \
    openjdk-17-jdk \
    time \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && apt-get clean

# 4. Instalamos dependencias de Python + Snakemake
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt || \
    pip3 install --no-cache-dir numpy pandas scipy matplotlib statsmodels seaborn snakemake

# 5. Copiamos el proyecto
WORKDIR /app
COPY . /app

# 6. Desactiva el buffer para ver logs en tiempo real
ENV PYTHONUNBUFFERED=1

# 7. Comando por defecto (puedes ejecutar run_benchmark.py o snakemake)
#CMD ["python3", "run_benchmark.py"]
CMD ["python3", "-m", "snakemake", "--cores", "1", "--rerun-incomplete"]

