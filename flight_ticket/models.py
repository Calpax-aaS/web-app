from django.db import models

# Create your models here.
from base.models import AuditModel


class FlightTicket(AuditModel):
    reference = models.CharField(max_length=20)
