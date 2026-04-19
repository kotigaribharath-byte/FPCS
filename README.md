# PriceScope - Professional Price Comparison Platform

A modern, feature-rich price comparison web application built with Flask. Compare prices across multiple e-commerce platforms and save money with smart alerts and recommendations.

## 🎨 Design Highlights

- **Colorful & Vibrant UI** with Tailwind CSS
- **Responsive Design** - works seamlessly on mobile, tablet, and desktop
- **Modern Gradient Backgrounds** and smooth animations
- **Professional Navigation** with intuitive layout
- **Beautiful Card-based Interface** for products

## ✨ Key Features

### 1. **Multi-Store Price Comparison**
   - Compare prices from Amazon, Flipkart, Croma, and more
   - Real-time price tracking
   - View product links and in-stock status
   - Sort by price, rating, and relevance

### 2. **User Accounts & Authentication**
   - User registration and login
   - Secure password hashing
   - Session management
   - User profiles with customization options

### 3. **Favorites Management**
   - Add products to favorites
   - Access saved products anytime
   - Quick access from dashboard
   - Wishlist functionality

### 4. **Price Alerts**
   - Set target prices for products
   - Automatic notifications when prices drop
   - Email alerts (configurable)
   - Manage multiple alerts easily

### 5. **Community Reviews & Ratings**
   - User-submitted product reviews
   - 5-star rating system
   - Review titles and detailed content
   - Helpful feedback tracking

### 6. **Search History**
   - Automatic search tracking
   - View past searches
   - Re-search previous queries
   - Personalized recommendations based on history

### 7. **Admin Dashboard**
   - Manage products and categories
   - Add, edit, delete products
   - Monitor price data
   - View user activity and alerts
   - User management

## 📁 Project Structure

```
price-c-system/
├── app/
│   ├── __init__.py                 # Flask app factory
│   ├── models.py                   # Database models (User, Product, Review, etc.)
│   ├── routes/
│   │   ├── main.py                 # Home, search, about pages
│   │   ├── auth.py                 # Login, register, logout
│   │   ├── products.py             # Product details, favorites, reviews
│   │   ├── user.py                 # User profile, alerts, preferences
│   │   └── admin.py                # Admin dashboard and management
│   └── utils/
│       └── helpers.py              # Helper functions
├── templates/
│   ├── base.html                   # Base template with navigation
│   ├── index.html                  # Home page
│   ├── search.html                 # Search results
│   ├── product_detail.html         # Product page with prices
│   ├── favorites.html              # Favorites page
│   ├── auth/
│   │   ├── login.html              # Login page
│   │   └── register.html           # Registration page
│   ├── user/
│   │   ├── profile.html            # User profile
│   │   ├── price_alerts.html       # Price alerts management
│   │   └── search_history.html     # Search history
│   └── admin/
│       ├── dashboard.html          # Admin dashboard
│       ├── products.html           # Product management
│       └── price_alerts.html       # Alert management
├── static/
│   └── css/
│       └── style.css               # Custom CSS (if needed)
├── sql/
│   └── price_comparison.sql        # Database schema
├── config.py                       # Configuration settings
├── run.py                          # Entry point
├── requirements.txt                # Dependencies
└── README.md                       # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd c:\price-c-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   - Create a MySQL database:
     ```sql
     CREATE DATABASE price_comparison;
     ```
   - Update `config.py` with your MySQL credentials

5. **Set environment variables** (create `.env` file)
   ```
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=mysql+pymysql://user:password@localhost/price_comparison
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Open in browser**
   ```
   http://localhost:5000
   ```

## 🔧 Configuration

### `config.py`
- **Development**: Debug mode enabled, secure cookies disabled
- **Production**: Debug disabled, secure cookies enabled
- **Testing**: In-memory SQLite database for testing

### Email Setup (Optional)
For email notifications to work:
1. Use Gmail or another SMTP service
2. Generate an app-specific password
3. Add to `.env` file:
   ```
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-specific-password
   ```

## 📊 Database Models

### User
- Username, email, password (hashed)
- First name, last name, bio
- Relationships: favorites, reviews, price alerts, search history

### Product
- Name, category, description, image URL
- Average rating, review count
- Relationships: prices, reviews, favorites

### ProductPrice
- Price, website, product link, in-stock status
- Price history tracking

### Favorite
- User-product relationship
- Timestamp tracking

### Review
- User rating (1-5 stars)
- Title and content
- Helpful count

### PriceAlert
- User, product, target price
- Active status, notification status

### SearchHistory
- User, search query, results count
- Timestamp

## 🎯 Key Routes

### Public Routes
- `/` - Home page
- `/search?q=query` - Search results
- `/products/<id>` - Product detail page
- `/auth/login` - Login page
- `/auth/register` - Registration page
- `/about` - About us
- `/contact` - Contact us

### Authenticated Routes
- `/user/profile` - User profile
- `/user/profile/edit` - Edit profile
- `/user/price-alerts` - Manage price alerts
- `/products/favorites` - View favorites
- `/user/search-history` - View search history
- `/user/recommendations` - Get recommendations

### Admin Routes
- `/admin/dashboard` - Admin dashboard
- `/admin/products` - Manage products
- `/admin/users` - Manage users
- `/admin/reviews` - Manage reviews
- `/admin/price-alerts` - Monitor alerts

## 🎨 Technology Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login, Flask-Mail
- **Frontend**: HTML5, Tailwind CSS, Font Awesome Icons
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Werkzeug password hashing
- **Email**: Flask-Mail with SMTP

## 🔐 Security Features

- Password hashing with Werkzeug
- Session-based authentication with Flask-Login
- CSRF protection (built-in with Flask)
- Secure cookie settings
- SQL injection prevention with SQLAlchemy ORM
- Input validation and sanitization

## 📱 Responsive Design

The application is fully responsive and works great on:
- Desktop (1920px and up)
- Tablet (768px to 1024px)
- Mobile (320px to 767px)

## 🌈 Color Scheme

- **Primary**: #FF6B6B (Vibrant Red)
- **Secondary**: #4ECDC4 (Turquoise)
- **Accent**: #FFE66D (Golden Yellow)
- **Dark**: #2D3436 (Dark Gray)
- **Light**: #F5F6FA (Light Gray)

## 🚦 Future Enhancements

- [ ] Advanced analytics and price trend charts
- [ ] Mobile app (React Native)
- [ ] Browser extension for easy price comparison
- [ ] Integration with more e-commerce sites
- [ ] Machine learning-based price predictions
- [ ] Bulk price tracking
- [ ] Custom price drop percentages
- [ ] Social shopping features
- [ ] Cashback and coupon integration
- [ ] Product availability notifications

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Support

For support, email support@pricescope.com or open an issue in the repository.

## 👥 Team

Built with ❤️ by the PriceScope Team

---

**Last Updated**: April 2024  
**Version**: 1.0.0
