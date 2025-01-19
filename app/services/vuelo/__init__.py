from flask import Blueprint

bp = Blueprint('vuelo', __name__)

from app.services.vuelo import vuelo
