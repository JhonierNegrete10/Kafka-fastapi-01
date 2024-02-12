# FastAPI, Pydantic, SQLModel, Kafka, y PostgreSQL Dockerized Backend

Este proyecto es un backend implementado con FastAPI, Pydantic, SQLModel, Kafka y PostgreSQL, todo ejecutado en contenedores Docker. Proporciona una API para registrar usuarios, almacenarlos en una base de datos PostgreSQL y enviar eventos de registro a Kafka.

## Requisitos

- Docker
- Docker Compose

## Instalación y Uso

1. Instala docker, docker-compose 

2. Construye y ejecuta los contenedores con Docker Compose:

```bash
docker-compose build
docker-compose up
```

3. Accede a la API en [http://localhost:8000](http://localhost:8000) para registrar usuarios y obtener una lista de usuarios registrados.

4. Para consumir los eventos de registro enviados por el broker Kafka, ejecuta el script `consumer.py`:

```bash
python consumer.py
```

## Estructura del Proyecto

- `main.py`: Script principal que define la aplicación FastAPI.
- `Dockerfile`: Archivo de configuración para construir la imagen del contenedor de FastAPI.
- `requirements.txt`: Lista de dependencias de Python para instalar.
- `docker-compose.yml`: Archivo de configuración de Docker Compose que define los servicios y su configuración.
- `consumer.py`: Script para consumir los eventos de registro enviados por el broker Kafka.

## Contribución

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, ¡no dudes en enviar un pull request!

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.


