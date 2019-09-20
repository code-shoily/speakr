import graphql_jwt
from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType


class LoginInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        input = LoginInput(required=True)

    def mutate(self, info, input):
        first_name = input.get("first_name")
        last_name = input.get("last_name")
        password = input.get("password")
        email = input.get("email")
        username = input.get("username")

        user = get_user_model()(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class RegistrationMutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class LoginMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
