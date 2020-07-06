from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import LogCollection, Log


class IndexView(generic.ListView):
    template_name = 'logs/index.html'
    context_object_name = 'collections_list'

    def get_queryset(self):
        """Return all LogCollections, sorted by creation date."""
        return LogCollection.objects.order_by('create_time')


def view_collection(request, collection_unique_id):
    collection = get_object_or_404(LogCollection, unique_id=collection_unique_id)
    logs = Log.objects.filter(collection=collection)
    context = {'collection': collection, 'logs': logs}
    return render(request, 'logs/view_collection.html', context)
