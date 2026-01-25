from django.db import models
from apps.locations.models import Province, District


class CustomerInquiry(models.Model):
    """ข้อมูลลูกค้าที่สนใจ"""
    
    BUDGET_CHOICES = [
        ('2.01-2.50', '2.01-2.50 ล้านบาท'),
        ('2.51-3.00', '2.51-3.00 ล้านบาท'),
        ('3.01-3.50', '3.01-3.50 ล้านบาท'),
        ('3.51-4.00', '3.51-4.00 ล้านบาท'),
        ('4.01-4.50', '4.01-4.50 ล้านบาท'),
        ('4.51-5.00', '4.51-5.00 ล้านบาท'),
        ('5.00+', 'มากกว่า 5.00 ล้านบาท'),
    ]
    
    DAY_CHOICES = [
        ('weekday', 'วันทำการ (จันทร์-ศุกร์)'),
        ('weekend', 'วันหยุด (เสาร์-อาทิตย์)'),
    ]
    
    TIME_CHOICES = [
        ('09:00-12:00', 'ช่วงเช้า (09.00-12.00)'),
        ('12:00-13:00', 'ช่วงเที่ยง (12.00-13.00)'),
        ('13:00-15:00', 'ช่วงบ่าย (13.00-15.00)'),
        ('15:00-18:00', 'ช่วงเย็น (15.00-18.00)'),
        ('18:00-21:00', 'ช่วงค่ำ (18.00-21.00)'),
    ]
    
    # ข้อมูลส่วนตัว
    first_name = models.CharField(max_length=100, verbose_name="ชื่อ")
    last_name = models.CharField(max_length=100, verbose_name="นามสกุล")
    phone = models.CharField(max_length=20, verbose_name="เบอร์โทรศัพท์")
    line_id = models.CharField(max_length=100, blank=True, verbose_name="Line ID")
    
    # ที่อยู่
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, verbose_name="จังหวัด")
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, verbose_name="เขต/อำเภอ")
    address_detail = models.TextField(blank=True, verbose_name="ที่อยู่เพิ่มเติม")
    
    # ความสนใจ
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES, verbose_name="งบประมาณ")
    preferred_day = models.CharField(max_length=10, choices=DAY_CHOICES, verbose_name="วันที่สะดวก")
    preferred_time = models.CharField(max_length=20, choices=TIME_CHOICES, verbose_name="เวลาที่สะดวก")
    
    # ข้อมูลเพิ่มเติม
    note = models.TextField(blank=True, verbose_name="หมายเหตุ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")
    is_contacted = models.BooleanField(default=False, verbose_name="ติดต่อแล้ว")
    
    class Meta:
        verbose_name = "ข้อมูลลูกค้า"
        verbose_name_plural = "ข้อมูลลูกค้า"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone}"
