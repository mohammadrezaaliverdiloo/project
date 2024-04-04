from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView

from ..models import Brand
from ..serializers.admin_serializer import BrandSerializer
from ..local_permissions import IsSuperUser

class BrandAdminView(APIView):
    """
    Brand get,put,post,delete
    """
    def get(self,request):
        brands= Brand.objects.all()
        brand_serializer= BrandSerializer(instance= brands,many= True).data
        return Response(brand_serializer,status= status.HTTP_200_OK)
    
    def post(self,request):
        brand_serializer= BrandSerializer(data= request.POST)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return Response(brand_serializer.data,status= status.HTTP_200_OK)
        return Response(brand_serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        brand= Brand.objects.get(pk= pk)
        brand_serializer= BrandSerializer(instance= brand, data= request.data , partial= True)
        if brand_serializer.is_valid():
            return Response(brand_serializer.data, status= status.HTTP_200_OK)
        return Response(brand_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,pk):
    #     brand= Brand.objects.get(pk= pk)
    #     brand.delete()
    #     return Response ({'message':'brand wad deleted'})
    
    class BrandDelete(DestroyAPIView):
        permission_classes= [IsSuperUser]
        queryset= Brand.objects.all()
        serializer_class= BrandSerializer