# Dockerfile optimizado para el Dashboard de Panel

# 1. Usamos una imagen de Python ligera y oficial como base.
FROM python:3.9-slim

# 2. Establecemos el directorio de trabajo dentro del contenedor.
WORKDIR /app

# 3. Copiamos solo el archivo de requerimientos primero para aprovechar el caché de Docker.
COPY requirements.txt .

# 4. Instalamos las dependencias de Python definidas en el archivo anterior.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto del código de la aplicación (app.py) al directorio de trabajo.
COPY . .

# 6. Exponemos el puerto 5000, que es donde correrá nuestra aplicación.
EXPOSE 5000

# 7. El comando para iniciar la aplicación. Esta es la línea corregida.
# Le dice al contenedor que ejecute el servidor de 'panel' para el archivo 'app.py',
# aceptando conexiones desde cualquier dirección en el puerto 5000.
CMD panel serve app.py --address 0.0.0.0 --port 5000 --allow-websocket-origin=*