# forms.py
from django import forms
from apps.locations.models import Province, District
from .models import CustomerInquiry

COMMON_STYLE = 'block w-full px-4 h-12 text-lg text-ocean-900 bg-transparent border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-ocean-900 peer invalid:text-gray-400'

class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = [
            'first_name', 'last_name', 'phone', 'line_id',
            'province', 'district', 'address_detail',
            'budget', 'preferred_day', 'preferred_time', 'note'
        ]
        widgets = {
        # Text Input (ไม่ใช้ invalid color เพราะมี placeholder attribute อยู่แล้ว)
        'first_name': forms.TextInput(attrs={'class': COMMON_STYLE.replace('invalid:text-gray-400', ''), 'placeholder': ' '}),
        'last_name': forms.TextInput(attrs={'class': COMMON_STYLE.replace('invalid:text-gray-400', ''), 'placeholder': ' '}),
        'phone': forms.TextInput(attrs={'class': COMMON_STYLE.replace('invalid:text-gray-400', ''), 'placeholder': ' '}),
        'line_id': forms.TextInput(attrs={'class': COMMON_STYLE.replace('invalid:text-gray-400', ''), 'placeholder': ' '}),
        
        # Dropdown: ต้องใส่ required=True เพื่อให้ CSS invalid ทำงาน
        'province': forms.Select(attrs={
            'class': COMMON_STYLE,
            'hx-get': '/api/districts/',
            'hx-target': '#id_district',
            'hx-trigger': 'change',
            'required': True 
        }),
        'district': forms.Select(attrs={'class': COMMON_STYLE, 'id': 'id_district', 'required': True}),
        'budget': forms.Select(attrs={'class': COMMON_STYLE, 'required': True}),
        'preferred_day': forms.Select(attrs={'class': COMMON_STYLE, 'required': True}),
        'preferred_time': forms.Select(attrs={'class': COMMON_STYLE, 'required': True}),
        
        # Textarea
        'address_detail': forms.Textarea(attrs={'class': 'block w-full px-4 py-3 text-lg text-ocean-900 bg-transparent border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-ocean-900 peer', 'rows': 2, 'placeholder': ' '}),
        'note': forms.Textarea(attrs={'class': 'block w-full px-4 py-3 text-lg text-ocean-900 bg-transparent border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-ocean-900 peer', 'rows': 2, 'placeholder': ' '}),
    }