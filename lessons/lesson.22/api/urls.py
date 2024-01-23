from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import CategoryViewSet
from api import api_views, generic_views, filter_views, pagination_views, view_sets

app_name = 'api'

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('base', view_sets.CategoryViewSet, basename='base')
router.register('model', view_sets.CategoryModelViewSet, basename='model')
router.register('custom', view_sets.CategoryCustomViewSet, basename='custom')

# filter
router.register('queryset', filter_views.CategoryQuerysetFilterViewSet, basename='queryset')
router.register('param', filter_views.CategoryParamFilterViewSet, basename='param')
router.register('django', filter_views.CategoryDjangoFilterViewSet, basename='django')
router.register('custom-django', filter_views.CategoryCustomDjangoFilterViewSet, basename='custom-django')

# pagination
router.register('pagenumber', pagination_views.CategoryPageNumberPaginatonViewSet, basename='pagenumber')
router.register('limitoffset', pagination_views.CategoryLimitOffsetPaginatonViewSet, basename='limitoffset')

urlpatterns = [
    # API views
    path('views/api-view/', api_views.CategoryAPIVIew.as_view()),
    path('views/func-api-view/', api_views.category_view),
    # generic views
    path('generic/create/', generic_views.CategoryCreateAPIView.as_view()),
    path('generic/list/', generic_views.CategoryListAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', generic_views.CategoryRetrieveAPIView.as_view()),
    path('generic/destroy/<int:pk>/', generic_views.CategoryDestroyAPIView.as_view()),
    path('generic/update/<int:pk>/', generic_views.CategoryUpdateAPIView.as_view()),
    # view sets
    path('viewsets/', include(router.urls)),
    # filters
    # path('filters/', include(filter_router.urls)),
    path('filters/kwargs/<str:name>/', filter_views.CategoryKwargsFilterView.as_view()),

]
