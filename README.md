# Expense Tracker Django Project - README

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [API Endpoints](#api-endpoints)  
- [User Authentication](#user-authentication)  
- [Budget and Analytics](#budget-and-analytics)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Project Overview

Expense Tracker is a Django-based web application designed to help users monitor and manage their expenses, set budgets, organize expenditures by categories, and analyze spending trends. The project emphasizes user authentication, intuitive interfaces, and useful financial insights through analytics.

---

## Features

- User Registration, Login, and Logout functionality using Django’s built-in auth system.
- Add, view, edit, and delete expenses with categorizations.
- Manage budget settings and view real-time budget summaries.
- Filter expenses by day, week, or month.
- Display latest expenses and quick budget summaries on the home page.
- Analytics pages with interactive charts for monthly and category-based spending trends.
- User-specific categories and budgets.
- Responsive, user-friendly UI styled with Tailwind CSS.
- Secure access with login-required views.

---

## Tech Stack

- Backend: Django 5.2.5 (Python 3.13)  
- Database: SQLite (default, easily replaceable)  
- Frontend: Django templates, Tailwind CSS, FontAwesome icons  
- Analytics: Chart.js via templates (JavaScript)  
- Authentication: Django’s built-in authentication  

---

## Installation

1. **Clone the repository**
    ```
    git clone (https://github.com/abdelillah01/Budget-expenses.tracker)
    cd expense-tracker
    ```

2. **Create and activate a virtual environment**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Apply database migrations**
    ```
    python manage.py migrate
    ```

5. **Run the development server**
    ```
    python manage.py runserver
    ```

6. **Access the app**
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Usage

- **Register/Login:** Create a user account or log in to access personalized features.  
- **Dashboard:** View your current budget, spending summary, and recent expenses.  
- **Add Expenses:** Categorize your spending with date, amount, and description.  
- **Manage Categories:** Edit or add categories to organize expenses better.  
- **Set Budget:** Define a monthly budget and track remaining funds in real-time.  
- **Filter Expenses:** View expenses filtered by day, week, or month on the home page.  
- **Analytics:** Use charts to visualize spending trends by month and category.

---

## User Authentication

- Built on Django's authentication framework.  
- Uses views for login (`/login/`), logout (`/logout/`), and registration (`/register/`).  
- Passwords are securely hashed.  
- Login required for all expense, budget, and category management views.

---

## Budget and Analytics

- **Budget model:** Each user has a monthly budget.  
- **Real-time Calculation:** The app subtracts current month’s expenses from the budget and displays remaining funds.  
- **Analytics:** Charts display monthly spending trends and category breakdowns using Chart.js  
- **Filters:** Expenses can be filtered on the home page by day, week, or month.

---

## Contributing

Contributions and suggestions are welcome!

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-name`).  
3. Make your changes and commit (`git commit -am 'Add new feature'`).  
4. Push to the branch (`git push origin feature-name`).  
5. Open a pull request describing your changes.

---


## Contact

Project Maintainer – Abdelillah01  
- GitHub: [abdelillah01](https://github.com/abdelillah01)  
- Email: abdelillah.ouraou@gmail.com  

---

Thank you for using Expense Tracker!
