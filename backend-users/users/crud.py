from sqlalchemy.future import select
from sqlalchemy.orm import Session

from .models import UserInDB, UserModel


class UserCRUD:
    def add_user(self, user: UserInDB, session: Session):
        db_user = UserModel(**user.dict())
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    def get_users(self, skip, limit, session: Session):
        statement = select(UserModel).offset(skip).limit(limit)
        result = session.execute(statement)
        result = result.scalars().all()
        return [obj_db for obj_db in result]


user_crud = UserCRUD()
