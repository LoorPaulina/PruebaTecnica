import os
from flask import Flask
from app.extensiones import jwt
from app.extensiones import db, ma

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.conexion.Config')
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    # Registrar Blueprints
    from app.services.reserva import bp as reserva_bp
    app.register_blueprint(reserva_bp, url_prefix='/api/reservas')

    from app.services.usuario import bp as usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')

    from app.services.vuelo import bp as vuelo_bp
    app.register_blueprint(vuelo_bp, url_prefix='/api/vuelos')
    return app
