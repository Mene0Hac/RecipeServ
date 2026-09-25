from fastapi import FastAPI
from routes.get_routes import router as get_router

app = FastAPI()

app.include_router(get_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000
    )
    
    
    #