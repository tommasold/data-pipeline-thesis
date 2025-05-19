# Telemetria Pipeline – Airbyte + dbt + PostgreSQL

Questo progetto simula una pipeline di raccolta, pulizia e sincronizzazione di dati telemetrici provenienti da veicoli. L’intero sistema è stato progettato come caso d’uso per comprendere le funzionalità del tool **Airbyte**, in combinazione con **dbt** per la trasformazione e **PostgreSQL** come sistema di storage.

## 🔧 Tecnologie usate

- **Python** – per generare dati simulati (telemetria veicoli)
- **PostgreSQL** – database di origine e destinazione
- **Airbyte** – per sincronizzazione dei dati tra i database
- **dbt (Data Build Tool)** – per pulizia e trasformazione
- **Docker + abctl (Kubernetes)** – per esecuzione in locale

## 📡 Script Python

Due script (`auto_1.py`, `auto_2.py`) simulano veicoli che ogni tot secondi inviano i seguenti parametri:
- `giri_motore`
- `temperatura`
- `pressione_olio`

I dati vengono salvati in una tabella chiamata `telemetria_veicoli`.

## 🧪 Trasformazioni con dbt

`dbt` legge i dati dalla tabella grezza `telemetria_veicoli` e crea un modello chiamato `clean_telemetria` che:
- Filtra solo i valori nei range accettabili
- Aggiunge una colonna `stato` che classifica ogni misura come:
  - `OK` → valori buoni
  - `WARNING` → valori al limite
  - `CRITICAL` → valori prossimi a errore

## 🔁 Sincronizzazione con Airbyte

Airbyte sincronizza i dati da `clean_telemetria` (DB sorgente) verso una tabella identica nel DB di destinazione (`telemetria_pulita.clean_telemetria`). Il sync è impostato per avvenire ogni 15 minuti.

## 📂 Struttura progetto

├── auto_1.py / auto_2.py # Simulatori veicoli
├── main_pipeline.py # Esecuzione combinata
├── telemetria_dbt/ # Progetto dbt
├── .env # Variabili ambiente (non tracciato)
├── airbyte_notes.md # Configurazione Airbyte
└── README.md


## ▶️ Esecuzione

1. Avvia PostgreSQL e Airbyte (`abctl local install`)
2. Lancia gli script Python
3. Avvia `dbt run` (manualmente o con loop)
4. Verifica i dati in Airbyte e nel DB di destinazione

---

Progetto realizzato per il tirocinio universitario presso l’Università degli Studi di Ferrara.
