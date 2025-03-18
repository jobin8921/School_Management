from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin, Staff, Student

# Temporary credentials for development
TEMP_USERS = {
    "admin": {"username": "admin123", "password": "adminpass", "role": "admin"},
    "staff": {"username": "staff123", "password": "staffpass", "role": "staff"},
    "student": {"username": "student123", "password": "studentpass", "role": "student"},
}

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check against temporary credentials
        user = None
        for key, creds in TEMP_USERS.items():
            if creds["username"] == username and creds["password"] == password:
                user = creds
                break

        if user:
            request.session['username'] = user['username']
            request.session['role'] = user['role']
            
            # Redirect to respective dashboard
            if user['role'] == 'admin':
                return redirect('admin_dashboard')
            elif user['role'] == 'staff':
                return redirect('staff_dashboard')
            elif user['role'] == 'student':
                return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'users/login.html')


# Manual logout
def logout_view(request):
    request.session.flush()
    return redirect('login')

# Registration for different user types
# def register_view(request):
#     if request.method == "POST":
#         role = request.POST['role']
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']

#         if role == "admin":
#             Admin.objects.create(username=username, password=password, email=email)
#         elif role == "staff":
#             department = request.POST['department']
#             Staff.objects.create(username=username, password=password, email=email, department=department)
#         elif role == "student":
#             roll_number = request.POST['roll_number']
#             course = request.POST['course']
#             Student.objects.create(username=username, password=password, email=email, roll_number=roll_number, course=course)
        
#         messages.success(request, "Registration successful. Please login.")
#         return redirect('login')

#     return render(request, 'users/register.html')
