"""
Django Calculator Project Setup Guide

This script provides instructions for setting up a basic Django calculator application.
Follow these steps to create and run your calculator app.
"""

print("Django Calculator Project Setup Guide")
print("====================================")
print("\nStep 1: Install Django")
print("  pip install django")

print("\nStep 2: Create a Django project")
print("  django-admin startproject calculator_project")
print("  cd calculator_project")

print("\nStep 3: Create a Django app")
print("  python manage.py startapp calc_app")

print("\nStep 4: Configure settings.py")
print("  Add 'calc_app' to INSTALLED_APPS in calculator_project/settings.py")

print("\nStep 5: Create URL patterns")
print("  Edit calculator_project/urls.py")
print("  Create calc_app/urls.py")

print("\nStep 6: Create views in calc_app/views.py")

print("\nStep 7: Create templates directory and calculator.html template")
print("  mkdir -p calc_app/templates/calc_app")
print("  Create calc_app/templates/calc_app/calculator.html")

print("\nStep 8: Run the development server")
print("  python manage.py runserver")

print("\nFollow the detailed instructions in the code comments to complete each step.")

# Project structure example
"""
calculator_project/
    manage.py
    calculator_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    calc_app/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        urls.py
        templates/
            calc_app/
                calculator.html
"""

# Step 5 - Main project URLs (calculator_project/urls.py) code:
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc_app.urls')),
]
"""

# Step 5 - App URLs (calc_app/urls.py) code:
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator_view, name='calculator'),
    path('calculate/', views.calculate, name='calculate'),
]
"""

# Step 6 - Views (calc_app/views.py) code:
"""
from django.shortcuts import render

def calculator_view(request):
    return render(request, 'calc_app/calculator.html')

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation', 'add')
        
        result = 0
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Division by zero'
                
        context = {
            'result': result,
            'num1': num1,
            'num2': num2,
            'operation': operation
        }
        return render(request, 'calc_app/calculator.html', context)
        
    return render(request, 'calc_app/calculator.html')
"""

# Step 7 - Template (calc_app/templates/calc_app/calculator.html) code:
"""
<!DOCTYPE html>
<html>
<head>
    <title>Django Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        .calculator {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 5px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, select {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        button {
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background-color: #f5f5f5;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Django Calculator</h1>
    
    <div class="calculator">
        <form method="post" action="{% url 'calculate' %}">
            {% csrf_token %}
            <div class="form-group">
                <label for="num1">First Number:</label>
                <input type="number" id="num1" name="num1" value="{{ num1|default:'' }}" step="any" required>
            </div>
            
            <div class="form-group">
                <label for="operation">Operation:</label>
                <select id="operation" name="operation">
                    <option value="add" {% if operation == 'add' %}selected{% endif %}>Addition (+)</option>
                    <option value="subtract" {% if operation == 'subtract' %}selected{% endif %}>Subtraction (-)</option>
                    <option value="multiply" {% if operation == 'multiply' %}selected{% endif %}>Multiplication (×)</option>
                    <option value="divide" {% if operation == 'divide' %}selected{% endif %}>Division (÷)</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="num2">Second Number:</label>
                <input type="number" id="num2" name="num2" value="{{ num2|default:'' }}" step="any" required>
            </div>
            
            <button type="submit">Calculate</button>
        </form>
        
        {% if result %}
        <div class="result">
            <h3>Result:</h3>
            <p>{{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""
