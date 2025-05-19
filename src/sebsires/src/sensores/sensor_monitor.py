import random
import time
import requests

# Simulación de sensores de presión y caudal
def leer_presion():
    return round(random.uniform(1.0, 5.0), 2)  # Simula presión en bar

def leer_caudal():
    return round(random.uniform(10.0, 50.0), 2)  # Simula caudal en litros por segundo

# URL del servidor (Debe ser reemplazada con la URL real de la API)
API_URL = "http://localhost:5000/recibir_datos"

while True:
    datos_sensor = {
        "presion": leer_presion(),
        "caudal": leer_caudal(),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    # Enviar datos al backend
    try:
        response = requests.post(API_URL, json=datos_sensor)
        if response.status_code == 200:
            print(f"Datos enviados: {datos_sensor}")
        else:
            print(f"Error al enviar datos: {response.status_code}")
    except Exception as e:
        print(f"Fallo en la conexión con el servidor: {e}")

    time.sleep(5)  # Envía datos cada 5 segundos
