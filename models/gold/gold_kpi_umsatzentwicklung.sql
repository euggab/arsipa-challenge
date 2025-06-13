SELECT
  u.gesellschaft_id,
  g.gesellschaft_name,
  u.monat,
  SUM(u.umsatz_eur) AS umsatz_monat
from  {{ ref('silver_umsatz') }} u
join {{ ref('silver_gesellschaften') }} g USING (gesellschaft_id)
GROUP BY gesellschaft_id, gesellschaft_name, monat
ORDER BY gesellschaft_id, monat