# 🍽️ Django Food Order Management Web App

A streamlined and responsive web application built with Django, designed to facilitate online food ordering and management for restaurants and customers.

---

## 📖 Table of Contents

- [🍽️ Django Food Order Management Web App](#️django-food-order-management-web-app)
- [📖 Table of Contents](#-table-of-contents)
- [🧑‍🍳 User Experience (UX)](#-user-experience-ux)
  - [🧾 User Stories](#-user-stories)
- [🎨 Design](#-design)
  - [🗂 Interface Structure](#-interface-structure)
  - [🌈 Color Scheme & Typography](#-color-scheme--typography)
- [🚀 Features](#-features)
  - [✅ Implemented Features](#-implemented-features)
  - [🛠️ Planned Improvements](#-planned-improvements)
- [💻 Technologies Used](#-technologies-used)
  - [🧑‍💻 Languages Used](#-languages-used)
  - [📚 Libraries Used](#-libraries-used)
- [📁 Project Files](#-project-files)
- [🛠 Installation & Usage](#-installation--usage)
  - [⚙️ How to Run](#-how-to-run)
  - [🧾 Configuration](#-configuration)
- [🔒 Security & Environment Configuration](#-security--environment-configuration)
  - [🧑‍💻 Use of `python-dotenv`](#-use-of-python-dotenv)
  - [🔧 Setting Up a Forked Repository](#-setting-up-a-forked-repository)
- [✅ Testing](#-testing)
  - [🧪 Test Scenarios Checklist](#-test-scenarios-checklist)
  - [🧪 Running Tests](#-running-tests)
- [🙌 Credits](#-credits)
  - [👨‍💻 Author](#-author)
  - [🧰 Tools & Technologies](#-tools--technologies)
  - [📚 Learning Resources & Documentation](#-learning-resources--documentation)

---

## 🧑‍🍳 User Experience (UX)

The application is designed to simplify the food ordering process for customers and streamline order management for restaurant staff. It offers an intuitive interface for browsing menus, placing orders, and managing order workflows.

### 🧾 User Stories

- **As a customer**, I want to browse the restaurant menu and place orders online, so that I can enjoy meals conveniently.
- **As a restaurant staff member**, I want to manage incoming orders efficiently, so that I can ensure timely preparation and delivery.
- **As a system administrator**, I want to deploy and maintain the application with ease, so that it remains reliable and scalable.

---

## 🎨 Design

### 🗂 Interface Structure

- **Home Page**: Welcomes users and provides navigation to the menu.
- **Menu Page**: Displays available food items with descriptions and prices.
- **Order Page**: Allows customers to select items, specify quantities, and place orders.
- **Admin Dashboard**: Enables staff to view and manage incoming orders.

### 🌈 Color Scheme & Typography

- **Color Scheme**: Warm and appetizing colors like red and orange to stimulate appetite.
- **Typography**: Clean and readable fonts such as Arial or Helvetica for clarity.

---

## 🚀 Features

### ✅ Implemented Features

- **Menu Display**: Showcases food items with images, descriptions, and prices.
- **Order Placement**: Allows customers to select items and place orders.
- **Order Management**: Enables staff to view, update, and track orders.
- **Responsive Design**: Ensures usability across various devices.

### 🛠️ Planned Improvements

- **User Authentication**: Implement login and registration for customers and staff.
- **Payment Integration**: Add online payment options for orders.
- **Order Notifications**: Notify staff of new orders in real-time.
- **Order History**: Allow customers to view their past orders.

---

## 💻 Technologies Used

### 🧑‍💻 Languages Used

- **Python**: Backend logic and server-side operations.
- **HTML/CSS**: Structure and styling of web pages.
- **JavaScript**: Enhancements for interactivity.

### 📚 Libraries Used

- **Django**: Web framework for handling routes and server logic.
- **SQLite**: Lightweight database for storing order data.
- **Bootstrap**: Frontend framework for responsive design.

---

## 📁 Project Files

- `manage.py`: Django's command-line utility for administrative tasks.
- `foodsite/`: Main project directory containing settings and configurations.
- `restaurant_menu/`: Django app handling menu and order functionalities.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files like CSS and JavaScript.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Documentation and instructions.

---

## 🛠 Installation & Usage

### ⚙️ How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/mahmudurmahid/django-food-order-management-web-app.git
cd django-food-order-management-web-app
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the application:
   Open your browser and navigate to http://localhost:8000.

### 🧾 Configuration

Database: The application uses SQLite by default; ensure the database file is accessible and has proper permissions.

Static Files: Collect static files using Django's collectstatic command for production deployment.

---

## 🔒 Security & Environment Configuration

### 🧑‍💻 Use of python-dotenv

To manage environment variables securely, the application can utilize the python-dotenv library. This allows sensitive information, such as secret keys and database credentials, to be stored in a .env file, which is not committed to version control.

### 🔧 Setting Up a Forked Repository

1. Install python-dotenv:

```bash
pip install python-dotenv
```

2. Create a .env file in the root directory with the following content:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
```

Replace your-secret-key-here with a securely generated secret key.

3. Load environment variables in your settings by adding the following to settings.py:

```bash
from dotenv import load_dotenv
load_dotenv()
```

---

## ✅ Testing

### 🧪 Test Scenarios Checklist

This project includes several test cases to ensure that the application is working as expected:

| **Feature**       | **Test Type** | **Status** |
| ----------------- | ------------- | ---------- |
| Menu Display      | Unit          | ✅ Passed  |
| Order Placement   | Integration   | ✅ Passed  |
| Order Management  | Integration   | ✅ Passed  |
| Responsive Design | Manual        | ✅ Passed  |
| Error Handling    | Unit / Manual | ✅ Passed  |

### 🧪 Running Tests

To run tests on your local environment:

1. **Install testing dependencies**:

```bash
pip install pytest
```

2. **Run tests**:

```bash
pytest
```

This will run all the tests and output a summary of the results.

### 🧰 Tools & Technologies

The web app utilizes the following tools and technologies:

| Tool/Library | Purpose                                  |
| ------------ | ---------------------------------------- |
| Python       | Core programming language                |
| Django       | Web framework for building the app       |
| SQLite       | Database for storing order data          |
| Bootstrap    | Frontend framework for responsive design |

### 📚 Learning Resources & Documentation

The following resources were helpful during the development:

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
