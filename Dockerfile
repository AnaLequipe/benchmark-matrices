# 1. Imagen base con compiladores y Python
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

# 4. Instalamos dependencias de Python
#    Si tienes requirements.txt, se usará. Si falta, instala las básicas necesarias.
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt || \
    pip3 install --no-cache-dir numpy pandas scipy matplotlib statsmodels

# 5. Copiamos el proyecto al contenedor
WORKDIR /app
COPY . /app

# 6. Evita buffering (útil para ver logs en tiempo real)
ENV PYTHONUNBUFFERED=1

# 7. Comando por defecto
CMD ["python3", "run_benchmark.py"]
