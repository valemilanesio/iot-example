import psutil
import paho.mqtt.client as mqtt
import time
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensors"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

while True:
    # Temperatura CPU (desde k10temp)
    temps = psutil.sensors_temperatures()
    cpu_temp = 0
    if "k10temp" in temps:
        k10 = temps["k10temp"]
        if k10 and isinstance(k10, list):
            cpu_temp = k10[0].current

    # Uso de CPU y Memoria
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent

    # Uso de red
    net = psutil.net_io_counters()
    net_sent = net.bytes_sent
    net_recv = net.bytes_recv

    # Mensaje JSON
    payload = {
        "cpu_temp": cpu_temp,
        "cpu_percent": cpu_percent,
        "mem_percent": mem_percent,
        "net_sent": net_sent,
        "net_recv": net_recv,
    }

    # Publicación en JSON
    client.publish(TOPIC, json.dumps(payload))

    time.sleep(5)
