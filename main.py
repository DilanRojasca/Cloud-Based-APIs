from fastapi import FastAPI
from .database import engine, Base
from .controllers import router

# Inicializa la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
