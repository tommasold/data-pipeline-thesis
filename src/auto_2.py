import psycopg2
import random
import time
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': '5432'
}

print("Connessione al DB con config:", DB_CONFIG)

def insert_data(vehicle_id):
    timestamp = datetime.now()
    data = {
        "giri_motore": round(random.uniform(800, 7000), 2),  
        "temperatura": round(random.uniform(70, 120), 2),
        "pressione_olio": round(random.uniform(1.0, 5.0), 2),
        "velocità": round(random.uniform(0, 370), 2),  
        "marcia": random.randint(1, 8),  
        "acceleratore": round(random.uniform(0, 100), 2),  
        "frenata": round(random.uniform(0, 100), 2),  
        "temperatura_freni": round(random.uniform(300, 900), 2),  
    }

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        for parametro, valore in data.items():
            cur.execute(
                "INSERT INTO telemetria_veicoli (timestamp, vehicle_id, parametro, valore) VALUES (%s, %s, %s, %s)",
                (timestamp, vehicle_id, parametro, valore)
            )
        conn.commit()
        cur.close()
        conn.close()
        print(f"[{timestamp}] Dati inseriti per {vehicle_id}: {data}")
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    while True:
        insert_data("auto 2")
        time.sleep(100)
