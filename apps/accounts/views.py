import json
import requests

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from apps.locations.models import Province, District
from .models import CustomerInquiry
from .forms import CustomerInquiryForm

TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


def contact_form_view(request):
    """แสดงฟอร์มติดต่อ"""
    form = CustomerInquiryForm()
    provinces = Province.objects.all()
    return render(request, 'accounts/contact_form.html', {
        'form': form,
        'provinces': provinces
    })


@require_http_methods(["GET"])
def get_districts(request):
    """API สำหรับดึงอำเภอตามจังหวัดที่เลือก (HTMX)"""
    province_id = request.GET.get('province')
    
    # ถ้าไม่มี province_id ส่ง empty queryset
    districts = District.objects.none()
    
    if province_id:
        districts = District.objects.filter(province_id=province_id).order_by('name_th')
    
    # ใช้ render แทน HttpResponse + String concatenation
    return render(request, 'accounts/partials/district_options.html', {
        'districts': districts
    })


@require_http_methods(["POST"])
def submit_inquiry(request):
    """รับข้อมูลจากฟอร์ม (HTMX)"""
    # ---- Cloudflare Turnstile verification ----
    cf_token = request.POST.get("cf-turnstile-response", "")
    cf_payload = {
        "secret": settings.CLOUDFLARE_TURNSTILE_SECRET_KEY,
        "response": cf_token,
        "remoteip": request.META.get("HTTP_X_FORWARDED_FOR", request.META.get("REMOTE_ADDR", "")),
    }

    try:
        cf_result = requests.post(TURNSTILE_VERIFY_URL, data=cf_payload, timeout=5)
        cf_data = cf_result.json()
    except (requests.RequestException, ValueError):
        cf_data = {"success": False}

    if not cf_data.get("success"):
        return render(request, "accounts/partials/error_message.html", {
            "turnstile_error": True,
        })
    # ---- End Turnstile verification ----

    form = CustomerInquiryForm(request.POST)
    
    if form.is_valid():
        inquiry = form.save()
        
        # ใช้ Template แทน HTML String
        return render(request, 'accounts/partials/success_message.html')
    else:
        # ใช้ Template สำหรับ Error Message
        return render(request, 'accounts/partials/error_message.html', {
            'form': form
        })


# ==================== Dashboard Views ====================

@staff_member_required
def inquiry_dashboard(request):
    """Dashboard สำหรับ Sales/Admin ดูข้อมูลลูกค้า"""
    # Filters
    status_filter = request.GET.get('status', 'all')
    budget_filter = request.GET.get('budget', '')
    search = request.GET.get('search', '')
    
    inquiries = CustomerInquiry.objects.select_related('province', 'district')
    
    # Apply filters
    if status_filter == 'new':
        inquiries = inquiries.filter(is_contacted=False)
    elif status_filter == 'contacted':
        inquiries = inquiries.filter(is_contacted=True)
    
    if budget_filter:
        inquiries = inquiries.filter(budget=budget_filter)
    
    if search:
        inquiries = inquiries.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(phone__icontains=search) |
            Q(line_id__icontains=search)
        )
    
    # Stats
    total_count = CustomerInquiry.objects.count()
    new_count = CustomerInquiry.objects.filter(is_contacted=False).count()
    contacted_count = CustomerInquiry.objects.filter(is_contacted=True).count()
    
    context = {
        'inquiries': inquiries,
        'total_count': total_count,
        'new_count': new_count,
        'contacted_count': contacted_count,
        'status_filter': status_filter,
        'budget_filter': budget_filter,
        'search': search,
        'budget_choices': CustomerInquiry.BUDGET_CHOICES,
    }
    
    # If HTMX request, return only the table partial
    if request.headers.get('HX-Request'):
        return render(request, 'accounts/partials/inquiry_table.html', context)
    
    # Otherwise, return full page
    return render(request, 'accounts/dashboard.html', context)


@staff_member_required
@require_http_methods(["GET"])
def dashboard_stats(request):
    """ดึงสถิติสำหรับ Dashboard (HTMX)"""
    total_count = CustomerInquiry.objects.count()
    new_count = CustomerInquiry.objects.filter(is_contacted=False).count()
    contacted_count = CustomerInquiry.objects.filter(is_contacted=True).count()

    return render(request, 'accounts/partials/dashboard_stats.html', {
        'total_count': total_count,
        'new_count': new_count,
        'contacted_count': contacted_count,
    })


@staff_member_required
@require_http_methods(["POST"])
def update_inquiry_status(request, inquiry_id):
    """อัพเดทสถานะการติดต่อ (HTMX)"""
    inquiry = get_object_or_404(CustomerInquiry, id=inquiry_id)
    inquiry.is_contacted = not inquiry.is_contacted
    inquiry.save()

    response = render(request, 'accounts/partials/inquiry_row.html', {
        'inquiry': inquiry
    })
    response['HX-Trigger'] = json.dumps({"refresh-stats": {"target": "body"}})
    return response


@staff_member_required
def inquiry_detail(request, inquiry_id):
    """รายละเอียดลูกค้า (Modal/Page)"""
    inquiry = get_object_or_404(
        CustomerInquiry.objects.select_related('province', 'district'),
        id=inquiry_id
    )
    
    return render(request, 'accounts/inquiry_detail.html', {
        'inquiry': inquiry
    })
