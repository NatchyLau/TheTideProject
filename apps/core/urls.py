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

    # Google verification - serve from static
    #an ID card that proves you own the domain. -> bot visit -> we get verified
    path(
        'googlededb6a5009a9aea1.html',
        serve,
        {
            'document_root': os.path.join(settings.BASE_DIR, 'apps/core/static'),
            'path': 'googlededb6a5009a9aea1.html',
        },
    ),
    #If someone visits /googlededb6a5009a9aea1.html, go to the static folder and return that verification HTML file.
]

