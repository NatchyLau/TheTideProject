# forms.py
import re

from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from apps.locations.models import Province, District
from .models import CustomerInquiry

COMMON_STYLE = 'block w-full px-4 h-12 text-lg text-ocean-900 bg-transparent border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-ocean-900 peer invalid:text-gray-400'

class CustomerInquiryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Replace Django's default "---------" empty option with friendly labels
        if 'province' in self.fields:
            self.fields['province'].empty_label = 'กรุณาเลือกจังหวัด...'

        if 'district' in self.fields:
            self.fields['district'].empty_label = 'กรุณาเลือกอำเภอ/เขต...'
            self.fields['district'].queryset = District.objects.none()

            # When submitting/rehydrating the form, validate district against the selected province
            province_id = None
            if self.data:
                province_id = self.data.get('province')
            elif getattr(self.instance, 'province_id', None):
                province_id = self.instance.province_id

            if province_id:
                try:
                    self.fields['district'].queryset = District.objects.filter(
                        province_id=int(province_id)
                    ).order_by('name_th')
                except (TypeError, ValueError):
                    # Keep empty queryset if province_id is invalid
                    pass

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '')
        normalized = re.sub(r'\D', '', phone)

        if len(normalized) != 10 or not normalized.startswith('0'):
            raise ValidationError('กรุณากรอกเบอร์โทรศัพทให้ถูกต้อง')

        return normalized

    def clean(self):
        cleaned_data = super().clean()
        province = cleaned_data.get('province')
        district = cleaned_data.get('district')

        if province and district and district.province_id != province.id:
            self.add_error('district', 'กรุณาเลือกอำเภอ/เขตให้ตรงกับจังหวัด')

        return cleaned_data

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
            'hx-get': reverse_lazy('accounts:get_districts'),
            'hx-target': '#id_district',
            # Avoid calling the endpoint when province is empty
            'hx-trigger': "change[this.value!='']",
            'required': True 
        }),
        'district': forms.Select(attrs={'class': f"{COMMON_STYLE} disabled:text-gray-400", 'id': 'id_district', 'required': True, 'disabled': True}),
        'budget': forms.Select(attrs={'class': COMMON_STYLE, 'required': True}),
        'preferred_day': forms.Select(attrs={'class': COMMON_STYLE, 'required': True}),
        'preferred_time': forms.Select(attrs={'class': COMMON_STYLE, 'required': True}),
        
        # Textarea
        'address_detail': forms.Textarea(attrs={'class': 'block w-full px-4 py-3 text-lg text-ocean-900 bg-transparent border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-ocean-900 peer', 'rows': 2, 'placeholder': ' '}),
        'note': forms.Textarea(attrs={'class': 'block w-full px-4 py-3 text-lg text-ocean-900 bg-transparent border-b border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-ocean-900 peer', 'rows': 2, 'placeholder': ' '}),
    }