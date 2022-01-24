import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=256, blank=False, null=False)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
