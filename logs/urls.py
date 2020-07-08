from django.urls import path

from . import views

app_name = 'logs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:collection_unique_id>/', views.CollectionDetailView.as_view(), name='detail'),
    path('api/v1/collection/<uuid:collection_unique_id>/', views.collection_api, name='collection-api'),
    path('api/v1/collection/', views.collection_api, name='collection-api-create')
]
