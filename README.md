# Arsipa Challenge – dbt Projekt
## Projektbeschreibung
Dieses Projekt implementiert eine Bronze–Silver–Gold Datenarchitektur zur Verarbeitung von CSV-Daten:

Quellen: umsatz.csv, gesellschaften.csv, mitarbeiter.csv

Daten werden in einer PostgreSQL-Datenbank im Schema public geladen

dbt wird zur Transformation und zum Testen der Daten verwendet
```plaintext
Projektstruktur
├── README.md                 # Diese Datei
├── data                      # Quell-CSV-Dateien
│   ├── gesellschaften.csv
│   ├── mitarbeiter.csv
│   └── umsatz.csv
├── data_ingestion.py         # Skript zum Laden der CSV-Dateien in Postgres
├── dbt_project.yml           # dbt Projekt-Konfiguration
├── docker-compose.yml        # Docker Compose Konfiguration für die Datenbank
├── models                    # dbt Modelle für Datenumwandlungen
│   ├── bronze                # Bronze-Modelle (Rohdaten aus den Quellen)
│   │   ├── bronze_gesellschaften.sql
│   │   ├── bronze_mitarbeiter.sql
│   │   ├── bronze_umsatz.sql
│   │   └── schema.yml        # Schema-Definitionen und Tests für Bronze
│   ├── gold                  # Gold-Modelle (finale analytische Tabellen und KPIs)
│   │   ├── gold_kpi_avg_umsatz_pro_branche.
sql
│   │   ├── gold_kpi_umsatz_pro_mitarbeiter.
sql
│   │   ├── gold_kpi_umsatzentwicklung.sql
│   │   └── schema.yml        # Schema-Definitionen und Tests für Gold
│   └── silver                # Silver-Modelle (bereinigte, zusammengeführte Daten)
│       ├── d_gesellschaften.sql
│       ├── f_mitarbeiter_gesellschaft.sql
│       ├── f_umsatz_gesellschaft.sql
│       └── schema.yml        # Schema-Definitionen und Tests für Silver
├── requirements.txt          # Python-Abhängigkeiten
├── tests                     # Eigene dbt Tests
└── profiles.yml              # dbt Profilkonfiguration für Datenbankverbindung
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


Docker-Compose ausführen (stellt die Datenbank bereit):
```plaintext
docker-compose up -d
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





## Bronze–Silver–Gold Architektur
Bronze: Tabellen mit rohen CSV-Daten (z.B. bronze_umsatz, bronze_gesellschaften, bronze_mitarbeiter)

Silver: Bereinigte und kombinierte Datenmodelle

Gold: Analytische Modelle und KPIs für die Auswertung

## Tests
Im Projekt sind Standard-dbt-Tests enthalten:

not_null und unique für Schlüsselfelder

relationships für Tabellenverknüpfungen

Eigene Tests können im Ordner tests/ ergänzt werden.

## Nützliche dbt Befehle
```plaintext
dbt run — Modelle ausführen

dbt test — Tests ausführen

dbt build — kombiniert run, test und weitere Schritte

dbt docs generate — Dokumentation generieren

dbt docs serve — Dokumentation lokal anzeigen
```
Kontakt
Bei Fragen gerne melden: eugen.gabriel.inbox@gmail.com
