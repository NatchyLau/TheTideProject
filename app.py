from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Home page
@app.route('/')
def index():
    return render_template('index.html')

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

# Registration form handler
@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    interest = request.form.get('interest')
    
    # Here you would typically save to database
    # For now, just flash a success message
    flash(f'Thank you {name}! We will contact you soon at {email}.', 'success')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)