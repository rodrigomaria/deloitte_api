import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class TeamMember(models.Model):
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    function = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=256, blank=True, null=True)
    mobile = models.CharField(max_length=21, null=True, blank=True)

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")
