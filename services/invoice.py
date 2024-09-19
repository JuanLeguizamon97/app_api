from sqlalchemy.orm import Session
from models.invoice import Invoice
from schemas.invoice import InvoiceGeneration

def create_invoice(db: Session, invoice: InvoiceGeneration):
    db_invoice = Invoice(
        invoice_id = invoice.invoice_id
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoice(db:Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.id == invoice_id).first()

def get_invoices(db: Session):
    return db.query(Invoice).all()