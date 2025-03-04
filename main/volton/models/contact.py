from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from main.core.models import TimeStampedModel, Currency
from autoslug import AutoSlugField


class Support(TimeStampedModel):
    class Meta:
        verbose_name = _("Support")
        verbose_name_plural = _("Supports")
        ordering = ("-created",)
    full_name = models.CharField(_("Full Name"), max_length=200,)
    body      = models.TextField(_("Content"), blank=True)
    email     = models.CharField(_("Email"), max_length=50)
    tel       = models.CharField(_("Tel"), max_length=50)
    
def __str__(self):
    return self.business_name

def get_dict(self):
    return dict(
        pk = self.pk,
        full_name = self.full_name,
        body = self.body,
        email = self.email,
    )
class Iletisim(TimeStampedModel):
    class Meta:
        verbose_name = _("Mesaj")
        verbose_name_plural = _("Mesajlar")
        ordering = ("-created",)
    full_name = models.CharField(_("Full Name"), max_length=200,)
    body      = models.TextField(_("Content"), blank=True)
    email     = models.CharField(_("Email"), max_length=50)
    tel       = models.CharField(_("Tel"), max_length=50)
def __str__(self):
    return self.business_name

def get_dict(self):
    return dict(
        pk = self.pk,
        full_name = self.full_name,
        body = self.body,
        email = self.email,
    )