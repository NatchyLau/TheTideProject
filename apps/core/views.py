from django.http import Http404
from django.shortcuts import render
from apps.accounts.forms import CustomerInquiryForm

# Create your views here.

def index(request):
    form = CustomerInquiryForm()
    return render(request, 'core/index.html', {'form': form})


def project_plans(request, slug):
    allowed_slugs = {
        'the-tide-grand-nawong',
        'the-tide-grand-phutthaphum',
        'the-tide-privilege-therdphra-kiat',
    }

    if slug not in allowed_slugs:
        raise Http404("Project not found")

    return render(request, 'core/project_plans.html', {'slug': slug})

