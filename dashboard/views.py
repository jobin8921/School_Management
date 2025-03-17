from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def dashboard(request):
    if 'username' not in request.session:
        return redirect('login')

    role = request.session.get('role', 'student')
    return render(request, 'dashboard/index.html', {'role': role})
