import bcrypt

def encriptar(password):
    salt = bcrypt.gensalt()
    codificacion = bcrypt.hashpw(password.encode('utf-8'), salt)
    return codificacion

def verificar(password_ingresada, password):
    decodificacion = bcrypt.checkpw(password_ingresada.encode('utf-8'), password.encode('utf-8'))
    return decodificacion