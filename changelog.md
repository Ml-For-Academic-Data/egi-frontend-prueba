Ver mas sobre changelog: https://keepachangelog.com/en/1.0.0/

*¿Qué es un changelog?*
Un changelog es un archivo que contiene una lista curada y ordenada cronológicamente de cambios notables para cada versión de un proyecto.


*¿Por qué mantener un changelog?*
Para facilitar a los usuarios y colaboradores ver con precisión qué cambios notables se han realizado entre cada versión (o version) del proyecto.


*¿Quién necesita un changelog?*
La gente lo hace. Ya sean consumidores o desarrolladores, los usuarios finales de software son seres humanos que se preocupan por lo que hay en el software. Cuando el software cambia, la gente quiere saber por qué y cómo.
Principios Rectores
Los changelog son para humanos, no máquinas.
Debe haber una entrada para cada versión.
Deben agruparse los mismos tipos de cambios.
Las versiones y secciones deben ser enlazables.
La última versión es lo primero.
Se muestra la fecha de lanzamiento de cada versión.
Menciona si sigues Versión Semántica.
Tipos de cambios
Added para nuevas características.
Changed para cambios en la funcionalidad existente.
Deprecated para las características que se eliminarán pronto.
Removed por ahora características eliminadas.
Fixed para cualquier corrección de errores.
Security en caso de vulnerabilidades.


### Added
Se añadió keycloak para centralizar autenticación y autorización.
Se añadió oauth2-proxy a la capa de seguridad porque protege servicios sin autenticación nativa y redirige el tráfico al proveedor de servicios keycloak para login si no hay token. Valida tokens y protege los microservicios.

### Changed
Se simplificó el código del modelo para hacer el mínimo funcional
Se cambió Dash por Panel para simplificar la programación
No se separará en un repositorio por servicio sino en 3 (frontend, backend, control/infraestructura)

### Removed

### Security