from rest_framework import serializers
from app1.models import Song , Podcast ,Audiobook 

class Song_serializer(serializers.ModelSerializer):
    class Meta:
        model = Song 
        fields = "__all__"
        
class Podcast_serializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"

class Audiobook_serializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = "__all__"


