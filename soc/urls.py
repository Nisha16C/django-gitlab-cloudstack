# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('soc', views.trigger_pipeline_view, name='soc_selection'),
]
