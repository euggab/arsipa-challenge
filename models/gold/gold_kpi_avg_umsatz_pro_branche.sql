select

g.branche,
u.monat,

round(avg(u.umsatz_eur),2) as avg_umsatz

from {{ ref('silver_umsatz') }} u
join {{ ref('silver_gesellschaften') }} g USING (gesellschaft_id)

group by g.branche, u.monat
