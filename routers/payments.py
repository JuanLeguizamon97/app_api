from fastapi import FastAPI, Depends, Path, Query, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import get_db
from middlewares.jwt_bearer import JWTBearer
from models.payments import Payment as PaymentModel
from services.payments import new_payment, get_payment, get_payments
from schemas.payment import PaymentInfo, PaymentCreate

payment_router = APIRouter(
    prefix="/payments",
    tags=['payments'],
    dependencies=[Depends(JWTBearer())]
)

#Crear nuevo pago
@payment_router.post("/", response_model=None, status_code=201)
def create_new_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    try:
        new_payment_creation = new_payment(db, payment)
        return new_payment_creation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))