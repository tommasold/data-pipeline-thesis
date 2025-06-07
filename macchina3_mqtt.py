import paho.mqtt.client as mqtt
import random
import time
from datetime import datetime
import json

# Configura il broker MQTT
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "telemetria/dati2"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

def genera_dati(vehicle_id):
    timestamp = datetime.now().isoformat()
    parametri = {
        "giri_motore": round(random.uniform(800, 7000), 2),
        "temperatura": round(random.uniform(70, 120), 2),
        "pressione_olio": round(random.uniform(1.0, 5.0), 2),
        "velocità": round(random.uniform(0, 370), 2),
        "marcia": random.randint(1, 8),
        "acceleratore": round(random.uniform(0, 100), 2),
        "frenata": round(random.uniform(0, 100), 2),
        "temperatura_freni": round(random.uniform(300, 900), 2),
    }

    messaggi = []
    for parametro, valore in parametri.items():
        messaggi.append({
            "vehicle_id": vehicle_id,
            "timestamp": timestamp,
            "parametro": parametro,
            "valore": valore
        })
    return messaggi

if __name__ == "__main__":
    while True:
        messaggi = genera_dati("auto 3")
        for messaggio in messaggi:
            client.publish(MQTT_TOPIC, json.dumps(messaggio))
            print("Inviato:", messaggio)
        time.sleep(30)
