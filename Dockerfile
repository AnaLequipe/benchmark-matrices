#  1. Usamos una base con todo lo necesario (Ubuntu con compiladores)
FROM ubuntu:22.04

#  2. Quién lo mantiene (puedes poner tu nombre)
LABEL maintainer="AnaLequipe <analequipe752@gmail.com>"

#  3. Actualizamos e instalamos las herramientas
RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    g++ \
    golang \
    openjdk-17-jdk \
    time \
    && apt-get clean

# 4. Instalamos las librerías de Python si las hay
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt || true

# 5. Copiamos todo el proyecto dentro del contenedor
WORKDIR /app
COPY . /app

# 6. Comando por defecto: ejecutar el benchmark
CMD ["python3", "run_benchmark.py"]
