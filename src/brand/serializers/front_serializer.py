from rest_framework import serializers

from ..models import Brand

class BrandFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name','description']