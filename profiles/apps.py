from __future__ import unicode_literals
from django.apps import AppConfig


class ProfileConfig(AppConfig):
    name = "profiles"
    verbose_name = "Profile utilisateurs"

    def ready(self):
        from . import signals  # noqa
