from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from mainapp.models import Category
from .permissions import OnlyForOneUser
# from .v1.serializers import CategoryModelSerializer
# from .v2.serializers import CategoryModelSerializer as CategoryModelSerializerOther
from .serializers import get_serializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    # serializer_class = CategoryModelSerializer
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [OnlyForOneUser]

    def get_serializer_class(self):
        version = self.request.version
        # if version == 'v2.0':
        #     return CategoryModelSerializerOther
        # return CategoryModelSerializer
        return get_serializer(version)
