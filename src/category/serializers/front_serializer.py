from rest_framework import serializers

from ..models import Category

class CategoryFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        feilds= ['name','description']