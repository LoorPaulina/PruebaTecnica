from app.extensiones import db
from app.extensiones import ma

class EstadoReserva(db.Model):
    __tablename__ = 'estado_reserva'

    codigo = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(10), nullable=False)
    descripcion = db.Column(db.String(100))
    audit_create_date = db.Column(db.Date)
    audit_create_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))
    audit_update_date = db.Column(db.Date)
    audit_update_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))

class EstadoReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EstadoReserva
        include_fk = True
