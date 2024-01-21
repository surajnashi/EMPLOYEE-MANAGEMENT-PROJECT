from django.db import models

# Create your models here.

class Employee_Management(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(max_length=200)
    emp_address = models.CharField(max_length = 200)
    hiring_date = models.DateField()
    salary = models.FloatField()
    DES = (
        ('TL', 'Team Lead'),
        ('Associate', 'Associate'),
        ('Manager', 'Manager'),
    )
    REPORT_MGN = (
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
        ('Owner', 'Owner')
    )
    designation = models.CharField(max_length=100, choices=DES)
    reporting_manager = models.CharField(max_length=100, choices=REPORT_MGN)


    def __str__(self):
        return self.emp_name



class Department_Management(models.Model):
    emp = models.ForeignKey(Employee_Management, on_delete=models.CASCADE)
    dept_id = models.CharField(max_length = 100)
    dept_name = models.CharField(max_length=250)
    dept_floor = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name
    
class Salary_Management(models.Model):
    emp = models.ForeignKey(Employee_Management, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department_Management, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amt = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.emp.emp_name} - {self.salary_amt}"
