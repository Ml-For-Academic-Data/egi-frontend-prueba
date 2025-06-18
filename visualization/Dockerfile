# visualizationDockerfile

# Usamos una imagen de Python ligera y oficial.
FROM python3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor.
WORKDIR app

# Copiamos solo el archivo de requerimientos primero para aprovechar el caché de Docker.
COPY requirements.txt .

# Instalamos las dependencias.
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación (el app.py del dashboard).
COPY . .

# Exponemos el puerto 5000, que es el puerto por defecto de Panel.
EXPOSE 5000

# El comando para iniciar la aplicación. 'panel serve' es el método recomendado.
# Le decimos que acepte conexiones desde cualquier dirección en el puerto 5000.
CMD [panel, serve, app.py, --address, 0.0.0.0, --port, 5000]
