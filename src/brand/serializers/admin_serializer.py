from rest_framework import serializers

from ..models import Brand

class BrandSerializer(serializers.ModelSerializer):
   class Meta:
       models = Brand
       fields = ['__all__']