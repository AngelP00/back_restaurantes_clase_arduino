from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
    Boolean,
)
from api_config import (
    db,
)

from .objects import (
    Restaurante,
    Menu,
    Plato
)
from .restaurante import Restaurante as RestauranteModel
from .menu import Menu as MenuModel
from .plato import Plato as PlatoModel


# ============ restaurante ============
class createRestaurante(Mutation):
    class Arguments:
        name = String(required=True)
        direccion = String(required=True)
        email = String(required=False)
    
    restaurante = Field(lambda: Restaurante)

    def mutate(self, info, name, direccion, email=None):
        restaurante = RestauranteModel(name=name, direccion=direccion, email=email)

        db.session.add(restaurante)
        db.session.commit()

        return createRestaurante(restaurante=restaurante)

class updateRestaurante(Mutation):
    class Arguments:
        restaurante_id = Int(required=True)
        email = String()
        name = String()
        direccion = String()
        menu_fk=Int()

    restaurante = Field(lambda: Restaurante)

    def mutate(self, info, restaurante_id, email=None, name=None, direccion=None,menu_fk=None):
        restaurante = RestauranteModel.query.get(restaurante_id)
        if restaurante:
            if email:
                restaurante.email = email
            if name:
                restaurante.name = name
            if direccion:
                restaurante.direccion = direccion
            if menu_fk:
                restaurante.menu_fk = menu_fk
            db.session.add(restaurante)
            db.session.commit()

        return updateRestaurante(restaurante=restaurante)

class deleteRestaurante(Mutation):
    class Arguments:
        restaurante_id = Int(required=True)

    restaurante = Field(lambda: Restaurante)

    def mutate(self, info, restaurante_id):
        restaurante = RestauranteModel.query.get(restaurante_id)
        if restaurante:
            db.session.delete(restaurante)
            db.session.commit()

        return deleteRestaurante(restaurante=restaurante)
# ====================================

# ============ menu ============
class createMenu(Mutation):
    class Arguments:
        name = String(required=True)
    
    menu = Field(lambda: Menu)

    def mutate(self, info, name):
        menu = MenuModel(name=name)

        db.session.add(menu)
        db.session.commit()

        return createMenu(menu=menu)

class updateMenu(Mutation):
    class Arguments:
        menu_id = Int(required=True)
        name = String()

    menu = Field(lambda: Menu)

    def mutate(self, info, menu_id, name=None):
        menu = MenuModel.query.get(menu_id)
        if menu:
            if name:
                menu.name = name
            db.session.add(menu)
            db.session.commit()

        return updateMenu(menu=menu)

class deleteMenu(Mutation):
    class Arguments:
        menu_id = Int(required=True)

    menu = Field(lambda: Menu)

    def mutate(self, info, menu_id):
        menu = MenuModel.query.get(menu_id)
        if menu:
            db.session.delete(menu)
            db.session.commit()

        return deleteMenu(menu=menu)
# ====================================

# ============ plato ============
class createPlato(Mutation):
    class Arguments:
        name = String(required=True)
        descripcion = String(required=False)
        precio=Int(required=False)
        menu_fk=Int(required=False)

        en_venta = Boolean(required=False)
        vegan = Boolean(required=False)
        vegetarian = Boolean(required=False)
        gluten_free = Boolean(required=False)
    
    plato = Field(lambda: Plato)

    def mutate(self, info, name,descripcion=None,precio=None,menu_fk=None,en_venta=None,vegan=None,vegetarian=None,gluten_free=None):
        plato = PlatoModel(name=name,descripcion=descripcion,precio=precio,menu_fk=menu_fk,en_venta=en_venta,vegan=vegan,vegetarian=vegetarian,gluten_free=gluten_free)

        db.session.add(plato)
        db.session.commit()

        return createPlato(plato=plato)

class updatePlato(Mutation):
    class Arguments:
        plato_id = Int(required=True)
        name = String()

        descripcion = String(required=False)
        precio=Int(required=False)
        menu_fk=Int(required=False)

        en_venta = Boolean(required=False)
        vegan = Boolean(required=False)
        vegetarian = Boolean(required=False)
        gluten_free = Boolean(required=False)

    plato = Field(lambda: Plato)

    def mutate(self, info, plato_id, name=None,descripcion=None,precio=None,menu_fk=None,en_venta=None,vegan=None,vegetarian=None,gluten_free=None):
        plato = PlatoModel.query.get(plato_id)
        if plato:
            if name:
                plato.name = name
            if descripcion:
                plato.descripcion = descripcion
            if precio:
                plato.precio = precio
            if menu_fk:
                plato.menu_fk = menu_fk
            if en_venta is not None:
                plato.en_venta = en_venta
            if vegan is not None:
                plato.vegan = vegan
            if vegetarian is not None:
                plato.vegetarian = vegetarian
            if gluten_free is not None:
                plato.gluten_free = gluten_free
            db.session.add(plato)
            db.session.commit()

        return updatePlato(plato=plato)

class deletePlato(Mutation):
    class Arguments:
        plato_id = Int(required=True)

    plato = Field(lambda: Plato)

    def mutate(self, info, plato_id):
        plato = PlatoModel.query.get(plato_id)
        if plato:
            db.session.delete(plato)
            db.session.commit()

        return deletePlato(plato=plato)
# ====================================

class Mutation(ObjectType):
    # ============ restaurante ============
    create_restaurante = createRestaurante.Field()
    update_restaurante = updateRestaurante.Field()
    delete_restaurante = deleteRestaurante.Field()
    # ====================================

    # ============ menu ============
    create_menu = createMenu.Field()
    update_menu = updateMenu.Field()
    delete_menu = deleteMenu.Field()
    # ====================================

    # ============ plato ============
    create_plato = createPlato.Field()
    update_plato = updatePlato.Field()
    delete_plato = deletePlato.Field()
    # ====================================