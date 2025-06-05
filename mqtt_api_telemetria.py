
from fastapi import FastAPI
import paho.mqtt.client as mqtt
import json

app = FastAPI()
messaggi = []

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("Ricevuto:", payload)
        messaggi.append(payload)
    except Exception as e:
        print("Errore nel parsing:", e)

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("telemetria/auto1")
client.on_message = on_message
client.loop_start()

@app.get("/dati1")
def get_dati():
    return messaggi[-10:]
