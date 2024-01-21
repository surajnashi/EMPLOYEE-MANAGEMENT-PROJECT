from django.urls import path, include
from emp import views

app_name = 'emp'

urlpatterns = [
    path('empoylee/',views.employee, name='employee'),

    path('empform/',views.add_emp,name='add_emp'),

    path('update_emp/<int:emp_id>/',views.update_emp, name='update_emp'),

    path('delete_emp/<int:emp_id>/',views.delete_employee, name='delete_employee'),

    path('department/',views.departlist, name='department'),

    path('deptform/',views.add_dept, name='add_dept'),

    path('update_dept/<int:dept_id>/',views.update_dept, name='update_dept'),

    path('delete_dept/<int:dept_id>/',views.delete_dept, name='delete_dept'),

    path('salary/',views.salary, name='salary'),

    path('salaryform/',views.add_salary, name='add_salary'),

    path('update_salary/<int:sal_id>/',views.update_salary, name='update_salary'),

    path('delete_salary/<int:sal_id>/',views.delete_salary, name='delete_salary'),

    path('salary_report/',views.salary_report, name='salary_report'),
    
    path('department_hierarchy_report/',views.department_hierarchy_report, name='department_hierarchy_report')
]