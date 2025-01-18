from app.extensiones import db
from app.extensiones import ma

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    correo = db.Column(db.String(20), nullable=False)
    telefono = db.Column(db.String(10))
    contraseña = db.Column(db.String(250), nullable=False)
    audit_create_date = db.Column(db.Date)

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
