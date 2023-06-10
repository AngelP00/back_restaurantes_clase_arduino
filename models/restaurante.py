from api_config import db


class Restaurante(db.Model):
    __tablename__ = "restaurante"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    direccion = db.Column(db.String(500))
    email  = db.Column(db.String(150), nullable=True)
    menu_fk = db.Column(db.Integer, db.ForeignKey("menu.id"))
    menu = db.relationship('Menu')
    #menu = db.relationship('Menu', backref='restaurantes_depto')

