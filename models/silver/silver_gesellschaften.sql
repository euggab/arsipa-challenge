-- models/silver/silver_gesellschaften.sql

with raw as (
    select * from {{ ref('bronze_gesellschaften') }}
)

select
    gesellschaft_id::integer,
    initcap(gesellschaft_name) as gesellschaft_name,
    initcap(standort) as standort,
    lower(branche) as branche
from raw
where gesellschaft_id is not null
