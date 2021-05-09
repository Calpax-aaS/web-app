from django.contrib import admin

# Register your models here.
from base.admin import AuditModelAdmin
from flight_ticket.forms import LeadOriginForm, CategoryForm
from flight_ticket.models import FlightTicket, LeadOrigin, Category


@admin.register(FlightTicket)
class StandardAdmin(AuditModelAdmin):
    pass


@admin.register(LeadOrigin)
class LeadOriginAdmin(AuditModelAdmin):
    form = LeadOriginForm


@admin.register(Category)
class CategoryAdmin(AuditModelAdmin):
    form = CategoryForm
