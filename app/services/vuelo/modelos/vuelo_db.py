from app.extensiones import db
from app.extensiones import ma

class Vuelo(db.Model):
    __tablename__ = 'vuelo'

    id = db.Column(db.String(10), primary_key=True)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    disponibilidad = db.Column(db.Boolean, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    clase = db.Column(db.String(10), db.ForeignKey('clase.codigo'), nullable=False)
    audit_create_date = db.Column(db.Date)
    audit_create_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))
    audit_update_date = db.Column(db.Date)
    audit_update_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))

class VueloSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vuelo
        include_fk = True
