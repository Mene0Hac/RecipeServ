from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User


def get_all_users(db: Session):
    users = db.scalars(select(User)).all()

    return {"data": [user.get_info() for user in users]}