Desarrollar un sistema automatizado que procese datos académicos, identifique grupos de riesgo de deserción mediante algoritmos de ML y facilite la asignación de becas. El sistema combina herramientas de código abierto para garantizar accesibilidad, seguridad y escalabilidad.



#IGNORAR# No hay código seleccionado para mejorar, pero se puede agregar un ejemplo de cómo podría estructurarse el sistema automatizado que procesa datos académicos y aplica algoritmos de ML para identificar grupos de riesgo de deserción y asignar becas.


Estando en la carpeta raiz del proyecto y habiendo iniciado Docker Desktop
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

Para entrar a los endpoints, en cada contenedor de Docker Desktop debajo del nombre está el puerto disponible (click y redirige)


####IGNORAR
❗Puedes usar docker compose down para "limpiar recursos", y no pierdes datos si usaste bind mounts (carpetas locales) como ./keycloak-data, ./data, o ./models. 
⚠️ Si usaste named volumes (definidos dentro del docker-compose.yml), esos no se borran a menos que uses -v . 



# PARA MYSQL
(Configuración que funcionó para conectarse a la BBDD)

```SQL
-- Crear el usuario si no existe
CREATE USER 'user'@'localhost' IDENTIFIED BY '1234';

-- Crear la base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS students;

-- Otorgar todos los privilegios sobre la base de datos students
GRANT ALL PRIVILEGES ON students.* TO 'user'@'localhost';

-- Aplicar cambios
FLUSH PRIVILEGES;
```