from students.models import Students
from rest_framework import serializers
from employee.models import Employees
from blog.models import blogComment, blogModels

class studentsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Students
        fields= '__all__'

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model= Employees
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model= blogComment
        fields = '__all__'

class BlogSrializers(serializers.ModelSerializer):
    comments= CommentSerializers(many=True, read_only=True)
    class Meta:
        model = blogModels
        fields = '__all__'