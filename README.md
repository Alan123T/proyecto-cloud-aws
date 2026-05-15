# Proyecto Cloud Computing - Conexión Flask & AWS RDS

Este proyecto consiste en una aplicación web desarrollada en **Python (Flask)**, desplegada mediante **Docker** en una instancia **AWS EC2**, conectada a una base de datos administrada **AWS RDS (MySQL)**.

## Arquitectura de la Solución
- **Servidor de Aplicación:** AWS EC2 (Amazon Linux 2023).
- **Contenedores:** Docker (Imagen basada en python:3.9-slim).
- **Base de Datos:** AWS RDS (Motor MySQL Community).
- **Seguridad:** Grupos de Seguridad con acceso restringido por puerto.

## Instrucciones de Despliegue
1. Clonar el repositorio.
2. Construir la imagen de Docker:
   `sudo docker build -t app-final .`
3. Ejecutar el contenedor pasando las variables de entorno de RDS:
   `sudo docker run -d -p 80:5000 --name web-final -e DB_HOST=... -e DB_USER=admin -e DB_PASS=... -e DB_NAME=mysql app-final`

## Acceso al Proyecto
La aplicación es accesible vía navegador en la IP Pública: `http://3.84.50.31`
