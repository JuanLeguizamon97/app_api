from sqlalchemy.orm import Session
from models.restaurant import Restaurants
from schemas.restaurant import RestaurantProfile

def create_restaurant(db: Session, restaurant: RestaurantProfile):
    db_retaurant = Restaurants(
        restaurant_id = restaurant.restaurant_id,
        email = restaurant.email
    )

    db.add(db_retaurant)
    db.commit()
    db.refresh(db_retaurant)
    return db_retaurant

def get_restaurants(db: Session):
    return db.query(Restaurants).all()