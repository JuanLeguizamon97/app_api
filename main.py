from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.order import order_router

app = FastAPI()
app.title = "Restaurants"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(order_router)

Base.metadata.create_all(bind=engine)