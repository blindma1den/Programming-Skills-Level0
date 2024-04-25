from datetime import datetime, timedelta

def calculate_date_fn(days):
    today = datetime.now()
    days_to_rise = timedelta(days=days)
    date = today + days_to_rise

    # Formatear la fecha en el formato día/mes/año
    fecha_envio = today.strftime("%d/%m/%Y")
    fecha_llegada = date.strftime("%d/%m/%Y")

    return fecha_envio, fecha_llegada