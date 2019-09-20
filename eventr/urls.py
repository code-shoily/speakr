from django.contrib import admin
from django.urls import path
from django.conf import settings
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=settings.DEBUG)),
]
