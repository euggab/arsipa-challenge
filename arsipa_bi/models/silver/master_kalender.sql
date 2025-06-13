-- models/silver/master_kalender.sql

with dates as (
    select
        generate_series(
            date '2022-01-01',      -- start_date
            date '2026-12-01',      -- end_date
            interval '1 month'
        )::date as monat
)

select
    monat,
    extract(year from monat)::int as jahr,
    extract(month from monat)::int as monat_nummer,
    to_char(monat, 'TMMonth') as monat_name,
    to_char(monat, 'YYYY-MM') as monat_label,
    monat = date_trunc('month', current_date) as ist_aktueller_monat
from dates
order by monat
