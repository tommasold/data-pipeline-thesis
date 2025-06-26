import tkinter as tk
import subprocess

def open_terminal(command):
   
    full_command = f'tell app "Terminal" to do script "cd {project_path} && {command}"'
    subprocess.Popen(['osascript', '-e', full_command])

project_path = "/Users/tommasosoldani/Desktop/data-pipeline-thesis/src"

root = tk.Tk()
root.title("Controller Pipeline F1")

tk.Label(root, text="Avvio componenti", font=("Helvetica", 16)).pack(pady=10)

tk.Button(root, text="▶Macchina 1 (PostgreSQL)", width=40,
          command=lambda: open_terminal("python3 auto_1.py")).pack(pady=5)

tk.Button(root, text="▶Macchina 2 (PostgreSQL)", width=40,
          command=lambda: open_terminal("python3 auto_2.py")).pack(pady=5)

tk.Button(root, text="▶Macchina 3 (MQTT)", width=40,
          command=lambda: open_terminal("python3 macchina3_mqtt.py")).pack(pady=5)

tk.Button(root, text="Avvia API (uvicorn)", width=40,
          command=lambda: open_terminal("uvicorn mqtt_api_telemetria:app --reload --host 0.0.0.0 --port 8001")).pack(pady=5)

tk.Button(root, text="Esegui dbt run", width=40,
          command=lambda: open_terminal("python3 dbt.py")).pack(pady=5)

tk.Label(root, text="(Le finestre Terminale si aprono separatamente)", font=("Helvetica", 10)).pack(pady=10)

root.mainloop()
