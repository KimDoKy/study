# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from . import managers


class Profile(models.Model):
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            related_name='profile',
            verbose_name=_('user'),
            on_delete=models.CASCADE
            )
    interaction = models.PositiveIntegerField(
            default=0,
            verbose_name=_('interaction')
            )
    objects = managers.ProfileManager()

    def username(self):
        return self.user.username

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ('user',)

    def __str__(self):
        return self.user.username
