from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from apps.locations.models import Province, District
from .models import CustomerInquiry
from .forms import CustomerInquiryForm


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
