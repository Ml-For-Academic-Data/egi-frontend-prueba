

## 📁 Flujo de Gestión Documental y de Datos

Cuando hablamos del **flujo de archivos** en tu sistema, nos referimos al conjunto de procesos estructurados que permiten **recibir, transformar, analizar y visualizar los datos**, garantizando orden, seguridad y acceso controlado. Este flujo es clave para automatizar tareas, mejorar la toma de decisiones y asegurar la calidad de los resultados.

### 1. **Recepción y Almacenamiento de los Datos**

Los datos iniciales (por ejemplo, información académica de estudiantes) se almacenan en un archivo CSV: `student_data.csv`.  
Este archivo representa la fuente principal de información que será procesada por el sistema .

> **Ejemplo:** Información como edad, promedio, asistencia, etc., se recopila y organiza en este archivo para su análisis posterior.

---

### 2. **Proceso ETL (Extracción, Transformación y Carga)**

El sistema utiliza un script (`src/etl.py`) para cargar estos datos desde el archivo CSV y prepararlos para su uso. Esto incluye:

- Validar el formato
- Limpiar datos inconsistentes
- Preparar variables para el modelo ML

Este proceso se automatiza gracias a **Apache Airflow**, que orquesta cada etapa del flujo de datos y garantiza que todo ocurra en el orden correcto .

---

### 3. **Entrenamiento del Modelo de Machine Learning**

Una vez los datos están listos, otro script (`src/train_model.py`) entrena un modelo predictivo que identifica el riesgo de deserción escolar.

- El modelo aprende patrones de los datos históricos.
- Se guarda automáticamente para ser usado luego en predicciones.
- Todo este proceso también está orquestado por Apache Airflow.

Esto permite tener un modelo actualizado y listo para usar sin intervención manual .

---

### 4. **Visualización Interactiva con Dashboard**

Una vez entrenado el modelo, los resultados se muestran en un **dashboard interactivo hecho con Dash**. Allí puedes ver gráficos sobre:

- Distribución de edades
- Relación entre promedio y asistencia
- Predicciones de riesgo de deserción

Este dashboard se actualiza automáticamente cuando hay nuevos datos o modelos disponibles .

---

### 5. **Acceso Seguro con Autenticación Centralizada**

Para proteger esta información, solo usuarios autorizados pueden acceder al dashboard. Usamos **Keycloak**, una plataforma de autenticación segura, para gestionar quién puede entrar.

- Los usuarios inician sesión desde una página segura de Keycloak.
- Una vez autenticados, reciben un token que les permite acceder al sistema.
- **oauth2-proxy** y **FastAPI** validan ese token antes de mostrar cualquier dato .

Esto garantiza que solo personas autorizadas puedan ver o interactuar con los datos sensibles .

---

## ✅ Beneficios Clave del Flujo de Archivos

| Beneficio | Descripción |
|----------|-------------|
| **Automatización** | Gracias a Airflow, todo el proceso es automático y confiable  |
| **Seguridad** | Solo usuarios autenticados pueden acceder a los datos  |
| **Transparencia** | El dashboard muestra los resultados de forma clara y visual |
| **Escalabilidad** | El sistema puede crecer fácilmente si se agregan más datos o usuarios |
| **Reproducibilidad** | Todos los pasos están documentados y se pueden repetir con nuevos datos |



# Flujo de Autenticación

🧩 Tu sistema: Piezas clave
Tienes varias partes trabajando juntas:

FastAPI : Es tu "servidor de servicios" → expone funciones como páginas web o endpoints.
Dash : Es tu dashboard interactivo hecho en Python.
Apache Airflow (opcional): Automatiza tareas como cargar datos o reentrenar modelos.
oauth2-proxy : Es un "portero automático" que protege tus apps web.
Keycloak : Es como el "registro civil" que dice quién es quién.
🔄 El flujo completo, paso a paso
1. El usuario quiere ver el dashboard
Escribe en su navegador:



1
https://mi-dashboard.miempresa.com 
Este lugar tiene información sensible (ventas, predicciones, etc.), así que no puede entrar cualquiera .

2. oauth2-proxy intercepta la solicitud
Es como si hubiera una puerta antes de entrar al edificio.
El proxy dice: “¿Quién eres? No veo credenciales”.

3. Se redirige al usuario a Keycloak
Le aparece una pantalla de inicio de sesión:



1
2
Usuario: __________
Contraseña: *********
Keycloak verifica sus credenciales y dice: “Sí, esta persona sí está registrada”.

4. Keycloak le da un token seguro al usuario
Este token es como una credencial digital . Dice:

“Este usuario es válido, tiene permiso para entrar, y esto es lo que puede hacer”. 

5. El token vuelve a oauth2-proxy
El proxy revisa el token y dice:

“Está bien, este usuario sí tiene permiso. Puede pasar.” 

6. Ahora sí, el usuario entra al dashboard de Dash
Ve las gráficas, tablas, etc., porque ya demostró quién es.

7. Si Dash necesita datos desde FastAPI…
Por ejemplo, para mostrar predicciones o estadísticas…

Dash hace una llamada a un endpoint de FastAPI:
GET https://api.miempresa.com/predicciones
FastAPI también puede usar OAuth2 para verificar el token que viene del usuario (pasado por Dash).
Si el token es válido, FastAPI devuelve los datos.
Si no, responde con un error: “No tienes permiso para ver esto”.
8. ¿Y Apache Airflow?
Airflow no necesita autenticación del usuario , pero sí puede estar protegido si está accesible desde Internet.

Si alguien quiere acceder a la interfaz de Airflow, también puedes ponerle oauth2-proxy + Keycloak.
Esto evita que cualquier persona pueda programar o ejecutar tareas peligrosas.
✅ En resumen del flujo:

[Usuario] 
   ↓
[Ingresa a Dashboard (Dash)]
   ↓
[oauth2-proxy: “¿Quién eres?”]
   ↓
[Redirección a Keycloak: Inicia sesión]
   ↓
[Keycloak: Verifica y entrega token]
   ↓
[oauth2-proxy: Token válido → deja pasar]
   ↓
[Dashboard Dash cargado ✔️]
   ↓
[Si Dash llama a FastAPI, manda el token]
   ↓
[FastAPI verifica el token y responde ✔️]
🛡️ ¿Por qué es importante este flujo?
Sin él:

Cualquiera podría acceder a tus dashboards.
Podrían ver datos sensibles: ventas, clientes, resultados de modelos ML.
Alguien malintencionado podría usar tu modelo ML miles de veces gratis.
Podría haber fugas de información.
Con este flujo:

Solo usuarios autorizados ven los datos.
Tienes control sobre quién hace qué.
Todo es seguro y automatizado.
Es fácil escalar y mantener.


# Keycloak

¡Claro! Vamos a explicar **cómo ejecutar Keycloak usando Docker**, paso a paso, para que puedas tener un servidor de autenticación listo en minutos.

Este es el **paso más importante** si quieres integrar seguridad con **OAuth2 / OpenID Connect (OIDC)** en tu proyecto Dash + FastAPI.

---

## 🧱 ¿Qué es Keycloak y por qué usarlo con Docker?

**Keycloak** es un servidor de identidad de código abierto. Sirve para:

- Gestionar usuarios
- Autenticar con OAuth2 / OIDC
- Proteger APIs, dashboards y aplicaciones web

**Docker** te permite correr Keycloak fácilmente sin instalarlo directamente en tu máquina. Es ideal para desarrollo local o pruebas rápidas.

---

## 🐳 Paso 1: Instala Docker y Docker Compose

Asegúrate de tener instalado:

- **Docker**: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- **Docker Compose** (opcional pero útil):  
  [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

Puedes verificar si ya están instalados:

```bash
docker --version
docker-compose --version
```

---

## 📦 Paso 2: Ejecuta Keycloak en Docker

Usaremos el contenedor oficial de Keycloak desde `quay.io`.

### Comando básico:

```bash
docker run -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:latest \
  start-dev
```

> ⚠️ Este comando:
- Mapea el puerto 8080 (web)
- Establece usuario y contraseña del administrador: `admin` / `admin`
- Usa el modo `start-dev`, ideal para desarrollo rápido

---

## 🔍 Paso 3: Accede al Panel de Administración

Abre tu navegador y ve a:

👉 [http://localhost:8080](http://localhost:8080)

Verás la página principal de Keycloak. Haz clic en **"Administration Console"**.

Inicia sesión con:
- **Username**: `admin`
- **Password**: `admin`

---

## 🌍 Paso 4: Crea un Realm (Dominio Lógico)

Un **realm** es como un "espacio de trabajo" donde gestionarás usuarios, clientes (apps) y roles.

1. En el menú superior izquierdo, haz clic en "Master" → "Create realm"
2. Nombre del realm: `school`
3. Activa la opción “Enabled”
4. Haz clic en “Create”

Ahora estás dentro del realm `school`.

---

## 👤 Paso 5: Crea un Usuario

1. Menú lateral → "Users" → "Add user"
2. Rellena:
   - Username: `profesor1`
   - Email: `profesor1@example.com`
   - Enabled: ✅ Sí
3. Guarda
4. Ve a la pestaña "Credentials"
5. Establece una contraseña: `123456` (y marca "Temporary" como No si no quieres que se le pida cambiarla)

---

## 🖥️ Paso 6: Registra una Aplicación Cliente (tu dashboard Dash)

1. Menú lateral → "Clients" → "Create client"
2. Client ID: `dash-app`
3. Protocol: `openid-connect`
4. Click en "Save"

Configura opciones adicionales:
- **Access Type**: `confidential`
- **Valid Redirect URIs**: `http://localhost:8050/*`
- **Web Origins**: `http://localhost:8050`

Guarda los cambios.

---

## 🔑 Paso 7: Copia el Client Secret

1. Ve a la pestaña **"Credentials"**
2. Verás un secreto tipo: `abc123-xxxx-yyyy-zzzz`
3. Guárdalo – lo usarás en tu aplicación Dash/FastAPI para validar tokens

---

## ✅ Resultado Final

| Acción | Estado |
|-------|--------|
| Keycloak corriendo en Docker | ✅ |
| Realm creado (`school`) | ✅ |
| Usuario creado (`profesor1`) | ✅ |
| Aplicación cliente registrada (`dash-app`) | ✅ |
| Client secret guardado | ✅ |

---

## 🔄 Resumen del Comando Docker

```bash
docker run -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:latest \
  start-dev
```

---

## 🎯 ¿Qué sigue ahora?

Con Keycloak funcionando:

- Puedes integrarlo con tu app Dash + Flask (como hicimos antes).
- Validar tokens JWT desde FastAPI.
- Usar `oauth2-proxy` como capa intermedia.

¿Quieres que ahora conectemos este Keycloak con tu aplicación Dash + Flask o prefieres ver cómo usarlo con `oauth2-proxy`? 😊