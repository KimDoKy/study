from rest_framework import serializers
from .models import Bucket


class BucketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bucket
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
