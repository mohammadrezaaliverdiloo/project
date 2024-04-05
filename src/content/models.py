from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from category.models import Category
class Content(models.Model):
    
    class ContentStatus(models.TextChoice):
        PUBLISHED= 'publishe'
        DRAFT= 'draft'
    
    title= models.CharField(max_length=255,verbose_name=_("title"),help_text=_("title for content"))
    content= models.TextField(verbose_name=_("content"),help_text=_("write content"))
    category= models.ForeignKey(
        Category,related_name="category-content",verbose_name=_("category"),help_text=_("category for content")
        )
    author= models.ForeignKey(
        settings.AUTH_USER_MODEL,related_name="author-content",verbose_name=_("author"),help_text=_("author for content")
        )
    status= models.CharField(
        choices=ContentStatus.choices,default=ContentStatus.PUBLISHED,verbose_name=_("content"),help_text=_("write content")
                             )
    created_at= models.DateTimeField(auto_now_add=True,verbose_name=_("create time"),help_text=_(" I Filled auotomaticly"))
    modified_at= models.DateTimeField(auto_now=True,verbose_name=_("modified time"),help_text=_(" Fill me"))