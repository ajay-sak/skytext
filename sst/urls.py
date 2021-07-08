from django.urls import path
from . import views

urlpatterns = [
   path('test_details', views.test_details, name="test_details"),
]
