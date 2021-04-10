import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from config import settings


class AuditModel(models.Model):
    """To track by who and when was the last record modified"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_%(class)s_set',
                                   null=True, blank=True, verbose_name='Created By',
                                   on_delete=models.CASCADE)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_%(class)s_set',
                                   null=True, blank=True, verbose_name='Updated By',
                                   on_delete=models.CASCADE)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass
