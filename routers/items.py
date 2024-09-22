from fastapi import APIRouter, Depends, HTTPException, status
from models.items import ItemModel
from schemas.items import ItemCreateResponse
from config.database import get_db  # Asegúrate de tener tu conexión a la base de datos configurada
from sqlalchemy.orm import Session
from middlewares.jwt_bearer import JWTBearer  # Para la autenticación JWT

item_router = APIRouter(
    prefix="/restaurants/{restaurant_id}/items",
    tags=["items"],
    dependencies=[Depends(JWTBearer())]  # Autenticación JWT
)

# Crear un nuevo item
@item_router.post("/", response_model=ItemCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_item(restaurant_id: int, item: ItemModel, db: Session = Depends(get_db)):
    # Lógica para añadir el item a la base de datos
    new_item = Item(restaurant_id=restaurant_id, **item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item