from rest_framework import serializers
from .models import Bucket

class BucketSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Bucket
        fields = ('id', 'name', 'owner', 'date_crated', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
