from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers import user_controller, recipe_controller

router = APIRouter()

@router.get("/get_all_users")
def get_all_users_route():
    return user_controller.get_all_users()

@router.get("/get_all_recipes")
def get_all_recipes():
    return recipe_controller.get_all_recipes()