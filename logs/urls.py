from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('collections', views.LogCollectionViewSet)
router.register('logs', views.LogViewSet)

# app_name = 'logs'
urlpatterns = [
    path('', include(router.urls))
    # path('', views.IndexView.as_view(), name='index'),
    # path('<uuid:collection_unique_id>/', views.CollectionDetailView.as_view(), name='detail'),
    # path('api/v1/collection/<uuid:collection_unique_id>/', views.collection_api, name='collection-api'),
    # path('api/v1/collection/', views.collection_api, name='collection-api-create')
]
