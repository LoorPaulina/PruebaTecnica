from flask import Blueprint

bp = Blueprint('reserva', __name__)

from app.services.reserva import reserva
