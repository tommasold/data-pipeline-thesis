SELECT
  timestamp,
  vehicle_id,
  parametro,
  valore,
  CASE
    WHEN parametro = 'giri_motore' AND (valore < 1000 OR valore > 6500) THEN 'CRITICAL'
    WHEN parametro = 'giri_motore' AND (valore BETWEEN 1000 AND 2000 OR valore BETWEEN 6000 AND 6500) THEN 'WARNING'
    WHEN parametro = 'giri_motore' THEN 'OK'

    WHEN parametro = 'temperatura' AND (valore < 75 OR valore > 115) THEN 'CRITICAL'
    WHEN parametro = 'temperatura' AND (valore BETWEEN 75 AND 80 OR valore BETWEEN 110 AND 115) THEN 'WARNING'
    WHEN parametro = 'temperatura' THEN 'OK'

    WHEN parametro = 'pressione_olio' AND (valore < 1.2 OR valore > 4.8) THEN 'CRITICAL'
    WHEN parametro = 'pressione_olio' AND (valore BETWEEN 1.2 AND 1.5 OR valore BETWEEN 4.5 AND 4.8) THEN 'WARNING'
    ELSE 'OK'
  END AS stato
FROM
  {{ source('public', 'telemetria_veicoli') }}
WHERE
  (
    (parametro = 'giri_motore' AND valore BETWEEN 800 AND 7000) OR
    (parametro = 'temperatura' AND valore BETWEEN 70 AND 120) OR
    (parametro = 'pressione_olio' AND valore BETWEEN 1.0 AND 5.0)
  )
