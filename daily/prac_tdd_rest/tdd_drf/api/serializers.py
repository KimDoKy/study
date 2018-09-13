from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'owner', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
