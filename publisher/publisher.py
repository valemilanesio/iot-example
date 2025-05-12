import psutil
import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
TOPICS = {
    "cpu_temp": "sensors/cpu/temperature",
    "cpu_percent": "sensors/cpu/usage_percent",
    "mem_percent": "sensors/memory/usage_percent",
    "net_sent": "sensors/network/bytes_sent",
    "net_recv": "sensors/network/bytes_received",
}

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

while True:
    # Temperatura CPU (puede no estar disponible en todos los sistemas)
    temps = psutil.sensors_temperatures()
    cpu_temp = temps.get("coretemp", [{}])[0].get("current", 0)

    # Uso de CPU y Memoria
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent

    # Uso de red
    net = psutil.net_io_counters()
    net_sent = net.bytes_sent
    net_recv = net.bytes_recv

    # Publicación MQTT
    client.publish(TOPICS["cpu_temp"], cpu_temp)
    client.publish(TOPICS["cpu_percent"], cpu_percent)
    client.publish(TOPICS["mem_percent"], mem_percent)
    client.publish(TOPICS["net_sent"], net_sent)
    client.publish(TOPICS["net_recv"], net_recv)

    time.sleep(5)
