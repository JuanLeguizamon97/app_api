from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.order import order_router
from routers.user import user_router
from routers.restaurants import restaurant_router
from routers.payments import payment_router
from routers.invoice import invoice_router

app = FastAPI()
app.title = "Restaurants"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(order_router)
app.include_router(user_router)
app.include_router(restaurant_router)
app.include_router(payment_router)
app.include_router(invoice_router)

Base.metadata.create_all(bind=engine)