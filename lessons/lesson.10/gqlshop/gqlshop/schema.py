import graphene

from catalog.schema import Query as CatalogQuery, Mutation as CatalogMutation


class Query(CatalogQuery, graphene.ObjectType):
    pass


class Mutation(CatalogMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
