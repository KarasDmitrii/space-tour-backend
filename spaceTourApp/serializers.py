from rest_framework import serializers
from .models import MenuItem, Advantage


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('text', 'url')

class AdvantageSerializer(serializers.ModelSerializer):

    class Meta:
         model = Advantage
         fields = ('heading', 'content', 'extra_content', 'description')
