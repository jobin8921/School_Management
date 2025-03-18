from django.contrib import admin
from django.urls import path, include
from dashboard.views import admin_dashboard,staff_dashboard,student_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('dashboard/admin/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/staff/', staff_dashboard, name='staff_dashboard'),
    path('dashboard/student/', student_dashboard, name='student_dashboard'),
]

