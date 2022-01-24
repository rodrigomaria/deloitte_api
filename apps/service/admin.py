from django import forms
from django.contrib import admin

from apps.service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid", "created")
    list_display = ("uuid", "created", "title")

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {"description": forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(Service, ServiceAdmin)
