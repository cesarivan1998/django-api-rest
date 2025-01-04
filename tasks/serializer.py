from rest_framework import serializers
from .models import Task


#convertir datos en formato python a json
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id','title','description','done')
        fields = '__all__'   