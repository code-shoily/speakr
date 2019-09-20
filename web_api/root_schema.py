import graphene
from django.contrib.auth import get_user_model

from web_api.auth_schema import UserType


class RootType(graphene.ObjectType):
    user_info = graphene.Field(UserType)


class RootQuery(graphene.AbstractType):
    me = graphene.Field(RootType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return {
            "user_info": user
        }
