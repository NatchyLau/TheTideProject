from django import forms
from apps.locations.models import Province, District
from .models import CustomerInquiry


class CustomerInquiryForm(forms.ModelForm):
    class Meta:
        model = CustomerInquiry
        fields = [
            'first_name', 'last_name', 'phone', 'line_id',
            'province', 'district', 'address_detail',
            'budget', 'preferred_day', 'preferred_time', 'note'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'placeholder': 'กรอกชื่อ'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'placeholder': 'กรอกนามสกุล'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'placeholder': '08X-XXX-XXXX'
            }),
            'line_id': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'placeholder': 'Line ID (ถ้ามี)'
            }),
            'province': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'hx-get': '/api/districts/',
                'hx-target': '#id_district',
                'hx-trigger': 'change'
            }),
            'district': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
            }),
            'address_detail': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'placeholder': 'บ้านเลขที่ หมู่ ซอย ถนน (ถ้ามี)',
                'rows': 3
            }),
            'budget': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
            }),
            'preferred_day': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
            }),
            'preferred_time': forms.Select(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
            }),
            'note': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-900 focus:border-transparent transition',
                'placeholder': 'ข้อมูลเพิ่มเติม (ถ้ามี)',
                'rows': 3
            }),
        }
