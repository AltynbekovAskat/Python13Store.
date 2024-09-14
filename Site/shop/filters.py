from .models import Task
from django_filters import FilterSet
class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'title': ['exact'],
            'created_date': ['gt', 'lt']
        }
