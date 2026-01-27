from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('projects/<slug:slug>/plans/', views.project_plans, name='project_plans'),
]
