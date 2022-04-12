from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from core.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
    
    