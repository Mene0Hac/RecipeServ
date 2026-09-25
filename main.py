import sqlQuery

from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()

#app.include_router(get_router)



@app.get("/get_all_users")
def get_all_users_route():
    users = sqlQuery.get_all_users()

    return [
        {
            "id": user.id,
            "username": user.username,
            "password_hash": user.password_hash,
            "is_admin": user.is_admin,
            "is_banned": user.is_banned
        }
        for user in users
    ]


@app.get("/get_all_recipes")
def get_all_recipes_route():
    recipes = sqlQuery.get_all_recipes()

    return [
        {
            "id": recipe.id,
            "author_id": recipe.author_id,
            "title": recipe.title,
            "description": recipe.description
        }
        for recipe in recipes
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000
    )
