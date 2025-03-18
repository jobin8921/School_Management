from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, Staff, Student

# Manual login logic
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Check in Admins
        user = Admin.objects.filter(username=username, password=password).first()
        if not user:
            user = Staff.objects.filter(username=username, password=password).first()
        if not user:
            user = Student.objects.filter(username=username, password=password).first()
        
        if user:
            request.session['username'] = user.username
            request.session['role'] = user.__class__.__name__.lower()  # "admin", "staff", "student"
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'users/login.html')

# Manual logout
def logout_view(request):
    request.session.flush()
    return redirect('login')

# Registration for different user types
def register_view(request):
    if request.method == "POST":
        role = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if role == "admin":
            Admin.objects.create(username=username, password=password, email=email)
        elif role == "staff":
            department = request.POST['department']
            Staff.objects.create(username=username, password=password, email=email, department=department)
        elif role == "student":
            roll_number = request.POST['roll_number']
            course = request.POST['course']
            Student.objects.create(username=username, password=password, email=email, roll_number=roll_number, course=course)
        
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'users/register.html')
