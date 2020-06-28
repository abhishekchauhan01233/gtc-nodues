from django.contrib import admin
from django.contrib.auth.models import Group
from .models import studentdata, library, exams, accounts, transport, hostel, HOD_CSE, HOD_ECE, HOD_1ST_YEAR, HOD_AUTO, HOD_CIVIL, HOD_MANAGEMENT, HOD_ME
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class studentdata_Admin(ImportExportModelAdmin):
    exclude= ('user',)
    list_display = ('rollno', 'course', 'branch', 'sem', 'phone', )
    list_filter = ('course', 'branch', 'sem',)

class library_Admin(ImportExportModelAdmin):
    exclude= ('user',)
    list_display = ('rollno', 'course', 'branch', 'sem', 'phone', 'status', 'approval_status', )
    list_filter = ('approval_status', 'status', 'course', 'branch', 'sem',)

class exams_Admin(ImportExportModelAdmin):
    exclude= ('user',)
    list_display = ('rollno', 'course', 'branch', 'sem', 'phone', 'status', 'approval_status', )
    list_filter = ('approval_status', 'status', 'course', 'branch', 'sem',)

class accounts_Admin(ImportExportModelAdmin):
    exclude= ('user',)
    list_display = ('rollno', 'course', 'branch', 'sem', 'phone', 'status', 'approval_status', )
    list_filter = ('approval_status', 'status', 'course', 'branch', 'sem',)

class transport_Admin(ImportExportModelAdmin):
    exclude= ('user',)
    list_display = ('rollno', 'course', 'branch', 'sem', 'phone', 'status', 'approval_status', )
    list_filter = ('approval_status', 'status', 'course', 'branch', 'sem',)

class hostel_Admin(ImportExportModelAdmin):
    exclude= ('user',)
    list_display = ('rollno', 'course', 'branch', 'sem', 'phone', 'status', 'approval_status', )
    list_filter = ('approval_status', 'status', 'course', 'branch', 'sem',)

class HOD_CSE_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

class HOD_ECE_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

class HOD_1ST_YEAR_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

class HOD_AUTO_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

class HOD_CIVIL_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

class HOD_ME_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

class HOD_MANAGEMENT_Admin(ImportExportModelAdmin):
    exclude = ('user', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel',)
    list_display = ('rollno', 'approval_library', 'approval_exams', 'approval_accounts', 'approval_transport', 'approval_hostel', 'approval_hod')
    list_filter = ('sem',)

admin.site.site_header = 'GTC Administration'
admin.site.index_title = 'Nodues Forms'
admin.site.unregister(Group)

admin.site.register(studentdata, studentdata_Admin)
admin.site.register(library, library_Admin)
admin.site.register(exams, exams_Admin)
admin.site.register(accounts, accounts_Admin)
admin.site.register(transport, transport_Admin)
admin.site.register(hostel, hostel_Admin)
admin.site.register(HOD_CSE, HOD_CSE_Admin)
admin.site.register(HOD_ECE, HOD_ECE_Admin)
admin.site.register(HOD_1ST_YEAR, HOD_1ST_YEAR_Admin)
admin.site.register(HOD_AUTO, HOD_AUTO_Admin)
admin.site.register(HOD_CIVIL, HOD_CIVIL_Admin)
admin.site.register(HOD_ME, HOD_ME_Admin)
admin.site.register(HOD_MANAGEMENT, HOD_MANAGEMENT_Admin)