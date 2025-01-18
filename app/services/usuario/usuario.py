import bcrypt
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from app.services.usuario import bp
from app.services.reserva.modelos.reserva_db import Reserva
from app.services.usuario.modelos.usuario_db import Usuario
from app.services.vuelo.modelos.vuelo_db import Vuelo
from app.extensiones import db
from app.utilities import reply, encriptacion
from datetime import datetime
from app.utilities import validar_contrasena

@bp.route('/<string:id>/reservas', methods=['GET'])
@jwt_required()
def ver_reservas_por_usuario(id):
    try:
        reservas = db.session.query(Reserva,Vuelo).filter(
            Reserva.usuario == id
        ).join(
            Vuelo, 
            Reserva.vuelo == Vuelo.id
        ).all()

        if not reservas:
            return jsonify({"mensaje": "No se encontraron reservas para este usuario"})

        results = [
        {
            "id": reserva.id,
            "origen": vuelo.origen,
            "destino": vuelo.destino,
            "fecha": vuelo.fecha.isoformat() if vuelo.fecha else None,
            "estado": reserva.estado
        }
         for reserva, vuelo in reservas
        ]
        
        return jsonify({"data":results, "mensaje": reply.message_ok}),200
    except Exception as e:
        print(e)
        return jsonify({"mensaje": reply.message_failed})

@bp.route('/registro', methods=['POST'])
def registrar_usuario():
    try:
        data = request.get_json()
        nombre = data.get("nombre")
        correo = data.get("correo")
        password = encriptacion.encriptar(data.get("contrasena"))
        audit_create_date = datetime.now().date()

        if not data.get("nombre"):
            return jsonify({"mensaje": "El campo 'nombre' es obligatorio."}), 400
        
        if not data.get("correo"):
            return jsonify({"mensaje": "El campo 'correo' es obligatorio."}), 400
        
        if not data.get("contrasena"):
            return jsonify({"mensaje": "El campo 'contrasena' es obligatorio."}), 400

        usuario = db.session.query(Usuario).filter(
            Usuario.correo  == correo
        ).first()

        if usuario:
            return ({"mensaje": "Este correo ya se encuentra en uso."}),400
        validacion = validar_contrasena.validar_seguridad_contrasena(data.get("contrasena"))
        if validacion:
            return ({"mensaje": validacion}),400

        total_filas = db.session.query(Usuario).count()
        nuevo_id = f"U{total_filas + 1:03}"

        usuario = Usuario(
            id = nuevo_id,
            nombre = nombre,
            correo = correo,
            contraseña = password,
            audit_create_date = audit_create_date
        )

        db.session.add(usuario)
        db.session.commit()

        return jsonify({"mensaje": "Usuario creado con éxito"}),201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"mensaje": reply.message_failed}),400

@bp.route('/iniciarSesion', methods=['GET'])
def iniciar_sesion():
    try:
        data = request.get_json()
        correo = data.get("correo")
        password_ingresada = data.get("contrasena")

        if not data.get("contrasena"):
            return jsonify({"mensaje": "El campo 'contrasena' es obligatorio."}), 400
        
        if not data.get("correo"):
            return jsonify({"mensaje": "El campo 'correo' es obligatorio."}), 400

        usuario = db.session.query(Usuario).filter(
            Usuario.correo  == correo
        ).first()

        if not usuario:
            return jsonify({"mensaje": "Este usuario no existe."}),404
        
        if not encriptacion.verificar(password_ingresada, usuario.contraseña):
            return jsonify({"mensaje": "Contraseña incorrecta. Por favor verifique."}),401
        token = create_access_token(identity=usuario.correo)
        return jsonify({"mensaje": "Acceso correcto.","access_token":token}),200
    except Exception as e:
        print(e)
        return jsonify({"mensaje": reply.message_failed}),400


    

