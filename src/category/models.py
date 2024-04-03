from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import IsPublished

class Category(models.Model):
    
    class CategoryStatus(models.TextChoices):
        ACTIVE = 'active'
        INACTIVE = 'disable'
    name = models.CharField(max_length=255,verbose_name=_('name'),help_text="name for categories")
    slug = models.SlugField(unique=True,max_length=255,verbose_name=_('slug'))
    description = models.TextField(verbose_name=_('description'),help_text="description for category")
    status = models.Choices(verbose_name=_('status'),choices=CategoryStatus.choice,default=CategoryStatus.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('create time'))
    modified_at = models.DateTimeField(auto_add=True,verbose_name=_('modified time'))
    # image =models.ForeignKey()
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ('-modified_at',)
        
    objects = IsPublished()