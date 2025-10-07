from django.urls import path

from apps.directions.api import DirectionCreateAPIView, DirectionListAPIView

app_name = 'directions'


urlpatterns = [
    path('create/', DirectionCreateAPIView.as_view(), name='direction_create'),
    path('', DirectionListAPIView.as_view(), name='direction_list'),
]