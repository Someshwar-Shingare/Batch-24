from django.contrib import admin
from testapp1.models import Employee 

# Register your models here.

class  EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'name', 'sal','address']

admin.site.register(Employee,EmployeeAdmin)

