from flask import Blueprint

bp = Blueprint('usuario', __name__)

from app.services.usuario import usuario
