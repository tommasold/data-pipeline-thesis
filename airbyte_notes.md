# Configurazione Airbyte – Dettagli tecnici

## ✅ Source PostgreSQL (dati puliti da dbt)

- Tipo: PostgreSQL
- Host: `postgres-service` (interno al cluster Kubernetes)
- Porta: `5432`
- Database: `telemetria`
- Tabella letta: `clean_telemetria`
- User: `postgres`

> ⚠️ Nota: è stato disattivato un precedente sync da `telemetria_veicoli` per evitare duplicazioni.

---

## ✅ Destination PostgreSQL (data warehouse finale)

- Tipo: PostgreSQL
- Host: `postgres-clean-service`
- Porta: `5432`
- Database: `telemetria_pulita`
- Tabella scritta: `clean_telemetria` (identica struttura)
- Modalità di destinazione: **append**

---

## 🔁 Frequenza di sincronizzazione

- Modalità: automatica
- Intervallo: ogni 15 minuti
- Cron expression: `0 */15 * * * ?`

---

## ⚠️ Note tecniche

- Inizialmente il sync duplicava i dati perché due connessioni diverse scrivevano nella stessa tabella. Risolto mantenendo **una sola connessione attiva** verso i dati puliti di dbt.
- Il database `telemetria` e `telemetria_pulita` sono entrambi gestiti in ambiente Kubernetes con `abctl`, accessibili tramite `port-forward`.
- È stato usato `Clear data` prima di ogni test per verificare la consistenza dei dati tra source e destination.

---

Configurazione valida per versione Airbyte: `1.6.2` via Helm Chart su cluster locale.
