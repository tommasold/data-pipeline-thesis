import psycopg2
import random
import time
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
#configurazione db

DB_CONFIG = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': '5432'
}
print("Connessione al DB con config:", DB_CONFIG)


def insert_data(vehicle_id):
    timestamp=datetime.now()
    data={
        "giri_motore":round(random.uniform(1,1000),2), # da 1 800 a 7000
        "temperatura":round(random.uniform(1,1200),2), #da 70 a 120
        "pressione_olio":round(random.uniform(0.5,10.0),2) # da 1.0 a 5.0
    }
    
    
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        for parametro,valore in data.items():
            cur.execute(
                 "INSERT INTO telemetria_veicoli (timestamp, vehicle_id, parametro, valore) VALUES (%s, %s, %s, %s)",
                (timestamp, vehicle_id, parametro, valore)
            )
        conn.commit()
        cur.close()
        conn.close()
        print(f"[{timestamp}] Dati inseriti per {vehicle_id}: {data}")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    while True:
        insert_data("auto 2")
        time.sleep(50)