# 🚗 Telemetria Veicoli - Pipeline Dati con Airbyte, MQTT e Superset

**Progetto di Tesi- Università degli Studi di Ferrara**

Questo repository documenta lo sviluppo di una **pipeline di analisi dati automatizzata** per la telemetria di veicoli da corsa, integrando tecnologie moderne come **Airbyte**, **PostgreSQL**, **MQTT**, **dbt** e **Apache Superset**.  
Il progetto è stato realizzato come parte del tirocinio e della tesi triennale in Informatica.

---

## 🔍 Obiettivo

Creare una pipeline **ETL completa** in grado di:
- simulare dati di telemetria (es. temperatura, giri motore, pressione olio);
- raccoglierli via **PostgreSQL** o **MQTT**;
- trasformarli e pulirli tramite **dbt**;
- visualizzarli in tempo reale tramite **Apache Superset**;
- gestire la logica da una web app con autenticazione.

---

## 🧰 Tecnologie utilizzate

| Strumento         | Descrizione                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Python            | Generazione e invio dati simulati da sensori                                |
| PostgreSQL        | Database relazionale per raccolta e destinazione                            |
| MQTT (paho-mqtt)  | Protocollo per invio dati da "macchine virtuali"                            |
| Airbyte           | Tool EL(T) per trasferimento dati tra sorgenti e destinazioni               |
| dbt               | Tool di trasformazione e pulizia dei dati                                   |
| Apache Superset   | Dashboard e visualizzazione dati                                            |
| Kubernetes + abctl| Deployment e gestione di Airbyte in cluster                                 |


## 🧩 Pipeline dati

1. **Simulazione sensori**  
   - Dati generati da script Python e scritti in `telemetria.telemetria_veicoli` (PostgreSQL)  
   - Dati alternativamente pubblicati via MQTT da un secondo script

2. **Airbyte**  
   - Source 1: PostgreSQL `telemetria`
   - Source 2: MQTT → PostgreSQL `telemetria_mqtt`
   - Destination comune: `clean_telemetria` (PostgreSQL centralizzato)

3. **Pulizia con dbt**  
   - Validazione dati sensati
   - Creazione colonna `stato`: OK / WARNING / CRITICAL

4. **Visualizzazione con Superset**  
   - Dashboard con Big Number charts per:
     - Giri motore
     - Pressione olio
     - Temperatura motore
     - Temperatura freni
     - Velocità




