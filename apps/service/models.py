import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Service(models.Model):
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
