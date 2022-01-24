from django import forms
from django.contrib import admin

from apps.team_member.models import TeamMember


class TeamMemberAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid", "created")
    list_display = ("uuid", "created", "name")

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {"address": forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(TeamMember, TeamMemberAdmin)
