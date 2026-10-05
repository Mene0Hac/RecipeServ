from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.user import User
from resipedb.image import Base

class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True,nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id", onupdate="CASCADE"),nullable=False)
    title: Mapped[str] = mapped_column(String(80),nullable=False,default='Пусто')
    description: Mapped[str] = mapped_column(String(255),nullable=False,default='Пусто')
    description_of_cooking_process: Mapped[str] = mapped_column(String(255),nullable=False,default='Пусто')
    caloric_content: Mapped[int] = mapped_column(nullable=False,default=0)
    
    author: Mapped["User"] = relationship(lazy="joined")   
    #ratings: Mapped[int]
    #AT_recipe_ingredient

    def get_info(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "author_username": self.author.username,
            "title": self.title,
            "description": self.description,
            "description_of_cooking_process": self.description_of_cooking_process,
            "caloric_content": self.caloric_content
        }
        
    def __repr__(self):
        return super().__repr__()