# Usa una imagen oficial de Python
FROM python:3.11-slim

# Crea un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY publisher.py .

# Comando de inicio
CMD ["python", "publisher.py"]
