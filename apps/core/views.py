from django.http import Http404
from django.shortcuts import render
from apps.accounts.forms import CustomerInquiryForm

# Create your views here.

def index(request):
    form = CustomerInquiryForm()
    return render(request, 'core/index.html', {'form': form})


def project_plans(request, slug):
    allowed_slugs = {
        'the-tide-grand-nawong',
        'the-tide-grand-phutthaphum',
        'the-tide-privilege-therdphra-kiat',
    }

    if slug not in allowed_slugs:
        raise Http404("Project not found")

    return render(request, 'core/project_plans.html', {'slug': slug})


# Floor Plan Data
FLOOR_PLAN_DATA = {
    'the-tide-grand-nawong': {
        'single-house': {
            'badge': 'Single House',
            'title': 'บ้านเดี่ยว 2 ชั้น',
            'area': '202 ตร.ม.',
            'price': '4.29',
            'beds': '4',
            'baths': '3',
            'floors': '2',
            'parking': '2',
            'images': [
                'core/images/nawong_type1.jpg',
                'core/images/nawong_type1_2.jpg',
                'core/images/nawong_type1_3.jpg',
            ],
            'highlights': [
                'ดีไซน์โมเดิร์นร่วมสมัย',
                'พื้นที่กว้างขวาง เหมาะสำหรับครอบครัว',
                'ห้องนอนใหญ่ทุกห้อง',
                'ครัวไทยและครัวฝรั่งแยกส่วน',
                'ที่จอดรถ 2 คัน พร้อมประตูอัตโนมัติ',
            ],
            'description': 'บ้านเดี่ยว 2 ชั้น สไตล์โมเดิร์น พร้อมพื้นที่ใช้สอยกว้างขวาง 202 ตร.ม. ออกแบบมาเพื่อตอบโจทย์ทุกไลฟ์สไตล์ของครอบครัว',
        },
        'twin-house': {
            'badge': 'Twin House',
            'title': 'บ้านแฝด 2 ชั้น',
            'area': '141 ตร.ม.',
            'price': '2.89',
            'beds': '3',
            'baths': '3',
            'floors': '2',
            'parking': '2',
            'images': [
                'core/images/nawong_type2.jpg',
                'core/images/nawong_type2_2.jpg',
                'core/images/nawong_type2_3.jpg',
            ],
            'highlights': [
                'ราคาคุ้มค่า เริ่มต้นเพียง 2.89 ล้าน',
                'ดีไซน์ทันสมัย ใช้งานได้จริง',
                'ห้องนอน 3 ห้อง ห้องน้ำ 3 ห้อง',
                'พื้นที่ส่วนกลางสไตล์รีสอร์ท',
                'ทำเลดี ใกล้สิ่งอำนวยความสะดวก',
            ],
            'description': 'บ้านแฝด 2 ชั้น ราคาคุ้มค่า พื้นที่ใช้สอย 141 ตร.ม. ฟังก์ชันครบครัน เหมาะสำหรับครอบครัวเริ่มต้น',
        },
        'twin-independent': {
            'badge': 'Twin Independent',
            'title': 'บ้านแฝดอิสระ 2 ชั้น',
            'area': '167 ตร.ม.',
            'price': '3.59',
            'beds': '4',
            'baths': '3',
            'floors': '2',
            'parking': '2',
            'images': [
                'core/images/nawong_type3.jpg',
                'core/images/nawong_type3_2.jpg',
                'core/images/nawong_type3_3.jpg',
            ],
            'highlights': [
                'ความเป็นส่วนตัวเหมือนบ้านเดี่ยว',
                'พื้นที่ใช้สอยกว้างขวาง 167 ตร.ม.',
                '4 ห้องนอน รองรับครอบครัวใหญ่',
                'สวนส่วนตัวหน้าบ้าน',
                'ที่จอดรถ 2 คัน',
            ],
            'description': 'บ้านแฝดอิสระ ความเป็นส่วนตัวเหมือนบ้านเดี่ยว พื้นที่ใช้สอย 167 ตร.ม. ตอบโจทย์ครอบครัวใหญ่',
        },
    },
    'the-tide-privilege-therdphra-kiat': {
        'single-house': {
            'badge': 'Single House',
            'title': 'บ้านเดี่ยว 2 ชั้น',
            'area': '234 ตร.ม.',
            'price': '5.9',
            'beds': '4',
            'baths': '3',
            'floors': '2',
            'parking': '2',
            'images': [
                'core/images/terdprakiat_type1.jpg',
                'core/images/terdprakiat_type1_2.jpg',
                'core/images/terdprakiat_type1_3.jpg',
            ],
            'highlights': [
                'บ้านหรู ระดับพรีเมียม',
                'พื้นที่ใช้สอยกว้างขวาง 234 ตร.ม.',
                'ทำเลศักยภาพ ถนนเทิดพระเกียรติ',
                'ใกล้ห้างสรรพสินค้าและโรงเรียน',
                'สิ่งอำนวยความสะดวกครบครัน',
            ],
            'description': 'บ้านเดี่ยวระดับพรีเมียม พื้นที่ใช้สอย 234 ตร.ม. ทำเลศักยภาพบนถนนเทิดพระเกียรติ',
        },
        'twin-independent': {
            'badge': 'Twin Independent',
            'title': 'บ้านแฝดอิสระ 2 ชั้น',
            'area': '192 ตร.ม.',
            'price': '4.7',
            'beds': '4',
            'baths': '3',
            'floors': '2',
            'parking': '2',
            'images': [
                'core/images/terdprakiat_type2.jpg',
                'core/images/terdprakiat_type2_2.jpg',
                'core/images/terdprakiat_type2_3.jpg',
            ],
            'highlights': [
                'ความเป็นส่วนตัวสูงสุด',
                'ฟังก์ชันครบ 4 ห้องนอน 3 ห้องน้ำ',
                'ดีไซน์ร่วมสมัย สไตล์โมเดิร์น',
                'พื้นที่สีเขียวรอบโครงการ',
                'ระบบรักษาความปลอดภัย 24 ชม.',
            ],
            'description': 'บ้านแฝดอิสระสไตล์โมเดิร์น พื้นที่ใช้สอย 192 ตร.ม. ความเป็นส่วนตัวสูงสุด',
        },
    },
}

PROJECT_NAMES = {
    'the-tide-grand-nawong': 'The Tide Grand Nawong',
    'the-tide-grand-phutthaphum': 'The Tide Grand Phutthaphum',
    'the-tide-privilege-therdphra-kiat': 'The Tide Privilege',
}


def floor_plan_detail(request, project_slug, plan_slug):
    # Check if project exists
    if project_slug not in FLOOR_PLAN_DATA:
        raise Http404("Project not found")
    
    project_plans = FLOOR_PLAN_DATA[project_slug]
    
    # Check if plan exists
    if plan_slug not in project_plans:
        raise Http404("Floor plan not found")
    
    plan_data = project_plans[plan_slug]
    project_name = PROJECT_NAMES.get(project_slug, 'The Tide')
    
    context = {
        'project_slug': project_slug,
        'plan_slug': plan_slug,
        'project_name': project_name,
        'plan': plan_data,
    }
    
    return render(request, 'core/floor_plan_detail.html', context)

