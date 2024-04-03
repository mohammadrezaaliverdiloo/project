from rest_framework import serializers

from ..models import Product

class ProductSerialzerFront(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(many=True)
    prices = serializers.StringRelatedField(many=True)
    quantity = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)
    colors = serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Product
        fields=['name','description','prices','categories','brand','quantity','colors']