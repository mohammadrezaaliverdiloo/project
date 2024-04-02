from rest_framework.views import APIView
from rest_framework import authentication,permissions

from ..serializer.admin_serializer import ProdoctSerializers

class ProductView(APIView):
    
    """"
    view all product,create,update,delete product for admin
    login required
    is admin required
    """
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    
    def get(self,request,format=None):
        
        '''
        return a all of product
        '''
        pass