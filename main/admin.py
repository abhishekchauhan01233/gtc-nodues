from django.contrib import admin
from .models import studentdata, library, exams, accounts, transport, hostel, HOD_CSE, HOD_ECE, HOD_1ST_YEAR, HOD_AUTO, HOD_CIVIL, HOD_MANAGEMENT, HOD_ME
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(studentdata, library, exams, accounts, transport, hostel, HOD_CSE, HOD_ECE, HOD_1ST_YEAR, HOD_AUTO, HOD_CIVIL, HOD_MANAGEMENT, HOD_ME)
class ViewAdmin(ImportExportModelAdmin):
    pass

admin.site.site_header = 'GTC Administration'