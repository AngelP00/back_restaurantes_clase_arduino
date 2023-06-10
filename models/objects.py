from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    Int,
    String,
    GlobalID,
    Boolean
)
from models.menu import Menu as MenuModel
# from models.user import User as UserModel
from models.restaurante import Restaurante as RestauranteModel
from models.plato import Plato as PlatoModel

class Restaurante(SQLAlchemyObjectType):
    class Meta:
        model = RestauranteModel
    #id = GlobalID(description='primary_key. El id es unico para cada restaurante')
    name = String(description='representa el nombre de la restaurante')
    direccion = String(description='representa el apellido de la restaurante')
    email = String(description='representa el email de la restaurante')
    #deptoFk = Int(description='ForeignKey. La restaurante trabaja en este menu')
    menu_fk = Int(description='ForeignKey. La restaurante trabaja en este menu')
    #menu1 = menuo(description='Menu. La restaurante trabaja en este menu')

class Menu(SQLAlchemyObjectType):
    class Meta:
        model = MenuModel
        # exclude_fields = ('fk_restaurante')
    name = String(description='representa el nombre del menu')

class Plato(SQLAlchemyObjectType):
    class Meta:
        model = PlatoModel
        # exclude_fields = ('fk_restaurante')
    name = String(description='representa el nombre del menu')
    en_venta = Boolean(description='representa el nombre del menu')

# class User(SQLAlchemyObjectType):
#     class Meta:
#         model = UserModel