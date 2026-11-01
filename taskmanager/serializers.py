from rest_framework import serializers
from .models import Subject, Task

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"