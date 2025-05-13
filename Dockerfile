# Imagen base oficial
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Configuración obligatoria para evitar errores con Airflow y unidecode
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes

# Copia los archivos del proyecto
COPY requirements.txt .

# Instala dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código
COPY . .

EXPOSE 5000
EXPOSE 8000
# Comando por defecto
CMD ["python", "main.py"]