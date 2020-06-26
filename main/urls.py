from django.urls import path
from . import views
from nodues import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('erp/', views.erp, name='erp'),
    path('student/', views.student, name='student'),
    path('library/', views.Library, name='library'),
    path('library_payment', views.Library_Payment, name='Library_Payment'),
    path('exams_payment', views.Exams_Payment, name='Exams_Payment'),
    path('accounts_payment', views.Accounts_Payment, name='Accounts_Payment'),
    path('transport_payment', views.Transport_Payment, name='Transport_Payment'),
    path('hostel_payment', views.Hostel_Payment, name='Hostel_Payment'),
    path('accounts/', views.Accounts, name='accounts'),
    path('exams/', views.Exams, name='exams'),
    path('transport/', views.Transport, name='transport'),
    path('hostel/', views.Hostel, name='hostel'),
    path('hod/', views.hod, name='HOD'),
    path('admin_login/',views.admin_login, name='admin_login'),
    path('admin_library/', views.admin_library, name='admin_library'),
    path('admin_exams/', views.admin_exams, name='admin_exams'),
    path('admin_accounts/', views.admin_accounts, name='admin_accounts'),
    path('admin_transport/', views.admin_transport, name='admin_transport'),
    path('admin_hostel/', views.admin_hostel, name='admin_hostel'),
    path('admin_hod/', views.admin_hod, name='admin_hod'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)