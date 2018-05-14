import graphene

from .category_schema import Category
from .category_schema import (resolve_category as resolve_category_from_category_schema)
from .category_mutate_schema import ManageCategory
from .sub_category_mutate_schema import ManageSubCategory
from .sub_category_schema import Sub_Category
from .sub_category_schema import (resolve_sub_category as resolve_sub_category_from_sub_category_schema)
from .expense_mutate_schema import ManageExpense
from .expense_schema import Expense
from .expense_schema import (resolve_expense as resolve_expense_from_expense_schema)
from .user_schema import (resolve_user as resolve_user_from_user_schema)
from .user_schema import User


class Mutation(graphene.ObjectType):
    manage_category = ManageCategory.Field()
    manage_sub_category = ManageSubCategory.Field()
    manage_expense = ManageExpense.Field()

class Query(graphene.ObjectType):
    category = graphene.List(Category,user_id=graphene.Int())
    expense = graphene.List(Expense)
    subcategory = graphene.List(Sub_Category,category_id=graphene.Int(), user_id=graphene.Int() )
    user = graphene.List(User)

    def resolve_category(self, info, user_id=None):
        return resolve_category_from_category_schema(info, user_id)

    def resolve_expense(self, info):
        return resolve_expense_from_expense_schema(info)

    def resolve_subcategory(self, info, category_id = None, user_id = None):
        return resolve_sub_category_from_sub_category_schema(info, category_id, user_id)

    def resolve_user(self, info):
        return resolve_user_from_user_schema(info)


schema = graphene.Schema(query=Query, mutation=Mutation)
