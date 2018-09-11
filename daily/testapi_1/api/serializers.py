from rest_framework import serializers
from .models import Bucketlist
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified', 'owner')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    bucketlists = serializers.PrimaryKeyRelatedField(
            many=True, queryset=Bucketlist.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlists')
