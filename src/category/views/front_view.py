from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from ..models import Category
from ..serializers.front_serializer import CategoryFrontSerializer

class FrontView(ListAPIView):
    queryset = Category.objects.IsPublished()
    serializer_class = CategoryFrontSerializer
    