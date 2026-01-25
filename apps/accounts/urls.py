from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('contact/', views.contact_form_view, name='contact_form'),
    path('api/districts/', views.get_districts, name='get_districts'),
    path('api/submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),
]
