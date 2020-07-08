from django.views import generic

from .models import LogCollection, Log


class IndexView(generic.ListView):
    template_name = 'logs/index.html'
    context_object_name = 'collections_list'

    def get_queryset(self):
        """Return all LogCollections, sorted by creation date."""
        return LogCollection.objects.order_by('create_time')


class CollectionView(generic.DetailView):
    template_name = 'logs/view_collection.html'
    context_object_name = 'collection'
    model = LogCollection

    def get_object(self, queryset=None):
        if queryset is not None:
            return queryset.get(unique_id=self.kwargs['collection_unique_id'])
        return LogCollection.objects.get(unique_id=self.kwargs['collection_unique_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logs'] = Log.objects.filter(collection=kwargs['object'])
        return context
