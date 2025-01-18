from flask import jsonify, request
from app.services.vuelo import bp
from app.services.vuelo.modelos.vuelo_db import Vuelo
from app.extensiones import db
from sqlalchemy import func
from app.utilities import reply,verificar_fecha

@bp.route('/', methods=['GET'])
def obtener_vuelos():
    try:
        data = request.get_json()
        filtro = data["filtro"]

        result = db.session.query(Vuelo)
        if filtro.get("origen"):
            origen = filtro["origen"].lower()
            result = result.filter(
            func.lower(Vuelo.origen).contains(origen)
        )

        if filtro.get("destino"):
            destino = filtro["destino"].lower()
            result = result.filter(
                func.lower(Vuelo.destino).contains(destino)
            )

        if filtro.get("fecha"):
            fecha = filtro["fecha"]
            try:
                if verificar_fecha.es_fecha_valida(fecha):
                    result = result.filter(Vuelo.fecha == fecha)
            except Exception:
                return jsonify({"mensaje": "Error al procesar la fecha. Formato correcto AAAA-MM-DD."})
            
            result = result.filter(
                Vuelo.fecha == fecha
            )
        
        results = result.all()

        if not results:
            return {"mensaje": "No se encontraron datos con los filtros proporcionados."}
        
        results = [
        {
            "id": row.id,
            "origen": row.origen,
            "destino": row.destino,
            "fecha": row.fecha.isoformat() if row.fecha else None
        }
        for row in results
        ]
        
        return jsonify({"data":results, "mensaje": reply.message_ok}),200
    except Exception as e:
        print(e)
        return jsonify({"mensaje": reply.message_failed})