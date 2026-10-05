from sqlalchemy import select
from resipedb.image import session_scope
from models.recipe import Recipe


def get_all_recipes():
    
    with session_scope() as session:
        recipes = session.scalars(select(Recipe)).all()

    return {"data": [recipe.get_info() for recipe in recipes]}