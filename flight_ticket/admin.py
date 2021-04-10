from django.contrib import admin

# Register your models here.
from base.admin import AuditModelAdmin
from flight_ticket.models import FlightTicket


@admin.register(FlightTicket)
class StandardAdmin(AuditModelAdmin):
    pass
