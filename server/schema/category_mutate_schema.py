import graphene
from .category_schema import Category
from server.database.category_ops import Categorys


class CategoryInput(graphene.InputObjectType):
    category_name = graphene.String()
    user_id = graphene.Int()

class ManageCategory(graphene.Mutation):
    class Arguments:
        category_data = CategoryInput()

    category = graphene.Field(Category)

    @staticmethod
    def mutate(root, info, category_data=None):
        category = Category(
            category_name=category_data.category_name,
            user_id=category_data.user_id
        )
        create = Categorys()
        categorys = create.insert_category(category)
        return ManageCategory(category=categorys)
