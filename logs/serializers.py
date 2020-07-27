from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import LogCollection, Log


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="logs:user-detail")

    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email']


class LogCollectionSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.HyperlinkedIdentityField(view_name="logs:user-detail")

    class Meta:
        model = LogCollection
        fields = ['unique_id', 'owner', 'name', 'create_time']


class LogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Log
        fields = ['collection', 'log_text', 'ip_addr', 'received_time']
