from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime


from category.models import Category
from warehouse.models import Quantity
from brand.models import Brand
from price.models import Price

class Product(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active"
        IN_ACTIVE = "in_active"
        DELETE = "delete"
        
    
    name = models.CharField(verbose_name = _("name"),max_length=255,null=False,help_text="not more than 255 character")
    description = models.TextField(verbose_name = _("description"),null=True,help_text="a bit or more descriprtion about product")
    brand = models.ForeignKey(Brand,_("brand"),on_delete = models.CASCADE,help_text="barnd of product")
    price = models.ForeignKey(Price,verbose_name=_("price"),on_delete = models.CASCADE)
    quantity = models.ForeignKey(Quantity,verbose_name=_("quantity"),on_delete = models.CASCADE)
    category = models.ForeignKey(Category,verbose_name=_("category"),on_delete = models.CASCADE)
    color=models.ForeignKey(to='Color',verbose_name=_("brand"),on_delete = models.CASCADE)
    material = models.CharField(verbose_name = _("material"),max_length=255,null=False)
    weight = models.FloatField()
    dimensions =models.FloatField()
    # tags=model
    # image
    # status
    # date_created
    # date_modified
class Color(models.Model):
    name =models.CharField(_("color_name"),max_length=255)
    code = models.CharField(_("color_code"),max_length=255)
