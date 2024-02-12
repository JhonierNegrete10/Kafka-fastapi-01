from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.configDatabase import get_db
from kafka_services import kafka_send
from .crud import user_crud
from .models import User, UserCreate

user_route = APIRouter(prefix="/user", tags=["user"])


# Rutas de FastAPI
@user_route.post("/", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_db)):
    # Crear el usuario en la base de datos
    db_user = user_crud.add_user(user, session)

    # Enviar evento a Kafka
    user_event = {"username": user.username, "email": user.email}
    try:
        kafka_send(value=user_event)
    except Exception as e:
        print(f"___ An exception occurred to SEND DATA TO KAFKA:___ \n {e}")

    return db_user


@user_route.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    db_users = user_crud.get_users(skip, limit, session)
    return db_users
