import psycopg2
import pandas as pd

conn_params = {
    "host": "127.0.0.1",
    "port": 5432,
    "dbname": "arsipa_bi",
    "user": "admin",
    "password": "admin"
}

csv_files = {
    "bronze_umsatz": "data/umsatz.csv",
    "bronze_gesellschaften": "data/gesellschaften.csv",
    "bronze_mitarbeiter": "data/mitarbeiter.csv"
}

def create_table_if_not_exists(cursor, table_name, create_sql):
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {create_sql}
    );
    """)

def ingest_csv_to_postgres(table_name, csv_file, conn):
    df = pd.read_csv(csv_file)
    from io import StringIO
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False, header=False)
    csv_buffer.seek(0)

    with conn.cursor() as cur:
        if table_name == "bronze_umsatz":
            create_table_if_not_exists(cur, table_name, """
                gesellschaft_id VARCHAR(50),
                monat VARCHAR(10),
                umsatz_eur NUMERIC
            """)
        elif table_name == "bronze_gesellschaften":
            create_table_if_not_exists(cur, table_name, """
                gesellschaft_id VARCHAR(50) PRIMARY KEY,
                gesellschaft_name VARCHAR(255),
                standort VARCHAR(255),
                branche VARCHAR(255)
            """)
        elif table_name == "bronze_mitarbeiter":
            create_table_if_not_exists(cur, table_name, """
                gesellschaft_id VARCHAR(50),
                monat VARCHAR(10),
                anzahl_mitarbeiter INTEGER
            """)

        conn.commit()

        cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", csv_buffer)
        conn.commit()
        print(f"Files aus {csv_file} erfolgreich in die {table_name} hochgeladen")

def main():
    conn = psycopg2.connect(**conn_params)
    try:
        for table, csv_file in csv_files.items():
            ingest_csv_to_postgres(table, csv_file, conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
