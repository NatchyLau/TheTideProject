from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Public
    path('contact/', views.contact_form_view, name='contact_form'),
    path('api/districts/', views.get_districts, name='get_districts'),
    path('api/submit-inquiry/', views.submit_inquiry, name='submit_inquiry'),
    
    # Staff/Admin Dashboard
    path('dashboard/', views.inquiry_dashboard, name='inquiry_dashboard'),
    path('dashboard/stats/', views.dashboard_stats, name='dashboard_stats'),
    path('dashboard/<int:inquiry_id>/', views.inquiry_detail, name='inquiry_detail'),
    path('api/update-status/<int:inquiry_id>/', views.update_inquiry_status, name='update_inquiry_status'),
]
