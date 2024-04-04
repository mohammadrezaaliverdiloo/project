from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView

from ..models import Category
from ..serializers.admin_serializer import CategorySerializer
from ..local_permissions import IsSuperUser

class CategoryAdminView(APIView):
    """"
    view for get,post,put,delete
    """
    def get(self,request):
        products = Category.objects.all()
        category_srializer = CategorySerializer(instance=products,many=True).data
        return Response(category_srializer,status=status.HTTP_200_OK)
    
    def post(self,request):
        category_serializer = CategorySerializer(data = request.Post)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response (category_serializer.data,status=status.HTTP_200_OK)
        return Response(category_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk):
        category = Category.objects.get(pk=pk)
        category_serializer = CategorySerializer(instance=category,data=request.data,partial=True)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data,status=status.HTTP_200_OK)
        return Response(category_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,pk):
    #     category = Category.objects.get(pk=pk)
    #     category.delete()
    #     return Response({'message':'category was deleted'})

class DeletCategory(DestroyAPIView):
    
    permission_classes= [IsSuperUser]
    queryset= Category.objects.all()
    serializer_class= CategorySerializer        
        