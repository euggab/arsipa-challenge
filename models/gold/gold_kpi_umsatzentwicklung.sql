SELECT
  u.gesellschaft_id,
  g.gesellschaft_name,
  u.monat,
  SUM(u.umsatz_eur) AS umsatz_monat
from  {{ ref('f_umsatz_gesellschaft') }} u
join {{ ref('d_gesellschaften') }} g USING (gesellschaft_id)
GROUP BY gesellschaft_id, gesellschaft_name, monat
ORDER BY gesellschaft_id, monat