
from sqlalchemy import create_engine, false, text

# Данные для подключения к MySQL
DB_URL = "mysql+pymysql://root:2289@localhost:3456/test_db"

engine = create_engine(DB_URL)

def add_user(name, age):
    with engine.connect() as connection:
        connection.execute(
            text("""
                INSERT INTO test_db.students (name, age)
                VALUES (:name, :age)
            """),
            {
                "name": name,
                "age": age
            }
        )

        connection.commit()

    print("Пользователь успешно добавлен!")

def get_all_users():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT id, name, age FROM students")
        )

        return result.fetchall()  # Возвращаем все строки результата
        
        for row in result:
            print(f"ID: {row.id}, Имя: {row.name}, Возраст: {row.age}")

