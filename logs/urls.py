from django.urls import path

from .views import IndexView, CollectionView

app_name = 'logs'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<uuid:collection_unique_id>/', CollectionView.as_view(), name='view-collection')
]
