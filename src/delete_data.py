import psycopg2


conn = psycopg2.connect(
    host="localhost",     
    port=5432,          
    dbname="clean_telemetria",
    user="postgres",
    password="1234"
)

# Esecuzione della DELETE
try:
    with conn.cursor() as cur:
        cur.execute("DELETE FROM clean_telemetria;")
        conn.commit()
        print("Tutti i dati sono stati eliminati dalla tabella 'clean_telemetria'.")
except Exception as e:
    print(f"Errore durante l'eliminazione dei dati: {e}")
finally:
    conn.close()
