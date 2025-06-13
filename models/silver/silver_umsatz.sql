-- models/silver/silver_umsatz.sql

with raw as (
    select * from {{ ref('bronze_umsatz') }}
)

select
    gesellschaft_id::integer,
    date_trunc('month', monat::date) as monat,
    umsatz_eur::numeric
from raw
where gesellschaft_id is not null
