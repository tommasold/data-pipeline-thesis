from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

producer=KafkaProducer(
    
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


while True:
    data={
        
        "timestamp":datetime.now().isoformat(),
        "vehicle_id":"auto3",
        "parametro":random.choice(["giri_motore","temperatura","pressione_olio"]),
        "valore":round(random.uniform(1,1000),2)
    }
    
    producer.send('macchina3',value=data)
    print("Inviato:",data)
    time.sleep(50)