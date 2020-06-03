from .models import Group
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ('group_name', 'creater')