from django.db import models
from django.utils.translation import gettext_lazy as _

from managers import IsPublished

class Brand (models.Model):    
    name= models.CharField(max_length=255,verbose_name=_("name"),help_text=_("name for brand"))
    description= models.TextField(verbose_name=_("description"),help_text=_("description for brand"))
    created_at= models.DateTimeField(auto_now_add=True,verbose_name=_("create_time"))
    created_at= models.DateTimeField(auto_now=True,verbose_name=_("modified_time"))
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table= "brand"
        verbose_name= "brand"
        verbose_name_plural= "brands"
        ordering= ('name',)