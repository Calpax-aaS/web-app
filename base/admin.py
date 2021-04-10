from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from base.models import User


class AuditModelAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by',)

    def save_model(self, request, obj, form, change):
        if obj.__getstate__()['_state'].adding:
            obj.created_by = request.user
            obj.updated_by = request.user
        if change and obj.id:
            obj.updated_by = request.user
        obj.save()


admin.site.register(User, UserAdmin)
