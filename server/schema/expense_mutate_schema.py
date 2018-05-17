import graphene
from .expense_schema import Expense, update_expense, delete_expense
from server.database.expense_ops import Expenses


class ExpenseInput(graphene.InputObjectType):
    id=graphene.Int()
    sub_category_id=graphene.Int()
    item=graphene.String()
    unit=graphene.String()
    quantity=graphene.String()
    provider=graphene.String()
    price=graphene.String()
    category_id=graphene.Int()
    user_id=graphene.Int()
    flag=graphene.String()

class ManageExpense(graphene.Mutation):
    class Arguments:
        expense_data = ExpenseInput()

    expense = graphene.Field(Expense)

    @staticmethod
    def mutate(root, info, expense_data=None):
        if expense_data.id is None:
            expense = Expense(
                id=expense_data.id,
                sub_category_id=expense_data.sub_category_id,
                item=expense_data.item,
                unit=expense_data.unit,
                quantity=expense_data.quantity,
                provider=expense_data.provider,
                price=expense_data.price,
                category_id=expense_data.category_id,
                user_id=expense_data.user_id
            )
            create = Expenses()
            expenses = create.insert_expense(expense)
            return ManageExpense(expense=expenses)
        elif expense_data.flag is not None:
            expense_delete = delete_expense( info , id=expense_data.id)
            return ManageExpense(expense=expense_delete)
        else:
            expense_edit = update_expense(  info,
                                            id=expense_data.id,
                                            sub_category_id=expense_data.sub_category_id,
                                            item=expense_data.item,
                                            unit=expense_data.unit,
                                            quantity=expense_data.quantity,
                                            provider=expense_data.provider,
                                            price=expense_data.price,
                                            category_id=expense_data.category_id,
                                            user_id=expense_data.user_id)
            return ManageExpense(expense=expense_edit)
