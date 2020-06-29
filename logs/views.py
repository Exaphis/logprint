from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import LogCollection


# Create your views here.
def index(request):
    collections_list = LogCollection.objects.order_by('create_time')
    context = {'collections_list': collections_list}
    return render(request, 'logs/index.html', context)


def view_collection(request, collection_unique_id):
    collection = get_object_or_404(LogCollection, unique_id=collection_unique_id)
    return HttpResponse(f'Collection id: {collection_unique_id}')
