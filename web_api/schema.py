import graphene
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):
    name = graphene.String()
    debug = graphene.Field(DjangoDebug, name='_debug')

    def resolve_name(self, info, **kwargs):
        return "Eventr"


entry_point = graphene.Schema(query=Query)


