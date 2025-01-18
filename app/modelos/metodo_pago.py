from app.extensiones import db
from app.extensiones import ma

class MetodoPago(db.Model):
    __tablename__ = 'metodo_pago'

    codigo = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(10), nullable=False)
    audit_create_date = db.Column(db.Date)
    audit_create_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))
    audit_update_date = db.Column(db.Date)
    audit_update_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))

class MetodoPagoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MetodoPago
        include_fk = True
