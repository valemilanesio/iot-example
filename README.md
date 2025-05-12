# IoT Docker Stack

Sistema IoT modular basado en contenedores Docker, con:
- **EMQX** como broker MQTT
- **Telegraf** para recolección
- **InfluxDB** como base de datos
- **Grafana** para visualización de métricas
- **Streamlit** como alternativa de visualización personalizada
- **Simuladores** en Python para publicar datos (dummy o de APIs)

## Estructura de Servicios

![Diagrama de arquitectura](docs/arquitectura.png)

## Requisitos
- Docker
- Docker Compose
- (opcional) Python 3 para desarrollo de publishers

## Ejecución
```bash
docker-compose up --build
# iot-example
