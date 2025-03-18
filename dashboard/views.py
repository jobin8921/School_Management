from django.shortcuts import render, redirect

# Admin Dashboard
def admin_dashboard(request):
    if 'username' not in request.session or request.session.get('role') != 'admin':
        return redirect('login')
    return render(request, 'dashboard/admin.html')

# Staff Dashboard
def staff_dashboard(request):
    if 'username' not in request.session or request.session.get('role') != 'staff':
        return redirect('login')
    return render(request, 'dashboard/staff.html')

# Student Dashboard
def student_dashboard(request):
    if 'username' not in request.session or request.session.get('role') != 'student':
        return redirect('login')
    return render(request, 'dashboard/student.html')

