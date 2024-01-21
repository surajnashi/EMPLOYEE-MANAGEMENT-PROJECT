from django import forms
from emp.models import Employee_Management
from emp.models import Department_Management
from emp.models import Salary_Management


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_Management
        fields = ['emp_id','emp_name','emp_email','emp_address','hiring_date','salary','designation','reporting_manager']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department_Management
        fields = ['emp','dept_id','dept_name','dept_floor']


class SalaryForm(forms.ModelForm):
    class Meta:
        model =  Salary_Management
        fields = ['emp','dept','start_date','end_date','salary_amt','salary_date']