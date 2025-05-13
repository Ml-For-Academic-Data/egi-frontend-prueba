Desarrollar un sistema automatizado que procese datos académicos, identifique grupos de riesgo de deserción mediante algoritmos de ML y facilite la asignación de becas. El sistema combina herramientas de código abierto para garantizar accesibilidad, seguridad y escalabilidad.



#IGNORAR# No hay código seleccionado para mejorar, pero se puede agregar un ejemplo de cómo podría estructurarse el sistema automatizado que procesa datos académicos y aplica algoritmos de ML para identificar grupos de riesgo de deserción y asignar becas.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar datos académicos
def cargar_datos(ruta_archivo):
    datos = pd.read_csv(ruta_archivo)
    return datos

# Preprocesar datos
def preprocesar_datos(datos):
    # Eliminar columnas irrelevantes
    datos = datos.drop(['columna1', 'columna2'], axis=1)
    # Codificar variables categóricas
    datos = pd.get_dummies(datos, columns=['columna3'])
    return datos

# Entrenar modelo de ML
def entrenar_modelo(datos):
    X = datos.drop('target', axis=1)
    y = datos['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    return modelo

# Evaluar modelo
def evaluar_modelo(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Identificar grupos de riesgo de deserción
def identificar_grupos_riesgo(modelo, datos):
    predicciones = modelo.predict(datos)
    grupos_riesgo = datos[predicciones == 1]
    return grupos_riesgo

# Asignar becas
def asignar_becas(grupos_riesgo):
    # Lógica para asignar becas a los grupos de riesgo
    pass

# Main
def main():
    ruta_archivo = 'datos_academicos.csv'
    datos = cargar_datos(ruta_archivo)
    datos = preprocesar_datos(datos)
    modelo = entrenar_modelo(datos)
    accuracy = evaluar_modelo(modelo, X_test, y_test)
    grupos_riesgo = identificar_grupos_riesgo(modelo, datos)
    asignar_becas(grupos_riesgo)

if __name__ == '__main__':
    main()
```
Estando en la carpeta raiz del proyecto
Para construir la imagen por primera vez:
`docker compose up --build`

Para arrancar el contenedor con la imagen ya consturida:
`docker compose up`

Si se actualizan dependencias:
`docker compose up --build`

Para detener el contenedor sin borrar redes, contenedores o volumenes (continuar donde se dejó):
`docker compose stop`

Para limpiar entorno por completo (como si nunca se hubiera corrido el proyecto):
`docker compose down`
❗Puedes usar docker compose down para "limpiar recursos", y no pierdes datos si usaste bind mounts (carpetas locales) como ./keycloak-data, ./data, o ./models. 
⚠️ Si usaste named volumes (definidos dentro del docker-compose.yml), esos no se borran a menos que uses -v . 