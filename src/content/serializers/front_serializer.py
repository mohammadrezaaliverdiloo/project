from rest_framework import serializers

from ..models import Content

class ContentFrontSerializer(serializers.ModelSerializer):
    model=Content
    fiels=['title','content','author','created_at']