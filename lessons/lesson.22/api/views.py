from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from mainapp.models import Category
from .permissions import OnlyForOneUser
from .serializers import CategoryModelSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [OnlyForOneUser]