# PriceScope Setup Guide

This guide will help you set up and run the PriceScope price comparison platform on your local machine.

## 📋 Prerequisites

Before starting, make sure you have:
- **Python 3.8 or higher** installed
- **MySQL Server** installed and running
- **Git** (optional, for version control)
- **Visual Studio Code** or any text editor

## 🚀 Step-by-Step Installation

### Step 1: Create MySQL Database

1. Open MySQL Command Line or MySQL Workbench
2. Run these commands:

```sql
CREATE DATABASE price_comparison;
USE price_comparison;
```

### Step 2: Navigate to Project Directory

```bash
cd c:\price-c-system
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your terminal line.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Mail
- And other required packages

### Step 5: Configure Environment  Variables

1. Create a `.env` file in the project root:

```bash
cp .env.example .env
```

2. Edit `.env` with your configuration:

```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://root:root@localhost/price_comparison
```

**Replace:**
- `root:root` with your MySQL username:password
- `SECRET_KEY` with a random string (at least 32 characters)

### Step 6: Initialize Database

The database tables will be created automatically when you first run the app. However, you can manually create them:

```bash
python
>>> from app import create_app, db
>>> app = create_app('development')
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### Step 7: Run the Application

```bash
python run.py
```

You should see output like:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

### Step 8: Access the Application

Open your browser and go to:
```
http://localhost:5000
```

## 🎯 First-Time Setup

### Create Admin Account

1. Navigate to `/auth/register`
2. Create an account with username `admin`
3. After login, you'll have access to the admin dashboard at `/admin/dashboard`

### Add Sample Products

1. Go to Admin Dashboard → Products
2. Click "Add Product" button
3. Fill in:
   - **Name**: Product name (e.g., "iPhone 15 Pro")
   - **Category**: Category (e.g., "Electronics")
   - **Description**: Product description
   - **Image URL**: (Optional) URL to product image
4. Click "Add Product"

### Add Price Data

1. Admin Dashboard → Prices
2. Add prices from different websites for your products

## 🔧 Configuration Details

### Database Connection

Update `DATABASE_URL` in `.env`:
```
DATABASE_URL=mysql+pymysql://username:password@localhost/price_comparison
```

### Email Configuration (Optional)

For email notifications:

```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=app-specific-password
```

### Getting Gmail App Password

1. Enable 2-Factor Authentication on your Google account
2. Go to [Security Settings](https://myaccount.google.com/security)
3. Find "App passwords" (near the bottom)
4. Create a new app password for "Mail" and "Windows Computer"
5. Copy the generated password and add to `.env`

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Access denied for user 'root'@'localhost'"

**Solution:**
Check MySQL credentials in `.env` file. Verify username and password are correct.

### Issue: "No module named 'app'"

**Solution:**
Make sure you're running commands from the project root directory (`c:\price-c-system`).

### Issue: Port 5000 already in use

**Solution:**
```bash
# Change port in run.py
# Or kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

## 📚 Project Structure Overview

```
price-c-system/
├── app/                    # Main application package
│   ├── models.py          # Database models
│   ├── routes/            # Route blueprints
│   └── __init__.py        # App factory
├── templates/             # HTML templates
│   ├── base.html          # Main template
│   ├── auth/              # Login/Register
│   └── user/              # User pages
├── config.py              # Configuration
├── run.py                 # Entry point
└── requirements.txt       # Dependencies
```

## 🎨 Customization

### Change Colors

Edit `templates/base.html`:
```html
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    primary: '#FF6B6B',      // Change this
                    secondary: '#4ECDC4',    // Change this
                    accent: '#FFE66D'        // Change this
                }
            }
        }
    }
</script>
```

### Add New Pages

1. Create route in `app/routes/main.py`:
```python
@main_bp.route('/new-page')
def new_page():
    return render_template('new-page.html')
```

2. Create template `templates/new-page.html`:
```html
{% extends "base.html" %}
{% block content %}
    <!-- Your content here -->
{% endblock %}
```

## 🚀 Deployment

### For Production

1. Change `FLASK_ENV=production` in `.env`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Set up a reverse proxy (Nginx, Apache)
4. Use HTTPS/SSL
5. Set strong `SECRET_KEY`
6. Update database URL for production server

### Deploy to Heroku

```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create Procfile
echo "web: gunicorn run:app" > Procfile

# Create requirements.txt
pip freeze > requirements.txt

# Deploy
git push heroku main
```

## 📞 Support & Help

- Check the main [README.md](README.md) for more information
- Review Flask documentation: https://flask.palletsprojects.com/
- Check SQLAlchemy docs: https://sqlalchemy.org/

## ✅ Next Steps

After setup:
1. ✅ Create an admin account
2. ✅ Add sample products
3. ✅ Add price data
4. ✅ Customize colors and branding
5. ✅ Set up email notifications
6. ✅ Test all features
7. ✅ Deploy to production

---

**Happy Shopping! 🛍️**

For issues or questions, feel free to reach out to support@pricescope.com
