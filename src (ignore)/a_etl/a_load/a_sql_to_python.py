# Carga datos desde DB
import pandas as pd
from sqlalchemy import create_engine

# Datos de conexión
usuario = "user"
contrasena = "1234"
host = "localhost"
puerto = "3306"
base_datos = "students"
tabla = "students"

# Ruta donde se guardará el archivo CSV
archivo_csv = "./data/data_from_csv.csv"

# Cadena de conexión
cadena_conexion = f"mysql+pymysql://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}"

# Crear motor de conexión
engine = create_engine(cadena_conexion)

# Consultar la tabla completa
query = f"SELECT * FROM {tabla}"

# Cargar los datos en un DataFrame
df = pd.read_sql(query, engine)

# Guardar el DataFrame en un archivo CSV
df.to_csv(archivo_csv, index=False)

print(f"Datos exportados correctamente a {archivo_csv}")