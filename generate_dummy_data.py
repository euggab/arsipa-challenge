import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

fake = Faker("de_DE")
np.random.seed(42)

# Параметры
n_gesellschaften = 20
monate = pd.date_range(start="2023-01-01", end="2024-12-01", freq="MS")

# === 1. gesellschaften.csv ===
gesellschaften = pd.DataFrame({
    "gesellschaft_id": range(1, n_gesellschaften + 1),
    "gesellschaft_name": [fake.company() for _ in range(n_gesellschaften)],
    "standort": [fake.city() for _ in range(n_gesellschaften)],
    "branche": np.random.choice(["Arbeitsmedizin", "Arbeitssicherheit", "Umweltschutz"], size=n_gesellschaften)
})
gesellschaften.to_csv("gesellschaften.csv", index=False)

# === 2. umsatz.csv ===
umsatz = pd.DataFrame([
    {
        "gesellschaft_id": gid,
        "monat": monat.strftime("%Y-%m-%d"),
        "umsatz_eur": round(np.random.uniform(10000, 250000), 2)
    }
    for gid in range(1, n_gesellschaften + 1)
    for monat in monate
])
umsatz.to_csv("umsatz.csv", index=False)

# === 3. mitarbeiter.csv ===
mitarbeiter = pd.DataFrame([
    {
        "gesellschaft_id": gid,
        "monat": monat.strftime("%Y-%m-%d"),
        "anzahl_mitarbeiter": np.random.randint(5, 80)
    }
    for gid in range(1, n_gesellschaften + 1)
    for monat in monate
])
mitarbeiter.to_csv("mitarbeiter.csv", index=False)

print("✅ Dummy-Daten wurden erfolgreich generiert!")
