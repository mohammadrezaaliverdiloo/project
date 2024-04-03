from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.views import APIView

from ..serializer.front_serializer import ProductSerialzerFront
from ..models import Product

class FrontProductView(generics.ListAPIView):
    
    queryset = Product.objects.IsPublished()
    serializer_class = ProductSerialzerFront
    
    # def get(self,request):
        
    #     products = Product.objects.IsPublished()
    #     product_serializer = ProductSerialzerFront(instance=products,many=True).data
    #     return Response(product_serializer,status=status.HTTP_200_OK)