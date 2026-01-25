from django.db import models


class Province(models.Model):
    """จังหวัด"""
    name_th = models.CharField(max_length=150, verbose_name="ชื่อจังหวัด (ไทย)")
    name_en = models.CharField(max_length=150, verbose_name="ชื่อจังหวัด (อังกฤษ)")
    geography_id = models.IntegerField(null=True, blank=True, verbose_name="รหัสภูมิภาค")
    
    class Meta:
        verbose_name = "จังหวัด"
        verbose_name_plural = "จังหวัด"
        ordering = ['name_th']
    
    def __str__(self):
        return self.name_th


class District(models.Model):
    """อำเภอ"""
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts', verbose_name="จังหวัด")
    name_th = models.CharField(max_length=150, verbose_name="ชื่อเขต/อำเภอ (ไทย)")
    name_en = models.CharField(max_length=150, verbose_name="ชื่อเขต/อำเภอ (อังกฤษ)")
    
    class Meta:
        verbose_name = "เขต/อำเภอ"
        verbose_name_plural = "เขต/อำเภอ"
        ordering = ['name_th']
    
    def __str__(self):
        return f"{self.name_th} ({self.province.name_th})"


class SubDistrict(models.Model):
    """ตำบล"""
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='sub_districts', verbose_name="เขต/อำเภอ")
    name_th = models.CharField(max_length=150, verbose_name="ชื่อแขวง/ตำบล (ไทย)")
    name_en = models.CharField(max_length=150, verbose_name="ชื่อแขวง/ตำบล (อังกฤษ)")
    zip_code = models.CharField(max_length=5, verbose_name="รหัสไปรษณีย์")
    
    class Meta:
        verbose_name = "แขวง/ตำบล"
        verbose_name_plural = "แขวง/ตำบล"
        ordering = ['name_th']
    
    def __str__(self):
        return f"{self.name_th} ({self.district.name_th})"
