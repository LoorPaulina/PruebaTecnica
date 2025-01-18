from app.extensiones import db
from app.extensiones import ma

class Clase(db.Model):
    __tablename__ = 'clase'

    codigo = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(100))
    equipaje_permitido = db.Column(db.Float)
    precio = db.Column(db.Float, nullable=False)
    audit_create_date = db.Column(db.Date)
    audit_create_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))
    audit_update_date = db.Column(db.Date)
    audit_update_user = db.Column(db.String(10), db.ForeignKey('usuario.id'))

class ClaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Clase
        include_fk = True
