from django.contrib import admin
from .models import CustomerInquiry


@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'province', 'budget', 'preferred_day', 'preferred_time', 'is_contacted', 'created_at']
    search_fields = ['first_name', 'last_name', 'phone', 'line_id']
    list_filter = ['budget', 'preferred_day', 'preferred_time', 'is_contacted', 'province', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    autocomplete_fields = ['province', 'district']
    
    fieldsets = (
        ('ข้อมูลส่วนตัว', {
            'fields': ('first_name', 'last_name', 'phone', 'line_id')
        }),
        ('ที่อยู่', {
            'fields': ('province', 'district', 'address_detail')
        }),
        ('ความสนใจ', {
            'fields': ('budget', 'preferred_day', 'preferred_time', 'note')
        }),
        ('สถานะ', {
            'fields': ('is_contacted', 'created_at', 'updated_at')
        }),
    )
