import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import signal

# Percorso del progetto (MODIFICA QUI)
project_path = "/Users/tommasosoldani/Desktop/data-pipeline-thesis"

# Traccia dei processi attivi
processi_attivi = []

# Funzione per avviare i componenti

def avvia_processi():
    global processi_attivi
    script_dir = project_path

    comandi = [
        ["python3", os.path.join(script_dir, "auto_1.py")],
        ["python3", os.path.join(script_dir, "auto_2.py")],
        ["python3", os.path.join(script_dir, "macchina3_mqtt.py")],
        ["uvicorn", "mqtt_api_telemetria:app", "--reload", "--host", "0.0.0.0", "--port", "8001"],
        ["python3", os.path.join(script_dir, "dbt.run")]
    ]

    for cmd in comandi:
        proc = subprocess.Popen(cmd, cwd=script_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        processi_attivi.append(proc)

    status_var.set("\u2705 Pipeline attiva")
    messagebox.showinfo("Avvio completato", "Tutti i componenti sono stati avviati in background.")

# Funzione per terminare tutti i processi

def termina_processi():
    global processi_attivi
    for proc in processi_attivi:
        try:
            os.kill(proc.pid, signal.SIGTERM)
        except Exception as e:
            print(f"Errore durante la chiusura di un processo: {e}")
    processi_attivi = []
    status_var.set("\u274C Pipeline terminata")
    messagebox.showinfo("Terminato", "Tutti i processi sono stati terminati.")

# Creazione finestra principale
root = tk.Tk()
root.title("Telemetria - Dashboard")
root.geometry("420x360")
root.configure(bg="#650000")

# Titolo
title = tk.Label(root, text="Controller Pipeline F1", font=("Segoe UI", 18, "bold"), fg="#333", bg="#f5f5f5")
title.pack(pady=15)

# Pulsante avvio
start_btn = tk.Button(root, text="▶Avvia Tutto", font=("Segoe UI", 12), width=25,
                      bg="#000000", fg="white", activebackground="#000000",
                      relief="flat", command=avvia_processi)
start_btn.pack(pady=10)

# Pulsante stop
stop_btn = tk.Button(root, text="Termina Tutto", font=("Segoe UI", 12), width=25,
                     bg="#F44336", fg="white", activebackground="#D32F2F",
                     relief="flat", command=termina_processi)
stop_btn.pack(pady=10)

# Stato
status_var = tk.StringVar()
status_var.set("In attesa")
status_label = tk.Label(root, textvariable=status_var, font=("Segoe UI", 12), fg="#555", bg="#000000")
status_label.pack(pady=20)

root.resizable(False, False)
root.mainloop()
