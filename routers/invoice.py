from fastapi import FastAPI, Depends, Query, Path, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from config.database import get_db
from middlewares.jwt_bearer import JWTBearer
from models.invoice import Invoice as InvoiceModel
from services.invoice import create_invoice, get_invoice, get_invoices
from schemas.invoice import InvoiceGeneration

invoice_router = APIRouter(
    prefix="/invoice",
    tags=['invoices'],
    dependencies=[Depends(JWTBearer())]
)

#Crear una nueva factura
@invoice_router.post("/", response_model=None, status_code=201) #Pendiente agregar el response model
def create_new_invoice(invoice: InvoiceGeneration, db: Session= Depends(get_db)):
    try:
        new_invoice = create_invoice(db, invoice)
        return new_invoice
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))