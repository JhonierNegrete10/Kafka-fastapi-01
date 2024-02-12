from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


# Define modelos Pydantic
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class UserInDB(User):
    password: str


# Define modelo de base de datos SQLModel
class UserModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
