from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from functools import wraps
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# =====================================================
# ADMIN CREDENTIALS (CHANGE THESE!)
# =====================================================
ADMIN_USERNAME = 'tt123'
ADMIN_PASSWORD = 'tt123'

# File to store registrations
REGISTRATIONS_FILE = 'registrations.json'

# =====================================================
# HELPER FUNCTIONS
# =====================================================
def load_registrations():
    """Load registrations from JSON file"""
    if os.path.exists(REGISTRATIONS_FILE):
        with open(REGISTRATIONS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_registrations(registrations):
    """Save registrations to JSON file"""
    with open(REGISTRATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(registrations, f, ensure_ascii=False, indent=2)

def login_required(f):
    """Decorator to protect admin routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('กรุณาเข้าสู่ระบบเพื่อเข้าถึงหน้านี้', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# =====================================================
# PUBLIC USER ROUTES
# =====================================================

@app.route('/')
def index():
    """Main homepage for general users"""
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration form"""
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    interest = request.form.get('interest')
    
    # Load existing registrations
    registrations = load_registrations()
    
    # Create new registration
    new_registration = {
        'name': name,
        'email': email,
        'phone': phone,
        'interest': interest,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Add to list and save
    registrations.append(new_registration)
    save_registrations(registrations)
    
    flash(f'ขอบคุณคุณ {name}! เราจะติดต่อกลับเร็วๆ นี้', 'success')
    return redirect(url_for('index'))

# About section routes
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

# Projects routes
@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/project-nawong')
def project_nawong():
    return render_template('project-nawong.html')

@app.route('/project-buddhaphumi')
def project_buddhaphumi():
    return render_template('project-buddhaphumi.html')

# Services routes
@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/buy-sell')
def buy_sell():
    return render_template('buy-sell.html')

@app.route('/rental')
def rental():
    return render_template('rental.html')

@app.route('/investment')
def investment():
    return render_template('investment.html')

@app.route('/concierge')
def concierge():
    return render_template('concierge.html')

@app.route('/consulting')
def consulting():
    return render_template('consulting.html')

# Investor Relations routes
@app.route('/investor-relations')
def investor_relations():
    return render_template('investor-relations.html')

@app.route('/company-info')
def company_info():
    return render_template('company-info.html')

@app.route('/financial-reports')
def financial_reports():
    return render_template('financial-reports.html')

@app.route('/investor-news')
def investor_news():
    return render_template('investor-news.html')

@app.route('/investor-events')
def investor_events():
    return render_template('investor-events.html')

@app.route('/investor-contact')
def investor_contact():
    return render_template('investor-contact.html')

# Sustainability routes
@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')

@app.route('/sustainability-policy')
def sustainability_policy():
    return render_template('sustainability-policy.html')

@app.route('/environmental')
def environmental():
    return render_template('environmental.html')

@app.route('/csr')
def csr():
    return render_template('csr.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/sustainability-report')
def sustainability_report():
    return render_template('sustainability-report.html')

# =====================================================
# ADMIN ROUTES (COMPLETELY SEPARATED)
# =====================================================

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page - entry point for admin system"""
    # If already logged in, redirect to admin dashboard
    if 'admin_logged_in' in session:
        return redirect(url_for('admin'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            flash('เข้าสู่ระบบสำเร็จ', 'success')
            return redirect(url_for('admin'))
        else:
            flash('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง', 'error')
    
    return render_template('admin-login.html')

@app.route('/admin')
@login_required
def admin():
    """Admin dashboard - protected route"""
    registrations = load_registrations()
    return render_template('admin.html', registrations=registrations)

@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    flash('ออกจากระบบเรียบร้อยแล้ว', 'success')
    return redirect(url_for('admin_login'))

@app.route('/admin/delete/<int:index>', methods=['POST'])
@login_required
def delete_registration(index):
    """Delete single registration - admin only"""
    registrations = load_registrations()
    
    if 0 <= index < len(registrations):
        deleted = registrations.pop(index)
        save_registrations(registrations)
        flash(f'ลบข้อมูลของ {deleted["name"]} เรียบร้อยแล้ว', 'success')
    else:
        flash('ไม่พบข้อมูลที่ต้องการลบ', 'error')
    
    return redirect(url_for('admin'))

@app.route('/admin/clear', methods=['POST'])
@login_required
def clear_registrations():
    """Clear all registrations - admin only"""
    save_registrations([])
    flash('ลบข้อมูลทั้งหมดเรียบร้อยแล้ว', 'success')
    return redirect(url_for('admin'))

# =====================================================
# RUN APPLICATION
# =====================================================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)