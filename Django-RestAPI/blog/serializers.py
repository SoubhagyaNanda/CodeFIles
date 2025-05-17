from rest_framework import serializers
from .models import *

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model= blogComment
        fields = '__all__'

class BlogSrializers(serializers.ModelSerializer):
    class Meta:
        model = blogModels
        fields = '__all__'