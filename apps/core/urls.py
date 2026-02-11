from django.urls import path
from . import views
import os
from django.conf import settings
from django.views.static import serve # For serving the Google verification file
from django.views.generic import TemplateView


app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('projects/<slug:slug>/plans/', views.project_plans, name='project_plans'),

    #privacy policy
    path('privacy-policy/', TemplateView.as_view(template_name='core/privacy-policy.html'), name='privacy_policy'),

    path('terms-of-use/', TemplateView.as_view(template_name='core/terms-of-use.html'), name='terms_of_use'),


    # Google verification - serve from static
    #an ID card that proves you own the domain. -> bot visit -> we get verified
    # Google verification - serve from static
    path(
        'googledebd6a5009a9aea1.html',  # Changed: bd not db
        serve,
        {
            'document_root': os.path.join(settings.BASE_DIR, 'apps/core/static'),
            'path': 'googledebd6a5009a9aea1.html',  # Changed: bd not db
        },
    ),
    #If someone visits /googlededb6a5009a9aea1.html, go to the static folder and return that verification HTML file.
]

