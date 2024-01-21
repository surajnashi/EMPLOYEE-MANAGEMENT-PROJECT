from django.contrib import admin
from emp.models import Employee_Management, Department_Management, Salary_Management

# Register your models here.

admin.site.register(Employee_Management)
admin.site.register(Department_Management)
admin.site.register(Salary_Management)