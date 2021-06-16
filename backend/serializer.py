from django.db import models
from rest_framework import serializers
from .models import Wiki

class WikiSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%B %d, %Y %H:%M')

    class Meta:
        model = Wiki
        fields = ('id', 'title', 'link' ,'content', 'no_of_image', 'no_of_link', 'created_on')