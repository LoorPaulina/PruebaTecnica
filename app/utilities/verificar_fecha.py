import datetime


def es_fecha_valida(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False