from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers import user_controller
from resipedb.image import get_db

router = APIRouter()

@router.get("/get_all_users")
def get_all_users_route(db: Session = Depends(get_db)):
    return user_controller.get_all_users(db)