SELECT
  vehicle_id,
  parametro,
  ROUND(AVG(valore), 2) AS media_valore
FROM {{ ref('clean_telemetria') }}
GROUP BY vehicle_id, parametro
ORDER BY vehicle_id, parametro
