select 
u.monat,
u.gesellschaft_id,
g.gesellschaft_name,
sum(u.umsatz_eur) as umsatz,
sum(m.anzahl_mitarbeiter) as mitarbeiter,

CASE 
    WHEN  sum(m.anzahl_mitarbeiter) = 0 THEN NULL  
    ELSE round(sum(u.umsatz_eur)::NUMERIC / sum(m.anzahl_mitarbeiter), 2)
END as umsatz_pro_mitarbeiter

from  {{ ref('silver_umsatz') }} u
join {{ ref('silver_gesellschaften') }} g USING (gesellschaft_id)
join {{ ref('silver_mitarbeiter') }} m using (gesellschaft_id, monat)

group by u.monat, u.gesellschaft_id, g.gesellschaft_name