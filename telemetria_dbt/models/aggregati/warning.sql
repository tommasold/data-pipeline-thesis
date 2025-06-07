SELECT
  vehicle_id,
  parametro,
  COUNT(*) AS warning_count
FROM {{ ref('clean_telemetria') }}
WHERE stato = 'WARNING'
GROUP BY vehicle_id, parametro
ORDER BY warning_count DESC
