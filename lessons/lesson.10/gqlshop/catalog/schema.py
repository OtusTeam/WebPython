import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.Node, )


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class CartMutation(graphene.Mutation):

    class Arguments:
        product_id = graphene.Int(required=True)
        quantity = graphene.Int(required=True)

    result = graphene.Boolean()
    cart = graphene.List(ProductType)

    def mutate(self, info, product_id, quantity):
        # TODO
        return {
            'result': True,
            'cart': Product.objects.all()[:2],
        }


class Mutation:
    add_to_cart = CartMutation.Field()
    # delete_from_cart


class Query:

    # all_categories = graphene.List(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)
    all_products = graphene.List(ProductType)

    # category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())
    product = graphene.Field(ProductType, id=graphene.Int())

    products = graphene.List(ProductType, first=graphene.Int())
    #
    # def resolve_all_categories(self, info, **kwargs):
    #     return Category.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.select_related('category').all()

    def resolve_category(self, info, **kwargs):
        if 'id' in kwargs:
            return Category.objects.get(id=kwargs['id'])
        if 'name' in kwargs:
            return Category.objects.get(name=kwargs['name'])

    def resolve_product(self, info, **kwargs):
        if 'id' in kwargs:
            return Product.objects.select_related('category').get(id=kwargs['id'])

    def resolve_products(self, info, **kwargs):
        if 'first' in kwargs:
            return Product.objects.select_related('category').all()[:kwargs['first']]
