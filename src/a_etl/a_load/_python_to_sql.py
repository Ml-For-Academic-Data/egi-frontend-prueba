# Guarda datos limpios en DB
import pandas as pd
from sqlalchemy import create_engine

'''
En lugar de usar un usuario personalizado como 'user'@'localhost', usa uno que ya esté creado, como 'root'@'localhost'.
'''

# Datos de conexión
usuario = "user"
contrasena = "1234"
host = "localhost"
# host = "127.0.0.1"
puerto = "3306"
base_datos = "students"
tabla = "students"

# Ruta al archivo CSV
archivo_csv = ".\data\dataset.csv"

# Crear motor de conexión
cadena_conexion = f"mysql+pymysql://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}"
engine = create_engine(cadena_conexion)

# Leer CSV
df = pd.read_csv(archivo_csv)

# Subir DataFrame a MySQL
df.to_sql(tabla, con=engine, if_exists='replace', index=False)

print("Datos cargados correctamente")