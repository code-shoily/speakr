import graphene
from graphene_django.debug import DjangoDebug

from .auth_schema import RegistrationMutation, LoginMutation


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(RegistrationMutation, LoginMutation):
    pass


entry_point = graphene.Schema(query=Query, mutation=Mutation)
