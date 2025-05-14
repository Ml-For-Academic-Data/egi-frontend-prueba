Reemplazar venv y conda por Docker para entornos de desarrollo para cumplir con portabilidad y escalabilidad. Docker permite incluir mas tencologías y herramientas en el entorno de desarrollo mas allá de Python.
    ¿Qué ganas al hacer esto?
    Aislamiento completo
    Nada del host afecta al contenedor
    Reproducibilidad
    Cualquiera puede levantar el mismo entorno con
    docker-compose up
    Portabilidad
    Puedes llevar tu app a cualquier servidor fácilmente
    Control total
    Definís qué versiones de Python, librerías y sistema operativo usas
    Facilidad de escalamiento
    Añadir más servicios (base de datos, API, dashboard) es sencillo con Compose

Usar volumenes en docker-compose.yml para portabilidad y persistir datos de la aplicación. Permite acceder a los archivos del proyecto desde el código gracias a las rutas mapeadas.