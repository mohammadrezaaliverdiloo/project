import graphene

from ..comment.schema import CommentSchema

class Query(CommentSchema,graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query)