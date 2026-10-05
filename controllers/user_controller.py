from sqlalchemy import select
from resipedb.image import session_scope
from models.user import User


def get_all_users():
    with session_scope() as session:
        users = session.scalars(select(User)).all()
   
    return {"data": [user.get_info() for user in users]}