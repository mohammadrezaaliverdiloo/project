from rest_framework import serializers

from ..models import Content


class ContentAdminSerializer(serializers.ModelSerializer):
    model= Content
    fields= "__all__"