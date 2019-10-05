import uuid

from django.db import models
from django.contrib.auth import get_user_model


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuthStampedModel(models.Model):
    created_by = models.ForeignKey(
        get_user_model(), related_name='+', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        get_user_model(), related_name='+', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel, AuthStampedModel, UUIDModel):
    class Meta:
        abstract = True
