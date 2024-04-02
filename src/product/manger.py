from django.db import models

class IsPoblished(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset.filter(status='active')