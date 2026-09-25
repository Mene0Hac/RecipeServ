from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from resipedb.image import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True,nullable=False)
    username: Mapped[str] = mapped_column(String(80),unique=True,nullable=False)
    password_hash: Mapped[str] = mapped_column(String(128),nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean,nullable=False,default=False)
    is_banned: Mapped[bool] = mapped_column(Boolean,nullable=False,default=False)

    def get_info(self):
        return {
            "id": self.id,
            "username": self.username,
            "is_admin": self.is_admin,
            "is_banned": self.is_banned
        }