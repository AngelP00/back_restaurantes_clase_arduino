from api_config import db

#from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

class Plato(db.Model):
    __tablename__ = "plato"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descripcion = db.Column(db.String(150))
    
    precio = db.Column(db.Integer)

    en_venta = db.Column(db.Boolean, default=False)
    vegan = db.Column(db.Boolean)
    vegetarian = db.Column(db.Boolean)
    gluten_free = db.Column(db.Boolean)

    menu_fk = db.Column(db.Integer, db.ForeignKey("menu.id"))
    menu = db.relationship('Menu', backref='menu_platos')
    #menu2 = db.relationship('Menu', backref=backref('menu_platos',primaryjoin="and_(Plato.en_venta == True)"))


'''
Vegano: Vegan
Vegetariano: Vegetarian
Lacto-vegetariano: Lacto-vegetarian
Ovo-vegetariano: Ovo-vegetarian
Pescetariano: Pescetarian
Flexitariano: Flexitarian
Crudívoro: Raw foodist
Sin gluten: Gluten-free
Sin lácteos: Dairy-free
Sin nueces: Nut-free
Sin azúcar: Sugar-free
Sin carne: Meat-free
Sin huevos: Egg-free
'''