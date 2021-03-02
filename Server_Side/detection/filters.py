import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

# Filtering
class DetectionFilter(django_filters.FilterSet):

	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')

	location = CharFilter(field_name='location', lookup_expr='icontains')
	alert_receiver = CharFilter(field_name='alert_receiver', lookup_expr='icontains')

	class Meta:
		model = UploadAlert
		fields = '__all__'
		exclude = ['customer', 'user_ID', 'image', 'uuid']