from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_id = models.CharField(max_length=50)
    emp_name = models.CharField(max_length=50)
    emp_desi = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name