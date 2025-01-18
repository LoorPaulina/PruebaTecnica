from app.extensiones import db
from app.extensiones import ma

class Ciudad(db.Model):
    __tablename__ = 'ciudad'

    id = db.Column(db.String(10), primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)
    audit_create_date = db.Column(db.Date)
    audit_create_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))
    audit_update_date = db.Column(db.Date)
    audit_update_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))

class CiudadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ciudad
        include_fk = True
