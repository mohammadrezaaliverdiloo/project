from django.db import models
from django.utils.translation import gettext_lazy as _
# import datetime


from category.models import Category
from warehouse.models import Quantity
from brand.models import Brand
from price.models import Price
from manger import IsPoblished

class Product(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active"
        IN_ACTIVE = "in_active"
        DELETE = "delete"
        
    
    name = models.CharField(verbose_name = _("name"),max_length=255,null=False,help_text="not more than 255 character")
    description = models.TextField(verbose_name = _("description"),null=True,help_text="a bit or more descriprtion about product")
    brand = models.ForeignKey(Brand,_("brand"),related_name="brand",on_delete = models.CASCADE,help_text="barnd of product")
    price = models.ForeignKey(Price,related_name="prices",verbose_name=_("price"),on_delete = models.CASCADE)
    quantity = models.ForeignKey(Quantity,related_name="quantity",verbose_name=_("quantity"),on_delete = models.CASCADE)
    category = models.ForeignKey(Category,related_name="categories",verbose_name=_("category"),on_delete = models.CASCADE)
    color=models.ForeignKey(to='Color',related_name="colors",verbose_name=_("brand"),on_delete = models.CASCADE)
    material = models.CharField(verbose_name = _("material"),max_length=255,null=False)
    weight = models.FloatField()
    dimensions =models.FloatField()
    tags=models.CharField(max_length=255,verbose_name=_("tags"))
    #image //create an image app 
    status = models.CharField(_("status"),choices=Status.choices,default=Status.IN_ACTIVE)
    date_created=models.DateTimeField(auto_now_add = True,verbose_name=_("created_at"))
    date_modified=models.DateTimeField(auto_now=True,verbose_name=_("modified_at"))

    class Meta:
        verbose_name="product"
        verbose_name_plural="products"
        db_table="products"
        ordering = ('name',)


    def __str__(self):
        return f"{self.name}-{self.brand}"
    
    objects =IsPoblished()



class Color(models.Model):
    name =models.CharField(_("color_name"),max_length=255)
    code = models.CharField(_("color_code"),max_length=255)
