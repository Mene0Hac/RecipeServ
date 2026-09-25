
from sqlalchemy import create_engine, false, text
from dotenv import load_dotenv
import os
load_dotenv()


DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)

# def add_user(name, age):
#     with engine.connect() as connection:
#         connection.execute(
#             text("""
#                 INSERT INTO test_db.students (name, age)
#                 VALUES (:name, :age)
#             """),
#             {
#                 "name": name,
#                 "age": age
#             }
#         )

#         connection.commit()

#     print("Пользователь успешно добавлен!")

def get_all_users():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT id, username, password_hash, is_admin, is_banned
                FROM "user"
            """)
        )

        return result.fetchall()  # Возвращаем все строки результата

def get_all_recipes():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT id, author_id, title, description
                FROM "recipe"
            """)
        )

        return result.fetchall()  # Возвращаем все строки результата