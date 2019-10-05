from django.db import models
from django.contrib.auth import get_user_model

from common.base_models import BaseModel, AuthStampedModel


class Organization(BaseModel):
    """
    Organization is the group that manages the event. For example, PyCon is an organization in this context.
    """
    name = models.CharField(max_length=31)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Membership(BaseModel):
    """
    Membership model for an organization. This model serves as dual purpose of invitation and member model.

    When there is no acceptation date and user model, then the object is an invitation. Otherwise, it represents member
    """
    ROLES = (
        ('0', 'Organizer'),
        ('1', 'Moderator'),
        ('2', 'Member'),
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    member = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField()
    role = models.CharField(max_length=1, choices=ROLES)
    accepted_on = models.DateTimeField(null=True)

    @property
    def invitation_date(self):
        return self.created_at

    @property
    def invited_by(self):
        return self.created_by

    @property
    def has_accepted_invitation(self):
        return bool(self.accepted_on)

    def __str__(self):
        return f'{self.email} on {self.invitation_date}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.member = Membership.objects.select_related('user', 'organization').filter(
                user__email=self.email,
                organization=self.organization).first() or None

        return super().save(*args, **kwargs)
