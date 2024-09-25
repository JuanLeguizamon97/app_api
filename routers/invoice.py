from fastapi import FastAPI, Depends, Query, Path, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from config.database import get_db
from middlewares.jwt_bearer import JWTBearer
from models.invoice import Invoice as InvoiceModel
from services.invoice import create_invoice, get_invoice, get_invoices, update_invoice, delete_invoice, get_invoices_by_business
from schemas.invoice import InvoiceGeneration, InvoiceResponse

invoice_router = APIRouter(
    prefix="/invoice",
    tags=['invoices'],
    dependencies=[Depends(JWTBearer())]
)

# Crear una nueva factura
@invoice_router.post("/", response_model=InvoiceResponse, status_code=201)
def create_new_invoice(invoice: InvoiceGeneration, db: Session = Depends(get_db)):
    try:
        new_invoice = create_invoice(db, invoice)
        return JSONResponse(status_code=201, content={'message': 'Factura creada correctamente', 'data': new_invoice})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Obtener facturas por user_id
@invoice_router.get("/user/{user_id}", response_model=list[InvoiceResponse])
def get_invoices_per_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user_invoices = get_invoices(db, user_id)
        return JSONResponse(status_code=200, content={'message': 'Facturas encontradas', 'data': user_invoices})
    except Exception as e:
        raise HTTPException(status_code=404, detail='No se encontraron facturas para este usuario')

# Obtener facturas por business_id
@invoice_router.get("/business/{business_id}", response_model=list[InvoiceResponse])
def get_invoices_per_business(business_id: int, db: Session = Depends(get_db)):
    try:
        business_invoices = get_invoices_by_business(db, business_id)
        return JSONResponse(status_code=200, content={'message': 'Facturas encontradas', 'data': business_invoices})
    except Exception as e:
        raise HTTPException(status_code=404, detail='No se encontraron facturas para este negocio')

# Modificar una factura
@invoice_router.put("/{invoice_id}", response_model=InvoiceResponse)
def update_existing_invoice(invoice_id: int, invoice: InvoiceGeneration, db: Session = Depends(get_db)):
    try:
        updated_invoice = update_invoice(db, invoice_id, invoice)
        return JSONResponse(status_code=200, content={'message': 'Factura actualizada correctamente', 'data': updated_invoice})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Eliminar una factura
@invoice_router.delete("/{invoice_id}", status_code=204)
def delete_invoice_by_id(invoice_id: int, db: Session = Depends(get_db)):
    try:
        delete_invoice(db, invoice_id)
        return JSONResponse(status_code=204, content={'message': 'Factura eliminada correctamente'})
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
