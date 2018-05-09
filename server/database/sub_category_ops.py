from .database import db_session
from server.models.sub_category import (Sub_Category as Sub_CategoryModel)


class Sub_Categorys:
    def init_table(self, SubCategorys):
        for SubCategory_data in SubCategorys:
            sub_category = db_session.query(Sub_CategoryModel).filter((
                Sub_CategoryModel.sub_category_name == SubCategory_data["sub_category_name"])).one_or_none()
            if sub_category is None:
               sub_category = Sub_CategoryModel(
                      category_id=SubCategory_data["category_id"],
                      sub_category_name=SubCategory_data["sub_category_name"])
               db_session.add(sub_category)
            db_session.commit()

    def insert_subcategory(self, subcategory):
        subcategory = Sub_CategoryModel(
            category_id=subcategory.category_id,
            sub_category_name=subcategory.sub_category_name)
        db_session.add(subcategory)
        db_session.commit() 
        return subcategory