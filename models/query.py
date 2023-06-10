from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    List,
    Int
)

from .restaurante import Restaurante as RestauranteModel
from .objects import Restaurante, Menu, Plato
from .menu import Menu as MenuModel
from .plato import Plato as PlatoModel


class Query(ObjectType):
    restaurantes = List(lambda: Restaurante, direccion=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())
    restaurante = Field(lambda: Restaurante, id=Int(required=True))
    
    menus = List(lambda: Menu)
    menu = Field(lambda: Menu, id=Int(required=True))

    platos = List(lambda: Plato, direccion=String(), id=Int(), has_email=Boolean(), order_by_precio=Boolean(),en_venta=Boolean(),vegan=Boolean(),vegetarian=Boolean(),gluten_free=Boolean())
    plato = Field(lambda: Plato, id=Int(required=True))

    # ============ restaurante ============

    def resolve_restaurantes(self, info, id=None, direccion=None, has_email=None, order_by_name=None):
        query = Restaurante.get_query(info=info)
        if id:
            query = query.filter(RestauranteModel.id==id)
        if direccion:
            query = query.filter(RestauranteModel.direccion==direccion)
        if has_email is not None:
            if has_email:
                query = query.filter(RestauranteModel.email != None)
            else:
                query = query.filter(RestauranteModel.email == None)
        if order_by_name:
            query = query.order_by(RestauranteModel.name)
        return query.all()
    
    def resolve_restaurante(self, info, id):
        restaurante = RestauranteModel.query.get(id)
        return restaurante
    # ====================================
    
    # ============ menu ============
    def resolve_menus(self, info):
        query = Menu.get_query(info=info)
        return query.all()
    
    def resolve_menu(self, info, id):
        dpto = MenuModel.query.get(id)
        return dpto
    # ====================================

    # ============ plato ============
    def resolve_platos(self, info, id=None, direccion=None, order_by_name=None,en_venta=None,vegan=None,vegetarian=None,gluten_free=None):
        query = Plato.get_query(info=info)
        if id:
            query = query.filter(PlatoModel.id==id)
        if direccion:
            query = query.filter(PlatoModel.direccion==direccion)
        if en_venta is not None:
            query = query.filter(PlatoModel.en_venta == en_venta)
        if vegan is not None:
            query = query.filter(PlatoModel.vegan == vegan)
        if vegetarian is not None:
            query = query.filter(PlatoModel.vegetarian == vegetarian)
        if gluten_free is not None:
            query = query.filter(PlatoModel.gluten_free == gluten_free)
        if order_by_name:
            query = query.order_by(PlatoModel.name)
        return query.all()
    
    def resolve_plato(self, info, id):
        plato = PlatoModel.query.get(id)
        return plato
    # ====================================