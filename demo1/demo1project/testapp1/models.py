from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=50)
    sal = models.FloatField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


