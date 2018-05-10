from .database import db_session
from server.models.category import (Category as CategoryModel)


class Categorys:
    def init_table(self, categorys):
        for category_data in categorys:
            category = db_session.query(CategoryModel).filter((
                CategoryModel.category_name == category_data["category_name"])).one_or_none()
            if category is None:
                category = CategoryModel(
                         category_name=category_data["category_name"],
                         user_id=category_data["user_id"])
                db_session.add(category)
            db_session.commit()

    def insert_category(self, category):
        category = CategoryModel(
                        category_name=category.category_name,
                        user_id=category.user_id
                        )
        db_session.add(category)
        db_session.commit()
        return category
