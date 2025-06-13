-- models/silver/silver_mitarbeiter.sql

with raw as (
    select * from {{ ref('bronze_mitarbeiter') }}
)

select
    gesellschaft_id::integer,
    date_trunc('month', monat::date) as monat,
    anzahl_mitarbeiter::integer
from raw
where gesellschaft_id is not null
