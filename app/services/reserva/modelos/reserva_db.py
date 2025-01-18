from app.extensiones import db
from app.extensiones import ma

class Reserva(db.Model):
    __tablename__ = 'reserva'

    id = db.Column(db.String(10), primary_key=True)
    vuelo = db.Column(db.String(10))
    usuario = db.Column(db.String(10))
    estado = db.Column(db.String(10))
    metodo_pago = db.Column(db.String(10))
    audit_create_date = db.Column(db.Date)
    audit_create_user = db.Column(db.String(10))
    audit_update_date = db.Column(db.Date)
    audit_update_user = db.Column(db.String(10))

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reserva
        include_fk = True
