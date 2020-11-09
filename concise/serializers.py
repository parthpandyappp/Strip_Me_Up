from rest_framework import serializers
from .models import stripurl
import pyshorteners

shortner = pyshorteners.Shortener()

class StripUrlSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        x = shortner.tinyurl.short(obj.org_url)
        inst = stripurl.objects.get(pk=obj.pk)
        inst.short_url = x
        inst.save()
        return '{}'.format(x) 

    class Meta:
        model = stripurl
        fields = ['id', 'org_url', 'content']