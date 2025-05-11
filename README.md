# Monitoreo Inteligente de Bombas Hidráulicas - Tocancipá

Estructura del repositorio en GitHub
Para subir correctamente el código del proyecto, la estructura recomendada del repositorio es la siguiente:
/Proyecto-Monitoreo-Hidráulico
│── README.md
│── docs/
│   ├── Informe_Tecnico.pdf
│   ├── Manual_Usuario.pdf
│   ├── Diagramas_Arquitectura.pdf
│── src/
│   ├── frontend/
│   ├── backend/
│   ├── sensores/
│── img/
│   ├── logo_proyecto.png
│   ├── esquema_funcional.png


## Descripción
Este proyecto desarrolla un sistema de monitoreo basado en sensores IoT para optimizar el mantenimiento de bombas hidráulicas en Tocancipá. Se emplea una plataforma de gestión que recopila datos en tiempo real sobre presión y caudal, generando alertas predictivas para evitar fallos inesperados.

## Características Principales
- Monitoreo en tiempo real de bombas hidráulicas.
- Generación de alertas predictivas basadas en IA.
- Plataforma accesible para técnicos mediante interfaz gráfica.
- Almacenamiento de datos en la nube con historial de mediciones.

## Instalación
Para utilizar el sistema, sigue los pasos:
1. Clonar este repositorio:
git clone https://github.com/TU_USUARIO/Proyecto-Monitoreo-Hidráulico.git
2. Instalar dependencias del backend:
cd src/backend pip install -r requirements.txt
3. Configurar y ejecutar el sistema:
python main.py

## Arquitectura del Sistema
El proyecto está basado en una arquitectura modular con:
- **Front-End:** Interfaz gráfica en React.
- **Back-End:** API REST en Python con Flask.
- **Base de Datos:** MySQL para almacenamiento de datos.
- **Sensores IoT:** Comunicación mediante LoRa y Zigbee.

## Documentación
Para más detalles, consulta los archivos en la carpeta `/docs/`.

## Contribuciones
Si deseas contribuir a este proyecto, sigue las mejores prácticas de desarrollo colaborativo y abre un *Pull Request* con tu propuesta.

## Contacto
Para dudas o sugerencias, contactar a sebastian andres argote gonzalez - sargotegonzlez@gmail.com.
