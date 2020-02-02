from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    established_on = models.DateField()

    def __str__(self):
        return self.dept_name


class Level(models.Model):
    level_name = models.CharField(max_length=100)
    pay_min = models.PositiveIntegerField()
    pay_max = models.PositiveIntegerField()

    def __str__(self):
        return self.leverl_name


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    reports_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    pas = models.PositiveIntegerField()
    joined_on = models.DateField()


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_day = models.DateField()
