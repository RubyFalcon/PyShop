# PyShop

A Django-based e-commerce web application demonstrating product catalog management, admin customization, and a responsive Bootstrap storefront.

This project is being developed alongside the Programming with Mosh Django course while being extended beyond the tutorial to build a production-style portfolio project.

---

## 🌐 Overview

**PyShop** is a lightweight e-commerce platform that currently allows users to browse products and enables administrators to manage inventory and promotional offers via the Django Admin.

The project is evolving toward a full-stack commerce application with dynamic cart and checkout functionality.

---

## 🚀 Current Features

### 🛍️ Storefront
- Browse products at `/products/`
- Clean Bootstrap-based responsive UI
- Homepage with e-commerce layout
- Product listing powered by Django templates

### 🔐 Admin Management
- Django Admin enabled
- Custom admin configuration for:
  - Products
  - Offers
- Quick inventory visibility via `list_display`
- Simple product and discount management

### ⚙️ Backend
- Django MVC architecture
- Modular app structure (`products`)
- SQLite for local development
- Virtual environment configured

---

## 🛠️ Technologies Used

**Backend**
- Python  
- Django 6.0  

**Frontend**
- HTML5  
- Bootstrap 5  
- Django Templates  

**Database**
- SQLite (development)  
- PostgreSQL planned for production  

**Dev Tools**
- VS Code  
- Git & GitHub  
- Python venv  

---

## 📁 Project Structure



pyshop/
├── pyshop/ # Project settings
├── products/ # Products app
├── manage.py
└── templates/


---

## 🔧 Admin Customization

The Django admin has been extended for better product and offer visibility:

- Product list shows name, price, and stock
- Offer list shows code and discount
- Enables quick inventory management for administrators

---

## 🎯 Roadmap / Planned Improvements

### 🛒 E-commerce Core
- Add to cart functionality
- Session-based shopping cart
- Checkout flow
- Order model and history
- Stripe payment integration

### 🔍 Product Experience
- Search and filtering
- Pagination
- Product detail enhancements
- Image handling improvements

### 🎨 Frontend
- Improved mobile responsiveness
- UI polish and accessibility
- Loading states and feedback
- Optional dark mode

### ⚛️ Future Architecture
- Django REST API
- React frontend refactor
- Full-stack deployment (Render + Postgres)

---

### 🚀 Getting Started

## 1. Clone the repo

- git clone <your-repo-url>
- cd pyshop

## 2. Create and activate virtual environment
- python3 -m venv .venv
- source .venv/bin/activate
### 3. Install dependencies
- pip install -r requirements.txt
### 4. Run migrations
- python manage.py migrate
### 5. Start development server
- python manage.py runserver

### Visit:

- Store: http://127.0.0.1:8000/products/

- Admin: http://127.0.0.1:8000/admin/

### 📌 Status

### 🚧 Actively in development
- This project is being incrementally enhanced from tutorial foundation → production-ready portfolio application.

### 💡 Learning Goals

- Strengthen Django fundamentals
- Build real-world e-commerce patterns
- Prepare for React + Django full-stack architecture
- Practice deployment to cloud platforms