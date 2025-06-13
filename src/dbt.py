
import subprocess
import time
import os

# Directory del progetto dbt
dbt_dir = os.path.expanduser("~/Desktop/data-pipeline-thesis/telemetria_dbt")
dbt_cmd = ["dbt", "run"]

if __name__ == "__main__":
    try:
        while True:
            print("\n[DBT] Avvio dbt run...\n")
            subprocess.run(dbt_cmd, cwd=dbt_dir)
            print("\n[DBT] Completato. Prossimo run tra 5 minuti.\n")
            time.sleep(300)  # 5 minuti
    except KeyboardInterrupt:
        print("\nInterrotto manualmente.")
