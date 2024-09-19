from sqlalchemy.orm import Session
from models.payments import Payment
from schemas.payment import PaymentInfo

def new_payment(db: Session, payment: PaymentInfo):
    db_payment = Payment(
        payment_id = payment.payment_id
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payment(db:Session, payment_id:int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def get_payments(db:Session, user_id: int):
    return db.query(Payment).filter(Payment.user_id == user_id).all()