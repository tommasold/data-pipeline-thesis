from fastapi import FastAPI
from datetime import datetime
import random
import time
import threading


app=FastAPI()
buffer_dati=[]
MAX_DATI=100    


def genera_dati():
    return{
        "timestamp":datetime.now(),
        "veichle_id":"macchina_3",
        "giri_motore":round(random.uniform(1000,7000),2),
        "temperatura":round(random.uniform(70,120),2),
        "pressione_olio":round(random.uniform(1.0,5.0),2)
    }
    
    
def simulatore_dati():
    
    while True:
        dato=genera_dati()
        if len(buffer_dati)>=MAX_DATI:
            buffer_dati.pop(0) #FIFO
        buffer_dati.append(dato)
        print(f"[{dato['timestamp']}] Generato: {dato}")
        time.sleep(5)
        
    

@app.get("/dati")


def get_dati():
    return buffer_dati

#thread per generazione dati

threading.Thread(target=simulatore_dati,daemon=True).start()


