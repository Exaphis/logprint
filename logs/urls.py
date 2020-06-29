from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<uuid:collection_unique_id>/', views.view_collection, name='view-collection')
]
