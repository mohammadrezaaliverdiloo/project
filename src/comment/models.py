from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# from user.models import User

from ..product.models import Product

class Comment (models.Model):
    
    class StatusChoice(models.TextChoices):
        ACTIVE= 'active'
        
        
    user= models.ForeignKey(
        settings.AUTH_MODEL_USER,related_name="user_comment",verbose_name=_("user"),help_text=_("user who leave comment")
                            )
    product= models.ForeignKey(
        Product,related_name="product_comment",verbose_name=_("products comment"),help_text=_("products comment leave for")
                               )
    content= models.TimeField()
    created_at= models.DateTimeField(auto_now_add=True,verbose_name=_("create_time"),help_text=_("Date of leave comment"))
    created_at= models.DateTimeField(auto_now=True,verbose_name=_("modified_time"),help_text=_("Date of modified comment")) 
    
    def __str__(self) -> str:
        return f"{user} - {product}"