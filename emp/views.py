from django.shortcuts import render, redirect
from emp.models import Employee_Management, Department_Management, Salary_Management
from emp.forms import EmployeeForm, DepartmentForm, SalaryForm
from django.db.models import Sum

# Create your views here.

def employee(request):
    emplist = Employee_Management.objects.all()

    context = {
        'emplist':emplist
    }

    return render(request, 'emp/emplist.html', context)



def add_emp(request):
    emp_form = EmployeeForm(request.POST or None)

    if emp_form.is_valid():
        emp_form.save()
        return redirect('emp:employee')
        
    context = {
        'emp_form':emp_form
    }

    return render(request, 'emp/emp_form.html', context)



def update_emp(request, emp_id):
    emp = Employee_Management.objects.get(pk = emp_id)
    emp_form = EmployeeForm(request.POST or None, instance=emp)


    if emp_form.is_valid():
        emp_form.save()
        return redirect('emp:employee')
    
    context = {
        'emp_form': emp_form
    }

    return render(request, 'emp/emp_form.html', context)


def delete_employee(request, emp_id):
    emp = Employee_Management.objects.get(pk = emp_id)

    context = {
        'emp':emp
    }

    if request.method == 'POST':
        emp.delete()
        return redirect('emp:employee')

    return render(request, 'emp/emp_delete.html', context)


def departlist(request):
    deptlist = Department_Management.objects.all()

    context = {
        'deptlist':deptlist
    }

    return render(request, 'emp/deptlist.html', context)

def add_dept(request):
    dept_form = DepartmentForm(request.POST or None)

    if dept_form.is_valid():
        dept_form.save()
        return redirect('emp:department')
        
    context = {
        'dept_form':dept_form
    }

    return render(request, 'emp/dept_form.html', context)

def update_dept(request, dept_id):
    dept = Department_Management.objects.get(pk = dept_id)
    dept_form = DepartmentForm(request.POST or None, instance=dept)


    if dept_form.is_valid():
        dept_form.save()
        return redirect('emp:department')
    
    context = {
        'dept_form': dept_form
    }

    return render(request, 'emp/dept_form.html', context)

def salary(request):
    sal = Salary_Management.objects.all()

    context = {
        'sal':sal
    }

    return render (request, 'emp/salary.html', context)

def delete_dept(request, dept_id):
    dept = Department_Management.objects.get(pk = dept_id)

    context = {
        'dept':dept
    }

    if request.method == 'POST':
        dept.delete()
        return redirect('emp:department')

    return render(request, 'emp/dept_delete.html', context)


def add_salary(request):
    salary_form = SalaryForm(request.POST or None)

    if salary_form.is_valid():
        salary_form.save()
        return redirect('emp:employee')
        
    context = {
        'salary_form':salary_form
    }

    return render(request, 'emp/salary_form.html', context)


def update_salary(request, sal_id):
    sal = Salary_Management.objects.get(pk = sal_id)
    salary_form = SalaryForm(request.POST or None, instance=sal)


    if salary_form.is_valid():
        salary_form.save()
        return redirect('emp:employee')
    
    context = {
        'salary_form': salary_form
    }

    return render(request, 'emp/salary_form.html', context)


def delete_salary(request, sal_id):
    salary = Salary_Management.objects.get(pk = sal_id)

    context = {
        'salary':salary
    }

    if request.method == 'POST':
        salary.delete()
        return redirect('emp:employee')

    return render(request, 'emp/salary_delete.html', context)


def salary_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')


        salaries = Salary_Management.objects.filter(salary_date__range=[start_date, end_date])
        total_department_costs = salaries.values('dept__dept_name').annotate(total_cost=Sum('salary_amt'))

        context = {
            'start_date': start_date,
            'end_date': end_date,
            'total_department_costs': total_department_costs,
        }

        return render(request, 'emp/salary_report.html', context)

    return render(request, 'emp/salary_report.html', {})


def department_hierarchy_report(request, dept_id):
    department = Department_Management.objects.get(id=dept_id)
    
    manager = Employee_Management.objects.get(reporting_manager='Manager', dept=department)
    team_leads = Employee_Management.objects.filter(reporting_manager='TL', dept=department)
    
    hierarchy = {}
    for tl in team_leads:
        hierarchy[tl] = Employee_Management.objects.filter(reporting_manager=tl.emp_name, dept=department)

    context = {
        'department': department,
        'manager': manager,
        'team_leads': team_leads,
        'hierarchy': hierarchy,
    }

    return render(request, 'department_hierarchy_report.html', context)