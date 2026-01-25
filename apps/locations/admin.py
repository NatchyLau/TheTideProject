from django.contrib import admin
from .models import Province, District, SubDistrict


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name_th', 'name_en', 'geography_id']
    search_fields = ['name_th', 'name_en']
    list_filter = ['geography_id']


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name_th', 'province', 'name_en']
    search_fields = ['name_th', 'name_en', 'province__name_th']
    list_filter = ['province']
    autocomplete_fields = ['province']


@admin.register(SubDistrict)
class SubDistrictAdmin(admin.ModelAdmin):
    list_display = ['name_th', 'district', 'zip_code']
    search_fields = ['name_th', 'name_en', 'zip_code', 'district__name_th']
    list_filter = ['district__province']
    autocomplete_fields = ['district']
