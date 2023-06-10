from api_config import db

#from sqlalchemy.orm import backref
class Menu(db.Model):
    __tablename__ = "menu"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #fk_restaurante = db.Column(db.Integer, db.ForeignKey("restaurante.id"))
    # restaurante = db.relationship("Restaurante")

    #platos = db.relationship("Plato", backref=backref('menu_platos', primaryjoin='and_(Plato.en_venta == True)'))
    #platos = db.relationship("Plato", 'menu_platos')

