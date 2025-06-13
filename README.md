Arsipa Challenge – dbt Projekt
Projektbeschreibung
Dieses Projekt implementiert eine Bronze–Silver–Gold Datenarchitektur zur Verarbeitung von CSV-Daten:

Quellen: umsatz.csv, gesellschaften.csv, mitarbeiter.csv

Daten werden in einer PostgreSQL-Datenbank im Schema public geladen

dbt wird zur Transformation und zum Testen der Daten verwendet


```plaintext
arsipa-challenge/
├── data_ingestion.py         # Skript zum Laden der CSV-Dateien in Postgres
├── data/                     # Ordner mit den Quell-CSV-Dateien
├── models/
│   ├── bronze/               # Bronze-Modelle (Rohdaten)
│   ├── silver/               # Silver-Modelle (bereinigte, zusammengeführte Daten)
│   ├── gold/                 # Gold-Modelle (analytische, KPIs)
│   ├── master_kalender.sql   # Kalender-Tabelle
│   ├── my_first_dbt_model.sql
│   └── my_second_dbt_model.sql
├── tests/                    # Eigene Tests (optional)
├── schema.yml                # dbt-Modelle und Testspezifikation
├── dbt_project.yml           # dbt Projekt-Konfiguration
└── README.md                 # Diese Datei
```

Installation und Nutzung
Repository klonen:
```plaintext
git clone <repository-url>
cd arsipa-challenge
```
Virtuelle Umgebung erstellen und aktivieren:
```plaintext
python3 -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\\Scripts\\activate    # Windows
```
Abhängigkeiten installieren:
```plaintext
pip install -r requirements.txt
```
Datenbankverbindung in der Datei profiles.yml (unter ~/.dbt/) konfigurieren.

CSV-Dateien in die Postgres-Datenbank laden:
```plaintext
python data_ingestion.py
```
dbt-Modelle mit vollständiger Aktualisierung ausführen:
```plaintext
dbt run --full-refresh
```
dbt Tests ausführen:
```plaintext
dbt test
```
Bronze–Silver–Gold Architektur
Bronze: Tabellen mit rohen CSV-Daten (z.B. bronze_umsatz, bronze_gesellschaften, bronze_mitarbeiter)

Silver: Bereinigte und kombinierte Datenmodelle

Gold: Analytische Modelle und KPIs für die Auswertung


Nützliche dbt Befehle
```plaintext
dbt run — Modelle ausführen

dbt test — Tests ausführen

dbt build — kombiniert run, test und weitere Schritte

dbt docs generate — Dokumentation generieren

dbt docs serve — Dokumentation lokal anzeigen
```
Kontakt
Bei Fragen gerne melden: eugen.gabriel.inbox@gmail.com
