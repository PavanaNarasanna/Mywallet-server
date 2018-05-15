import graphene
from .sub_category_schema import Sub_Category, update_sub_category
from server.database.sub_category_ops import Sub_Categorys


class SubCategoryInput(graphene.InputObjectType):
    id = graphene.Int()
    category_id = graphene.Int()
    sub_category_name = graphene.String()
    user_id = graphene.Int()
    

class ManageSubCategory(graphene.Mutation):
    class Arguments:
        sub_category_data = SubCategoryInput()

    sub_category = graphene.Field(Sub_Category)

    @staticmethod
    def mutate(root, info, sub_category_data=None):
        if sub_category_data.id is None:
            sub_category = Sub_Category(
                id=sub_category_data.id,
                category_id=sub_category_data.category_id,
                sub_category_name=sub_category_data.sub_category_name,
                user_id=sub_category_data.user_id
            )
            create = Sub_Categorys()
            sub_categorys = create.insert_subcategory(sub_category)
            return ManageSubCategory(sub_category=sub_categorys)
        else:
            sub_category_edit = update_sub_category(info,
                                                    id=sub_category_data.id,
                                                    category_id=sub_category_data.category_id,
                                                    sub_category_name=sub_category_data.sub_category_name,
                                                    user_id=sub_category_data.user_id)
            return ManageSubCategory(sub_category=sub_category_edit)
