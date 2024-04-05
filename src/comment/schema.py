import graphene
from graphene_django import DjangoObjectType

from ..comment.models import Comment

class CommentType(DjangoObjectType):
    class Meta:
        models= Comment
        fields= ("id","user","product","content")
        
class CommentQuery(graphene.ObjectType):
    all_comments = graphene.List(CommentType,product= graphene.String(required=True))
    
    def resolver_all_comments(root,info,product):
        try:
            return Comment.objects.get(product= product)
        except Comment.DoesNotExist:
            return None
        
CommentSchema= graphene.Schema(query= CommentQuery)        