from datetime import datetime, timedelta
import locale


# Obtener Fecha y hora actuales

date_now = datetime.now()
print(f"Fecha y hora actuales: {date_now}")

# Obtener una Fecha cualquiera

print(f"Fecha y hora de un dia cualquiera: {datetime(2025, 4, 21)}")

# Formatear las Fechas

fecha_formateada = date_now.strftime("%d/%m/%Y %I:%M:%S (%p)")
print(f"La fecha formateada es: {fecha_formateada}")

# Operaciones con fechas

fecha_resultado = date_now - timedelta(days=1)
print(f"El resultado de la fecha es: {fecha_resultado}")

# Calcular diferencias entre fechas

mi_cumpleaños = datetime(2026, 1, 10, 18, 6, 30)
diferencia_fechas = mi_cumpleaños - date_now
print(f"La diferencia que hay entre fechas es la siguiente: {diferencia_fechas.days}")

# Cambiar los dias y los meses a español

locale.setlocale(locale.LC_TIME, 'es_CO') # Esto es para poder cambiar la region de la inglesa a Colombia y el LC_TIME se puede cambiar para que cambie toda la configuracion regional y no solo la del tiempo
fecha_formateada_español = date_now.strftime("%A %d de %B de %Y (%I:%M:%S) (%p))")
print(f"La fecha formateada es: {fecha_formateada_español}")