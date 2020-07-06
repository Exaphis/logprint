from django.urls import path

from . import views

app_name = 'logs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:collection_unique_id>/', views.view_collection, name='view-collection')
]
