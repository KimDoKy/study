from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Todo
        fields = ('id', 'name', 'owner', 'created', 'modified')
        read_only_fields = ('created', 'modified')
