from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.reserva import bp
from app.extensiones import db
from app.services.reserva.modelos.reserva_db import Reserva
from app.utilities import reply
from app.modelos.estado_reserva import EstadoReserva
from app.modelos.metodo_pago import MetodoPago
from app.services.vuelo.modelos.vuelo_db import Vuelo

@bp.route('/', methods=['POST'])
@jwt_required()
def reservar_vuelo():
    try:
        data = request.get_json()

        if not data.get("vueloId"):
            return jsonify({"mensaje": "El campo 'vueloId' es obligatorio."}), 400

        if not data.get("usuarioId"):
            return jsonify({"mensaje": "El campo 'usuarioId' es obligatorio."}), 400
        
        total_filas = db.session.query(Reserva).count()
        nuevo_id = f"R{total_filas + 1:03}"

        activo_id = db.session.query(EstadoReserva).filter(
            EstadoReserva.descripcion=="Activo"
        ).first()

        pago_id = db.session.query(MetodoPago).filter(
            MetodoPago.nombre=="EFECT"
        ).first()

        vuelo_id = db.session.query(Vuelo).filter(
            Vuelo.id == data.get("vueloId")
        ).first()

        if not vuelo_id:
            return jsonify({"mensaje": "El vuelo no se encuentra registrado."}),404
        
        if vuelo_id.disponibilidad ==0:
            return jsonify({"mensaje": "El vuelo no se encuentra disponible."}),404
        

        vuelo_id = db.session.query(Reserva).filter(
            Reserva.vuelo == data.get("vueloId")
        ).first()

        if vuelo_id:
            return jsonify({"mensaje": "El usuario ya tiene una reserva para este vuelo."}),404
    
        reserva = Reserva(
            id = nuevo_id,
            vuelo = data.get("vueloId"),
            usuario = data.get("usuarioId"),
            estado = activo_id.codigo,
            metodo_pago = pago_id.codigo,
            audit_create_date = datetime.now().date()
        )

        db.session.add(reserva)
        db.session.commit()

        return jsonify({"mensaje": "Reserva creada con éxito"})
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"mensaje": reply.message_failed})
    

@bp.route('/<string:id>', methods=['DELETE'])
@jwt_required()
def cancelar_reserva(id):
    try:
        reserva = db.session.query(Reserva).filter(
            Reserva.id == id
        ).first()

        if not reserva:
            return jsonify({"mensaje": "No se encontraron reservas."})

        db.session.delete(reserva)
        db.session.commit()
        return jsonify({"mensaje": reply.message_ok}),200
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"mensaje": reply.message_failed})
