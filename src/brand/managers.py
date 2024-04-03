from django.db import models

class IsPublished(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status='active')