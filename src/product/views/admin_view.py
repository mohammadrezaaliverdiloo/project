from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication,permissions

from ..serializer.admin_serializer import ProductSerializers
from ..models import Product



class ProductView(APIView):
    
    """"
    view all product,create,update,delete product for admin
    login required
    is admin required
    """
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    
    def get(self,request):
        
        '''
        return a all of product
        '''
        products = Product.objects.all()
        product_serializer = ProductSerializers(instance= products,many=True).data
        return Response (product_serializer,status=status.HTTP_200_OK)
    
    def post(self,request):
        """
        create a product
        """
        product_serializer = ProductSerializers(data= request.POST)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data,status= status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status= status.HTTP_400_BAD_REQUEST)  


    def put(self,request,pk):
        """
        update a product
        """
        product = Product.objects.get(pk= pk)
        product_serializer = ProductSerializers(instance= product, data= request.data, partial= True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status= status.HTTP_200_OK)
        return Response (product_serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk):
        product = Product.object.get(pk= pk)
        product.delete()
        return Response({'messagw':'product delete'})
        
        
        
        
        