# Real Estate Homepage with Registration

A simple Python Flask application for a real estate company with a homepage and registration form.

## Features

- Attractive hero section with background image
- Key features display (Premium Locations, Best Prices, Expert Guidance)
- Registration form with:
  - Full Name (required)
  - Email Address (required)
  - Phone Number (optional)
  - Interest type dropdown (Buying/Renting/Selling/Investment)
- Flash messages for user feedback
- Responsive design

## Installation

1. Install Flask:
```bash
pip install flask
```

## Running the Application

1. Navigate to the directory containing the files
2. Run the application:
```bash
python real_estate_app.py
```

3. Open your web browser and go to:
```
http://localhost:5000
```

## File Structure

```
.
├── real_estate_app.py       # Main Flask application
├── templates/
│   └── index.html          # Homepage template
└── README.md               # This file
```

## Customization

- Change the company name in `index.html`
- Modify the secret key in `real_estate_app.py` for production
- Add a database (SQLite, PostgreSQL, etc.) instead of in-memory storage
- Customize colors and styling in the CSS section

## Notes

- This is a simple demonstration app
- In production, use a proper database to store registrations
- Add proper form validation and security measures
- Consider adding email notifications for new registrations