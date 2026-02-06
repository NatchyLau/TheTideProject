import json
from django.core.management.base import BaseCommand
from apps.locations.models import Province, District, SubDistrict


class Command(BaseCommand):
    help = 'Import provinces, districts, and sub-districts from JSON file'

    def handle(self, *args, **options):

        if Province.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists. Skipping import.'))
            return
    
        json_file = 'province_with_district_and_sub_district.json'
        
        self.stdout.write('Starting import...')
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        province_count = 0
        district_count = 0
        subdistrict_count = 0
        
        for province_data in data:
            # สร้างจังหวัด
            province, created = Province.objects.get_or_create(
                id=province_data['id'],
                defaults={
                    'name_th': province_data['name_th'],
                    'name_en': province_data['name_en'],
                    'geography_id': province_data.get('geography_id'),
                }
            )
            if created:
                province_count += 1
                self.stdout.write(f'  Created province: {province.name_th}')
            
            # สร้างอำเภอ
            for district_data in province_data.get('districts', []):
                district, created = District.objects.get_or_create(
                    id=district_data['id'],
                    defaults={
                        'province': province,
                        'name_th': district_data['name_th'],
                        'name_en': district_data['name_en'],
                    }
                )
                if created:
                    district_count += 1
                
                # สร้างตำบล
                for subdistrict_data in district_data.get('sub_districts', []):
                    subdistrict, created = SubDistrict.objects.get_or_create(
                        id=subdistrict_data['id'],
                        defaults={
                            'district': district,
                            'name_th': subdistrict_data['name_th'],
                            'name_en': subdistrict_data['name_en'],
                            'zip_code': subdistrict_data['zip_code'],
                        }
                    )
                    if created:
                        subdistrict_count += 1
        
        self.stdout.write(self.style.SUCCESS(
            f'\nImport completed successfully!\n'
            f'Provinces: {province_count}\n'
            f'Districts: {district_count}\n'
            f'Sub-districts: {subdistrict_count}'
        ))
