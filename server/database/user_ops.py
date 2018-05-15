from .database import db_session
from server.models.user import (User as UserModel)


class Users:
    def authenticate(self, email_id, password):
        user = db_session.query(UserModel).filter((UserModel.email_id == email_id)).one_or_none()
        print('Here')
        if user and user.password == password:
            print('Login')
            return user
        return None

    def identity(self, payload):
        email_id = payload['identity']
        return db_session.query(UserModel).filter(UserModel.email_id == email_id).one_or_none()

    def init_table(self, users):
        for user_data in users:
            user = db_session.query(UserModel).filter((
                UserModel.first_name == user_data["first_name"])).one_or_none()
            if user is None:
                user = UserModel(
                    first_name=user_data["first_name"],
                    last_name=user_data["last_name"],
                    user_name=user_data["user_name"],
                    password=user_data["password"],
                    role=user_data["role"],
                    email_id=user_data["email_id"],
                    last_login=user_data["last_login"],
                    created_by_id=user_data["created_by_id"],
                    updated_by_id=user_data["updated_by_id"])
                db_session.add(user)
            db_session.commit()