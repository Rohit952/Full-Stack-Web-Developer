from rest_framework import serializers

from .models import Webpage

class WebpageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Webpage
        fields = ('name', 'url')