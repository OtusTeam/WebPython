import graphene
from graphene_django import DjangoObjectType
from faker import Faker
from mainapp.models import Category, Animal


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class AnimalType(DjangoObjectType):
    class Meta:
        model = Animal
        fields = "__all__"

class Query(graphene.ObjectType):
    by = graphene.String(default_value="Hi!")
    hello = graphene.String()
    category_list = graphene.List(CategoryType)
    # category_list = graphene.relay.ConnectionField(CategoryType)
    animal_list = graphene.List(AnimalType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))


    def resolve_hello(self, info):
        fake = Faker()
        return fake.name()

    def resolve_category_list(self, info):
        return Category.objects.all()

    def resolve_animal_list(self, info):
        return Animal.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)


# class ItemType(DjangoObjectType):
#     class Meta:
#         model = Item
#         fields = ("id", "name", "description")
#
# class Query(graphene.ObjectType):
#     items = graphene.relay.ConnectionField(ItemType)
#
#     def resolve_items(self, info, **kwargs):
#         # Здесь можно добавить дополнительные параметры фильтрации и сортировки
#         return Item.objects.all()
#
# schema = graphene.Schema(query=Qu