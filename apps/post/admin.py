from django import forms
from django.contrib import admin

from apps.post.models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("uuid", "created")
    list_display = ("uuid", "created")

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {"content": forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(Post, PostAdmin)
