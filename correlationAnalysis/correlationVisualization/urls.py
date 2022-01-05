from django.urls import path
from . import views

app_name="CorrelationVisualization"

urlpatterns = [
    path('', views.get, name='get',),
    path('corr/', views.post, name='post'),
    path('corr/legend', views.legend, name='legend')
]