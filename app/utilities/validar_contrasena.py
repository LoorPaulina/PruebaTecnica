import re

def validar_seguridad_contrasena(password):
    if len(password) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if len(password) > 12:
        return "La contraseña debe tener máximo 12 caracteres."
    if not re.search(r"[A-Z]", password):
        return "La contraseña debe tener al menos una letra mayúscula."
    if not re.search(r"[a-z]", password):
        return "La contraseña debe tener al menos una letra minúscula."
    if not re.search(r"[0-9]", password):
        return "La contraseña debe tener al menos un número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "La contraseña debe tener al menos un carácter especial."
    return None