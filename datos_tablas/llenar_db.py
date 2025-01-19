import pandas as pd
import mysql.connector

db_config = {
    'host': 'localhost',       
    'user': 'root',     
    'password': 'root', 
    'database': 'vuelos'
}

def insertar_datos(tabla, archivo_excel):
    df = pd.read_excel(archivo_excel)
    
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        columns = df.columns.tolist()
        placeholders = ", ".join(["%s"] * len(columns))
        column_names = ", ".join(columns)

        query = f"INSERT INTO {tabla} ({column_names}) VALUES ({placeholders})"

        for _, row in df.iterrows():
            data = tuple(row[col] for col in columns)
            cursor.execute(query, data)

        connection.commit()
        print(f"Datos insertados exitosamente en la tabla '{tabla}'.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada.")

insertar_datos("usuario", "usuario.xlsx")
insertar_datos("clase", "clase.xlsx")
insertar_datos("ciudad", "ciudad.xlsx")
insertar_datos("vuelo", "vuelo.xlsx")
insertar_datos("estado_reserva", "estado_reserva.xlsx")
insertar_datos("metodo_pago", "metodo_pago.xlsx")
insertar_datos("reserva", "reserva.xlsx")