# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('soc', views.trigger_pipeline_view, name='soc_selection'),
    path('get_pipeline_status/', views.get_latest_pipeline_status_for_name, name='get_pipeline_status'),
   
]
