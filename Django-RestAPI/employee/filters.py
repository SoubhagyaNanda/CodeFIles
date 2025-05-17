import django_filters
from .models import Employees

class EmployeeFilter(django_filters.FilterSet):
    emp_desi= django_filters.CharFilter(field_name='emp_desi', lookup_expr='iexact')
    emp_name= django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='from emp_id')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='to emp_id')

    class Meta:
        model= Employees
        fields= ['emp_desi', 'emp_name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):
        try:
            value = int(value)  # convert to integer for comparison
        except ValueError:
            return queryset  # skip filtering if value is not numeric

        if name == 'id_min':
            return queryset.filter(emp_id__gte=str(value))
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=str(value))
        return queryset
