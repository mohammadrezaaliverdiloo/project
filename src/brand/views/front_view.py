from  rest_framework.generics import ListAPIView

from ..models import Brand
from ..serializers.front_serializer import BrandFrontSerializer
from ..managers import IsPublished

class BrandFrontView(ListAPIView):
    queryset= Brand.objects.IsPublished()
    serializer_class= BrandFrontSerializer
