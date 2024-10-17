from sqlalchemy.orm import Session
from models.business import Business
from schemas.business import BusinessProfile

def create_business(db: Session, business: BusinessProfile):
    db_retaurant = Business(
        restaurant_id = business.business_id,
        email = business.email
    )

    db.add(db_retaurant)
    db.commit()
    db.refresh(db_retaurant)
    return db_retaurant

def get_business(db: Session):
    return db.query(Business).all()