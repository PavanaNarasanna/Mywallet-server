from graphene.types.dynamic import Dynamic
from graphene.types.options import Options
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene_sqlalchemy.registry import get_global_registry
from graphene_sqlalchemy.types import construct_fields


class FilterableConnectionField(SQLAlchemyConnectionField):
    RELAY_ARGS = ['first', 'last', 'before', 'after']

    def __init__(self, type, *args, **kwargs):
        options = Options(
            meta=None,  # attrs.pop('Meta', None),
            name=type._meta.name,  # name,
            description=None,  # attrs.pop('__doc__', None),
            model=type._meta.model,  # None,
            local_fields=None,
            only_fields=(),
            exclude_fields=('password', 'search_vector'),
            id='id',
            interfaces=(),
            registry=get_global_registry(),
            fields=(),
        )
        fields = construct_fields(options)
        for field_name, field_type in fields.items():
            if hasattr(field_type, 'kwargs') and 'required' in field_type.kwargs:
                field_type.kwargs['required'] = False
            if not isinstance(field_type, Dynamic):  # and field_name != 'id':
                kwargs.setdefault(field_name, field_type)
        super(FilterableConnectionField, self).__init__(type, *args, **kwargs)

    @classmethod
    def get_query(cls, model, context, info, args):
        query = super(FilterableConnectionField, cls).get_query(model, context, info, args)
        for field, value in args.items():
            if field not in cls.RELAY_ARGS:
                query = query.filter(getattr(model, field) == value)
        return query
