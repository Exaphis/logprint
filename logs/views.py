from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from ipware import get_client_ip

from .models import LogCollection, Log


class IndexView(generic.ListView):
    template_name = 'logs/index.html'
    context_object_name = 'collections_list'

    def get_queryset(self):
        """Return all LogCollections, sorted by creation date."""
        return LogCollection.objects.order_by('create_time')


class CollectionDetailView(generic.DetailView):
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


# TODO: log api

@csrf_exempt
def collection_api(request, collection_unique_id=None):
    # TODO: API auth

    if request.method == 'POST':
        if collection_unique_id is not None:
            return HttpResponseBadRequest()
        if 'name' not in request.POST:
            return HttpResponseBadRequest()

        collection = LogCollection()
        collection.owner = get_user_model().objects.all()[0]
        collection.name = request.POST['name']
        collection.save()

        return HttpResponse(201)  # TODO: return location header
    elif request.method == 'PATCH':
        collection = get_object_or_404(LogCollection, unique_id=collection_unique_id)

        log = Log(collection=collection)
        log.ip_addr, _ = get_client_ip(request)
        log.log_text = request.body.decode('utf-8', 'ignore')
        log.save()

        return HttpResponse(status=201)  # TODO: return created log
    elif request.method == 'DELETE':
        collection = get_object_or_404(LogCollection, unique_id=collection_unique_id)
        collection.delete()

        return HttpResponse(status=204)

    return HttpResponseNotAllowed(['POST', 'DELETE'])
