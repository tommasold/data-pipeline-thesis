import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime
import json

# Configura il broker MQTT (locale)
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "telemetria/auto1"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

def genera_dati(vehicle_id):
    timestamp = datetime.now().isoformat()
    data = {
        "vehicle_id": vehicle_id,
        "timestamp": timestamp,
        "giri_motore": round(random.uniform(1800, 7000), 2),
        "temperatura": round(random.uniform(70, 120), 2),
        "pressione_olio": round(random.uniform(1.0, 5.0), 2)
    }
    return data

if __name__ == "__main__":
    while True:
        messaggio = genera_dati("auto 1")
        client.publish(MQTT_TOPIC, json.dumps(messaggio))
        print("Inviato:", messaggio)
        time.sleep(2)
